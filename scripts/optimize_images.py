from pathlib import Path

from PIL import Image, ImageOps


SOURCE = Path("/private/tmp/cop31-drive-assets")
DESTINATION = Path(__file__).resolve().parents[1] / "dist" / "assets" / "photos"
MAX_SIZE = (1920, 1280)


def main() -> None:
    DESTINATION.mkdir(parents=True, exist_ok=True)
    converted = 0

    for source_path in sorted(SOURCE.iterdir()):
        if not source_path.is_file():
            continue

        with Image.open(source_path) as image:
            image = ImageOps.exif_transpose(image).convert("RGB")
            image.thumbnail(MAX_SIZE, Image.Resampling.LANCZOS)
            output_path = DESTINATION / f"{source_path.stem}.webp"
            image.save(output_path, "WEBP", quality=82, method=6)
            converted += 1

    cop31_logo = DESTINATION.parent / "cop31-logo.png"
    if cop31_logo.exists():
        with Image.open(cop31_logo) as logo:
            rgba_logo = logo.convert("RGBA")
            alpha_box = rgba_logo.getchannel("A").getbbox()
            if alpha_box:
                rgba_logo.crop(alpha_box).save(cop31_logo, "PNG", optimize=True)

    print(f"Converted {converted} images into {DESTINATION}")


if __name__ == "__main__":
    main()
