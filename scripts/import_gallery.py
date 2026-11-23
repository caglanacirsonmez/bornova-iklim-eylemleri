#!/usr/bin/env python3
"""Import the name-based COP31 photo folders into stable site galleries.

Topic folders are matched by their Turkish names, not by a numeric prefix.
Raster images are converted to responsive WebP assets. A one-page PDF placed
in a topic folder is rendered as a gallery image so certificates can be shown
inside the kiosk experience as well.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import tempfile
import unicodedata
from pathlib import Path

from PIL import Image, ImageFile, ImageOps


DEFAULT_SOURCE = Path("/Volumes/WORK/2026/10-EKİM/COP31 Dashboard/Fotoğraflar")
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DESTINATION = PROJECT_ROOT / "dist" / "assets" / "gallery"
MANIFEST = PROJECT_ROOT / "dist" / "gallery-manifest.js"
MAX_SIZE = (2000, 1600)
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
SOURCE_EXTENSIONS = IMAGE_EXTENSIONS | {".pdf"}
ImageFile.LOAD_TRUNCATED_IMAGES = True


# The category number is still present in the five top-level directories, but
# all topic matching below is name-based. Aliases cover the one spelling
# difference between the Drive folder and its locally synced directory.
TOPIC_GROUPS = [
    {
        "category": "gida-tarim-saglik",
        "source_category": 1,
        "topics": [
            ("kent-bostani", ("9 Kent Bostanı",)),
            ("ekolojik-kent-yerel-tohum-merkezi", ("Ekolojik Kent Yerel Tohum Merkezi",)),
            ("dayanisma-tarlasi", ("Dayanışma Tarlası",)),
            ("biyocesitlilik-envanteri", ("Biyoçeşitlilik Envanteri", "Bioçeşitlik Envanteri")),
            ("tarimsal-egitimler", ("Tarımsal Eğitimler",)),
            ("aricilik-faaliyetleri", ("Arıcılık Faaliyetleri",)),
            ("cografi-isaretli-urunler", ("Coğrafi İşaretli Ürünler",)),
            ("akilli-sulama-sistemi", ("Abide-i Hürriyet Parkı Akıllı Sulama Sistemi",)),
        ],
    },
    {
        "category": "enerji-ulastirma",
        "source_category": 2,
        "topics": [
            ("hibrit-direkler", ("Hibrit Direkler",)),
            ("elektrikli-arac-kullanimi", ("Elektrikli Minibüs",)),
            ("cati-ges", ("Yenilenebilir Enerji Üretimi (Çatı GES)",)),
            ("arazi-tipi-ges", ("Arazi tipi GES",)),
            ("sarj-uniteleri", ("Elektrikli Araç Şarj Üniteleri",)),
            ("aydinlatma-donusumu", ("Enerji Tasarrufu ve Aydınlatma Dönüşümü",)),
            ("uluslararasi-uyelikler", ("Uluslararası Üyelikler",)),
            ("kardes-sehirler", ("Kardeş Şehirler",)),
            ("energy-cities", ("Avrupa Enerji Kentleri Ağı Üyeliği ENERGY CITIES",)),
        ],
    },
    {
        "category": "dayanikli-sehirler",
        "source_category": 3,
        "topics": [
            ("dijital-ikiz", ("Dijital ikiz",)),
            ("borneye", ("Born-Eye",)),
            ("yoma", ("YOMA",)),
            ("bak", ("Bornova Belediyesi Arama Kurtarma Ekibi BAK",)),
            ("tulpar", ("Bornova Acil Durum Erken Uyarı ve Müdahale Sistemi : TULPAR",)),
            ("ust-ortu", ("Üst Örtü Projesi",)),
        ],
    },
    {
        "category": "insani-sosyal-kalkinma",
        "source_category": 4,
        "topics": [
            ("gulsah-durbay-genclik-merkezi", ("Gülşah Durbay Gençlik Merkezi",)),
            ("kent-marketler", ("Kent Market",)),
            ("kent-lokantalari", ("Kent Lokantası",)),
            ("sicak-yemek-destegi", ("Sıcak Yemek Desteği",)),
            ("kent-kasap", ("KENT KASAP",)),
            ("beslenme-paketi", ("Miniklere Beslenme Paketi Desteği",)),
            ("belgem", ("BELGEM Ücretsiz Dershane",)),
            ("oyuncak-kutuphanesi", ("Oyuncak Kütüphanesi",)),
            ("altin-bilezik", ("Altın Bilezik",)),
            ("cocuk-oyun-aktivite", ("Çocuk Oyun ve Aktivite Merkezleri",)),
            ("danismanlik-destek", ("Danışmanlık ve Destek Programları",)),
            ("adli-yardim", ("Adli Yardım Desteği",)),
            ("hos-geldin-bebek", ("Hoş Geldin Bebek",)),
            ("kadin-cocuk-egitim-atolye", ("Kadınlar ve Çocuklara Yönelik Eğitim ve Atölyeler",)),
            ("mutfak-atolyesi", ("Mutfak Atölyesi",)),
            ("hobi-beceri-kurslari", ("Hobi ve Beceri Edindirme Kursları",)),
            ("bornova-miras", ("Bornova Miras",)),
            ("kultur-rotalari", ("Kültür Rotaları",)),
        ],
    },
    {
        "category": "sifir-atik",
        "source_category": 5,
        "topics": [
            ("atik-bank", ("Atık Bank",)),
            ("kompost-uretimi", ("Kompost Üretimi",)),
            ("sifir-atik-belgesi", ("SIFIR ATIK BELGE",)),
            ("atik-toplayicilari-entegrasyonu", ("Bağımsız Sıfır Atık Toplayıcılarının Atık Yönetim Sistemine Entegrasyonu",)),
            ("atik-getirme-merkezi", ("Atık Getirme Merkezi ve Atıktan Sanata Atölyesi",)),
            ("depozito-yonetim-sistemi", ("Depozito Yönetim Sistemi",)),
            ("tambur-kompost", ("Tambur Kompost Projesi",)),
            ("atik-yonetimi-egitimleri", ("İklim Değişikliği ve Atık Yönetimi Eğitimleri",)),
            ("bireysel-karbon-ayak-izi", ("Bireysel Karbon Ayak İzi",)),
            ("belkahve", ("BELKAHVE İnşaat Metal Geri Dönüşüm Ticaret ve Sanayi A.Ş.",)),
            ("akilli-bank", ("Akıllı Bank",)),
        ],
    },
]


# These two files still exist in the local sync but were removed from the Drive
# folder. Keeping the exclusions here prevents a later import from reviving
# photos that are no longer part of the approved Drive selection.
DRIVE_REMOVED_FILES = {
    "WhatsApp Image 2026-10-09 at 12.05.02.jpeg",
    "YZC_6749-2.jpg",
}


def normalize_name(value: str) -> str:
    value = unicodedata.normalize("NFC", value).strip()
    value = re.sub(r"^\d+\s*-\s*", "", value)
    value = re.sub(r"\s+", " ", value)
    return value.casefold()


def numbered_directories(parent: Path) -> dict[int, Path]:
    directories = {}
    for path in parent.iterdir():
        if not path.is_dir() or path.name.startswith("."):
            continue
        match = re.match(r"^(\d+)\s*-", unicodedata.normalize("NFC", path.name))
        if match:
            directories[int(match.group(1))] = path
    return directories


def topic_directory(parent: Path, aliases: tuple[str, ...]) -> Path:
    candidates = {
        normalize_name(path.name): path
        for path in parent.iterdir()
        if path.is_dir() and not path.name.startswith(".")
    }
    for alias in aliases:
        match = candidates.get(normalize_name(alias))
        if match:
            return match
    raise FileNotFoundError(f"Topic folder not found under {parent}: {aliases[0]}")


def source_files(parent: Path, excluded_names: set[str]) -> list[Path]:
    excluded = {normalize_name(name) for name in excluded_names}
    return sorted(
        (
            path
            for path in parent.iterdir()
            if path.is_file()
            and not path.name.startswith(".")
            and path.suffix.lower() in SOURCE_EXTENSIONS
            and normalize_name(path.name) not in excluded
        ),
        key=lambda path: normalize_name(path.name),
    )


def file_digest(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def save_webp(source: Path, destination: Path) -> None:
    with Image.open(source) as image:
        image = ImageOps.exif_transpose(image)
        if image.mode in {"RGBA", "LA"}:
            background = Image.new("RGB", image.size, "white")
            background.paste(image, mask=image.getchannel("A"))
            image = background
        else:
            image = image.convert("RGB")
        image.thumbnail(MAX_SIZE, Image.Resampling.LANCZOS)
        image.save(destination, "WEBP", quality=82, method=5)


def save_source_as_webp(source: Path, destination: Path, temporary: Path) -> None:
    if source.suffix.lower() != ".pdf":
        save_webp(source, destination)
        return

    renderer = shutil.which("pdftoppm")
    if not renderer:
        raise RuntimeError("pdftoppm is required to render PDF gallery documents")
    prefix = temporary / destination.stem
    subprocess.run(
        [renderer, "-f", "1", "-l", "1", "-singlefile", "-r", "180", "-png", str(source), str(prefix)],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    save_webp(prefix.with_suffix(".png"), destination)


def main() -> None:
    parser = argparse.ArgumentParser(description="Import every name-based COP31 gallery photo.")
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument(
        "--exclude-name",
        action="append",
        default=[],
        help="Ignore a source filename that is not part of the approved Drive folder.",
    )
    parser.add_argument(
        "--asset-version",
        default="",
        help="Optional cache-busting token appended to every generated gallery URL.",
    )
    args = parser.parse_args()

    if not args.source.is_dir():
        raise SystemExit(f"Gallery source not found: {args.source}")
    if args.asset_version and not re.fullmatch(r"[A-Za-z0-9._-]+", args.asset_version):
        raise SystemExit("Asset version may contain only letters, numbers, dots, dashes, and underscores.")

    excluded_names = DRIVE_REMOVED_FILES | set(args.exclude_name)
    asset_suffix = f"?v={args.asset_version}" if args.asset_version else ""
    categories = numbered_directories(args.source)
    missing_categories = [group["source_category"] for group in TOPIC_GROUPS if group["source_category"] not in categories]
    if missing_categories:
        raise SystemExit(f"Missing category folders: {missing_categories}")

    DESTINATION.mkdir(parents=True, exist_ok=True)
    preserved_togg_files = sorted(DESTINATION.glob("c02-t03-??.webp"))
    keyed_manifest: dict[str, list[str]] = {}
    category_manifest: dict[str, list[list[str]]] = {}
    digest_to_url: dict[str, str] = {}
    imported = 0
    reused = 0

    with tempfile.TemporaryDirectory(prefix="cop31-gallery-") as temporary_directory:
        temporary = Path(temporary_directory)
        for group in TOPIC_GROUPS:
            category_path = categories[group["source_category"]]
            category_entries = []
            for topic_id, aliases in group["topics"]:
                folder = topic_directory(category_path, aliases)
                sources = source_files(folder, excluded_names)
                urls = []
                for image_number, source in enumerate(sources, start=1):
                    digest = file_digest(source)
                    url = digest_to_url.get(digest)
                    if url:
                        reused += 1
                    else:
                        filename = f"{topic_id}-{image_number:02d}.webp"
                        save_source_as_webp(source, DESTINATION / filename, temporary)
                        url = f"assets/gallery/{filename}{asset_suffix}"
                        digest_to_url[digest] = url
                        imported += 1
                    if url not in urls:
                        urls.append(url)
                keyed_manifest[topic_id] = urls
                category_entries.append(urls)
            category_manifest[group["category"]] = category_entries

    # The new Turkish source combines electric vehicle work into one topic.
    # Keep the earlier English E-Minibus and TOGG pages functional.
    keyed_manifest["elektrikli-minibus"] = keyed_manifest["elektrikli-arac-kullanimi"]
    keyed_manifest["togg-araclar"] = [
        f"assets/gallery/{path.name}{asset_suffix}" for path in preserved_togg_files
    ]

    referenced_files = {
        Path(url.split("?", 1)[0]).name
        for urls in keyed_manifest.values()
        for url in urls
    }
    for output_path in DESTINATION.glob("*.webp"):
        if output_path.name not in referenced_files:
            output_path.unlink()

    source = (
        "window.COP31_GALLERY = "
        + json.dumps(category_manifest, ensure_ascii=False, indent=2)
        + ";\n\nwindow.COP31_GALLERY_BY_KEY = "
        + json.dumps(keyed_manifest, ensure_ascii=False, indent=2)
        + ";\n"
    )
    MANIFEST.write_text(source, encoding="utf-8")
    print(
        f"Imported {imported} unique assets, reused {reused} duplicate selections, "
        f"and wrote {MANIFEST}"
    )


if __name__ == "__main__":
    main()
