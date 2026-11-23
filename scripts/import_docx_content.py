#!/usr/bin/env python3
"""Import the Turkish COP31 dashboard copy from the approved DOCX source.

The source document controls wording, paragraph order, bold/italic emphasis,
lists, and link labels. Site-specific topic IDs, gallery keys, and metric cards
are declared below so content updates cannot shift existing photography.
"""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path


W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PKG_REL = "http://schemas.openxmlformats.org/package/2006/relationships"
NS = {"w": W, "r": R}


def topic(
    item_id,
    title,
    start,
    end,
    *,
    lead=None,
    link=None,
    gallery_keys=(),
    metrics=(),
):
    return {
        "id": item_id,
        "title": title,
        "start": start,
        "end": end,
        "lead": lead,
        "link": link,
        "galleryKeys": list(gallery_keys),
        "metrics": [list(metric) for metric in metrics],
    }


LEGACY_CATEGORIES = [
    {
        "id": "gida-tarim-saglik",
        "title": "Gıda, Tarım ve Sağlık",
        "accent": "#85A283",
        "accentSoft": "#85A283",
        "accentInk": "#062D3C",
        "homeImage": "assets/gallery/dayanisma-tarlasi-02.webp?v=20261104c",
        "homePosition": "50% 50%",
        "icon": "sprout",
        "topics": [
            topic("kent-bostani", "Kent Bostanı", 3, 16, lead=4, gallery_keys=("kent-bostani",), metrics=(("9", "kent bostanı"), ("1.189", "üretim yapan kadın"))),
            topic("ekolojik-kent-yerel-tohum-merkezi", "Ekolojik Kent Yerel Tohum Merkezi", 18, 29, gallery_keys=("ekolojik-kent-yerel-tohum-merkezi",), metrics=(("193K", "dağıtılan tohum"), ("1K", "sergilenen tohum"), ("1.808K", "fide dağıtımı"), ("220K", "halka dağıtılan yazlık fide"), ("250+", "korunan yerel tohum çeşidi"))),
            topic("dayanisma-tarlasi", "Dayanışma Tarlası", 31, 36, lead=32, gallery_keys=("dayanisma-tarlasi",), metrics=(("15 dönüm", "üretim alanı"), ("86 ton", "vatandaşa ulaşan sebze"))),
            topic("biyocesitlilik-envanteri", "Biyoçeşitlilik Envanteri", 38, 44, lead=39, gallery_keys=("biyocesitlilik-envanteri",), metrics=(("519", "toplam kayıtlı tür"), ("433", "bitki türü"), ("41", "kuş türü"), ("23", "sürüngen türü"), ("22", "memeli türü"))),
            topic("tarimsal-egitimler", "Tarımsal Eğitimler", 46, 49, metrics=(("14K", "çocuklara ekolojik eğitim"), ("8.5K", "üreticiye tarımsal eğitim"), ("2.2K", "kadına sağlıklı gıda atölyesi"))),
            topic("aricilik-faaliyetleri", "Arıcılık Faaliyetleri", 51, 56, metrics=(("320", "yeni arıcı"), ("440 kg", "paylaşılan bal"))),
            topic("cografi-isaretli-urunler", "Coğrafi İşaretli Ürünler", 57, 60, lead=58, metrics=(("2", "tescilli yerel ürün"), ("1", "başvuru sürecindeki değer"))),
            topic("akilli-sulama-sistemi", "Abide-i Hürriyet Parkı Akıllı Sulama Sistemi", 61, 62, gallery_keys=("akilli-sulama-sistemi",), metrics=(("Dijital İkiz", "uzaktan kontrol"), ("Nem sensörleri", "ihtiyaca göre sulama"))),
        ],
    },
    {
        "id": "enerji-ulastirma",
        "title": "Enerji ve Ulaştırma",
        "accent": "#72A4C9",
        "accentSoft": "#AEC4D2",
        "accentInk": "#062D3C",
        "homeImage": "assets/gallery/hibrit-direkler-09.webp?v=20261104c",
        "homePosition": "50% 50%",
        "icon": "energy",
        "topics": [
            topic("hibrit-direkler", "Hibrit Direkler", 66, 71, gallery_keys=("hibrit-direkler",), metrics=(("6 kW", "günlük maksimum üretim"), ("%40", "Abide-i Hürriyet Parkı enerjisi"), ("650 Wh", "11 m/s rüzgârda üretim"), ("950 Wh", "güneş panelleri"))),
            topic("elektrikli-arac-kullanimi", "Elektrikli Araç Kullanımı", 73, 77, gallery_keys=("elektrikli-arac-kullanimi",), metrics=(("2", "17 kişilik elektrikli minibüs"), ("3", "elektrikli binek araç"), ("1.500 km", "aylık ortalama yol"), ("8.640 kg", "yıllık önlenen CO₂e"))),
            topic("cati-ges", "Yenilenebilir Enerji Üretimi (Çatı GES)", 79, 81, gallery_keys=("cati-ges",), metrics=(("3", "uygulama noktası"), ("362 kWp", "toplam kurulu güç"))),
            topic("arazi-tipi-ges", "Arazi Tipi GES", 82, 84, gallery_keys=("arazi-tipi-ges",), metrics=(("300 kWp", "kurulu güç"),)),
            topic("sarj-uniteleri", "Elektrikli Araç Şarj Üniteleri", 86, 90, gallery_keys=("sarj-uniteleri",), metrics=(("2 AC", "mevcut istasyon"), ("2 DC", "hızlı şarj istasyonu"), ("11", "planlanan lokasyon"), ("17", "planlanan şarj ünitesi"), ("10 yıl", "işletme süresi"))),
            topic("aydinlatma-donusumu", "Enerji Tasarrufu ve Aydınlatma Dönüşümü", 92, 95, gallery_keys=("aydinlatma-donusumu",), metrics=(("%40+", "enerji tasarrufu"), ("50.167 kWh", "yıllık daha az tüketim"), ("176.000 TL", "tasarruf"), ("1.020", "ağaç eşdeğeri"), ("21 ton", "yıllık önlenen CO₂e"))),
            topic("uluslararasi-uyelikler", "Uluslararası Üyeliklerimiz", 97, 99),
            topic("kardes-sehirler", "Kardeş Şehirlerimiz", 101, 102, metrics=(("12", "ülke"), ("18", "kardeş şehir"))),
            topic("energy-cities", "Avrupa Enerji Kentleri Ağı Üyeliği (ENERGY CITIES)", 104, 105, metrics=(("30+", "ülke"), ("1.000+", "yerel yönetim"), ("11", "yönetim kurulundaki ülke"))),
        ],
    },
    {
        "id": "dayanikli-sehirler",
        "title": "Dayanıklı Şehirler ve Yapılı Çevre",
        "accent": "#F5A313",
        "accentSoft": "#FEEAAB",
        "accentInk": "#062D3C",
        "homeImage": "assets/gallery/dijital-ikiz-02.webp?v=20261104d",
        "homePosition": "52% 50%",
        "icon": "resilience",
        "topics": [
            topic("dijital-ikiz", "Dijital İkiz", 110, 113, gallery_keys=("dijital-ikiz",), metrics=(("3B", "kent modelleme"), ("Yapay zekâ", "karar desteği"), ("IoT", "canlı veri entegrasyonu"))),
            topic("borneye", "Born-Eye", 115, 118, gallery_keys=("borneye",), metrics=(("VCA", "video analitiği"), ("Anlık", "yol kusuru tespiti"))),
            topic("yoma", "Yoma (Yangın Olaylarına Müdahale Aracı)", 120, 121, gallery_keys=("yoma",), metrics=(("3", "modernize su tankeri"), ("360°", "hareket kabiliyeti"), ("25 m", "önceki menzil"), ("70–80 m", "yeni püskürtme menzili"))),
            topic("bak", "Bornova Belediyesi Arama Kurtarma Ekibi (BAK)", 122, 124, gallery_keys=("bak",), metrics=(("2025", "ekibin kuruluş yılı"), ("AFAD", "hafif seviye akreditasyon"))),
            topic("tulpar", "Bornova Acil Durum Erken Uyarı ve Müdahale Sistemi / TULPAR", 126, 131, lead=127, metrics=(("NASA", "uydu verileri"), ("FWI", "yangın hava indeksi"), ("Telegram + SMS", "anlık uyarı"))),
            topic("ust-ortu", "Üst Örtü Projesi", 132, 133, gallery_keys=("ust-ortu",), metrics=(("Atıl ipler", "yeniden kullanım"), ("Büyükpark", "ilk uygulama"))),
        ],
    },
    {
        "id": "insani-sosyal-kalkinma",
        "title": "İnsani ve Sosyal Kalkınma",
        "accent": "#791718",
        "accentSoft": "#921533",
        "accentInk": "#FFFFFF",
        "homeImage": "assets/gallery/gulsah-durbay-genclik-merkezi-04.webp?v=20261104c",
        "homePosition": "22% 45%",
        "icon": "community",
        "topics": [
            topic("gulsah-durbay-genclik-merkezi", "Gülşah Durbay Gençlik Merkezi", 137, 148, lead=138, link=(148, "https://gdgm.bornova.bel.tr"), gallery_keys=("gulsah-durbay-genclik-merkezi",), metrics=(("1.620", "üniversiteli"),)),
            topic("kent-marketler", "Kent Marketler", 150, 154, lead=151, metrics=(("7", "hizmet noktası"), ("3.910", "desteklenen hane"))),
            topic("kent-lokantalari", "Kent Lokantaları", 155, 159, metrics=(("3", "Kent Lokantası"), ("5.000", "haftalık sunulan yemek"))),
            topic("sicak-yemek-destegi", "Sıcak Yemek Desteği", 160, 164, metrics=(("65+", "desteklenen yaş grubu"), ("12K", "ulaştırılan sıcak öğün"))),
            topic("kent-kasap", "Kent Kasap", 165, 168, metrics=(("1.000", "emekli aile"),)),
            topic("beslenme-paketi", "Miniklere Beslenme Paketi Desteği", 170, 172, metrics=(("7.5K", "sağlıklı kahvaltı öğünü"),)),
            topic("belgem", "BELGEM / Ücretsiz Dershane", 173, 178, metrics=(("4", "BELGEM merkezi"), ("2.5K", "öğrenci"))),
            topic("oyuncak-kutuphanesi", "Oyuncak Kütüphanesi", 179, 181, metrics=(("3.000", "toplanan oyuncak"),)),
            topic("altin-bilezik", "Altın Bilezik İstihdam Merkezi", 182, 189, link=(189, "https://www.altinbilezikbornova.com"), gallery_keys=("altin-bilezik",), metrics=(("110", "toplu iş görüşmesi"), ("~1.000", "iş ilanı"), ("714", "istihdam"), ("77 + 7", "firma ve STK"), ("3 gün", "istihdam fuarı"))),
            topic("cocuk-oyun-aktivite", "Çocuk Oyun ve Aktivite Merkezleri", 190, 192, metrics=(("10", "farklı merkez"), ("1.731", "çocuk"))),
            topic("danismanlik-destek", "Danışmanlık ve Destek Programları", 193, 195, metrics=(("2.9K", "danışmanlık alan vatandaş"),)),
            topic("adli-yardim", "Adli Yardım Desteği", 196, 198, metrics=(("108", "adli yardım alan kişi"),)),
            topic("hos-geldin-bebek", "Hoş Geldin Bebek Paketi", 199, 201, metrics=(("2K", "paket desteği alan bebek"),)),
            topic("kadin-cocuk-egitim-atolye", "Kadınlar ve Çocuklara Yönelik Eğitim ve Atölyeler", 202, 205, metrics=(("225", "eğitim, atölye ve etkinlik"), ("17K", "katılımcı"))),
            topic("mutfak-atolyesi", "Mutfak Atölyesi", 208, 216, gallery_keys=("mutfak-atolyesi",), metrics=(("30", "farklı workshop"), ("2.5K", "pratik eğitim alan kişi"))),
            topic("hobi-beceri-kurslari", "Hobi ve Beceri Edindirme Kursları", 217, 222, gallery_keys=("hobi-beceri-kurslari",), metrics=(("27", "branş"), ("9.5K", "vatandaş"))),
            topic("bornova-miras", "Bornova Miras", 223, 225, link=(225, "https://bornovamiras.com"), gallery_keys=("bornova-miras",), metrics=(("8.500 yıl", "Bornova’nın tarihi"),)),
            topic("kultur-rotalari", "Kültür Rotaları", 227, 231, gallery_keys=("kultur-rotalari",), metrics=(("18 nokta", "uzun rota · yaklaşık 6 saat"), ("15 nokta", "orta rota · yaklaşık 3 saat"), ("10 nokta", "kısa rota · yaklaşık 2 saat"))),
        ],
    },
    {
        "id": "sifir-atik",
        "title": "Sıfır Atık",
        "accent": "#65D7D1",
        "accentSoft": "#65D7D1",
        "accentInk": "#062D3C",
        "homeImage": "assets/gallery/atik-bank-01.webp?v=20261104c",
        "homePosition": "50% 50%",
        "icon": "recycle",
        "topics": [
            topic("atik-bank", "Atık Bank", 234, 239, gallery_keys=("atik-bank",), metrics=(("4.267 kg", "ambalaj atığı"), ("1.077 lt", "bitkisel atık yağ"))),
            topic("kompost-uretimi", "Kompost Üretimi", 240, 243, gallery_keys=("kompost-uretimi",), metrics=(("6765 kg", "yıllık katı gübre"), ("565 lt", "yıllık sıvı gübre"))),
            topic("sifir-atik-belgesi", "Sıfır Atık Belgesi", 245, 247),
            topic("atik-toplayicilari-entegrasyonu", "Bağımsız Sıfır Atık Toplayıcılarının Atık Yönetim Sistemine Entegrasyonu", 248, 249, metrics=(("250 ton", "yeniden ekonomiye kazandırılan ambalaj atığı"),)),
            topic("atik-getirme-merkezi", "Atık Getirme Merkezi ve Atıktan Sanata Atölyesi", 251, 258, metrics=(("1. Sınıf", "Atık Getirme Merkezi"),)),
            topic("depozito-yonetim-sistemi", "Depozito Yönetim Sistemi", 259, 261, metrics=(("6 ay", "kurulum süresi"), ("6", "Depozito İade Makinesi"))),
            topic("tambur-kompost", "Tambur Kompost Projesi", 262, 264, metrics=(("6 ton", "üretilen kompost"), ("20 ton", "hedeflenen üretim"))),
            topic("atik-yonetimi-egitimleri", "İklim Değişikliği ve Atık Yönetimi Eğitimleri", 265, 267, metrics=(("1.369", "eğitimlerle ulaşılan kişi"),)),
            topic("bireysel-karbon-ayak-izi", "Bireysel Karbon Ayak İzi", 268, 271, metrics=(("320", "bireysel ölçüm"), ("7.166 kg CO₂e", "Bornova kişi başı yıllık"), ("4.494 kg CO₂e", "Türkiye ortalaması"), ("%44", "Türkiye ortalamasının üzerinde"), ("8.500 kg CO₂e", "İzmir ortalaması"))),
            topic("belkahve", "BELKAHVE İnşaat Metal Geri Dönüşüm Ticaret ve Sanayi A.Ş.", 272, 276, lead=273),
            topic("akilli-bank", "Akıllı Bank", 278, 279, metrics=(("Med-Point", "Akıllı Kent Bankı"), ("Ücretsiz", "temel sağlık ölçümü"))),
        ],
    },
]


def topic_v2(
    item_id,
    title,
    *,
    lead=False,
    link=None,
    gallery_keys=(),
    metrics=(),
):
    return {
        "id": item_id,
        "title": title,
        "lead": lead,
        "link": link,
        "galleryKeys": list(gallery_keys),
        "metrics": [list(metric) for metric in metrics],
    }


# The order below mirrors the approved DOCX. Paragraph boundaries are resolved
# from its numbered headings so later copy edits do not require fragile indexes.
CATEGORIES = [
    {
        "id": "gida-tarim-saglik",
        "title": "Gıda, Tarım ve Sağlık",
        "accent": "#85A283",
        "accentSoft": "#85A283",
        "accentInk": "#062D3C",
        "homeImage": "assets/gallery/dayanisma-tarlasi-02.webp?v=20261104c",
        "homePosition": "50% 50%",
        "icon": "sprout",
        "topics": [
            topic_v2("kent-bostani", "Kent Bostanı", lead=True, gallery_keys=("kent-bostani",), metrics=(("9", "kent bostanı"), ("1.2K", "üretim yapan kadın"))),
            topic_v2("ekolojik-kent-yerel-tohum-merkezi", "Ekolojik Kent Yerel Tohum Merkezi", gallery_keys=("ekolojik-kent-yerel-tohum-merkezi",), metrics=(("193K", "dağıtılan tohum"), ("1K", "sergilenen tohum"), ("1.808K", "fide dağıtımı"), ("250+", "korunan yerel tohum çeşidi"))),
            topic_v2("dayanisma-tarlasi", "Dayanışma Tarlası", lead=True, gallery_keys=("dayanisma-tarlasi",), metrics=(("15 dönüm", "üretim alanı"), ("86 ton", "vatandaşa ulaşan sebze"))),
            topic_v2("biyocesitlilik-envanteri", "Biyoçeşitlilik Envanteri", lead=True, gallery_keys=("biyocesitlilik-envanteri",), metrics=(("519", "toplam kayıtlı tür"), ("433", "bitki türü"), ("41", "kuş türü"), ("23", "sürüngen türü"), ("22", "memeli türü"))),
            topic_v2("tarimsal-egitimler", "Tarımsal Eğitimler", metrics=(("14K", "çocuklara ekolojik eğitim"), ("8.5K", "üreticiye tarımsal eğitim"), ("2.2K", "kadına sağlıklı gıda atölyesi"))),
            topic_v2("aricilik-faaliyetleri", "Arıcılık Faaliyetleri", metrics=(("320", "yeni arıcı"), ("440 kg", "paylaşılan bal"))),
            topic_v2("cografi-isaretli-urunler", "Coğrafi İşaretli Ürünler", lead=True, metrics=(("2", "tescilli yerel ürün"), ("1", "başvuru sürecindeki değer"))),
        ],
    },
    {
        "id": "enerji-ulastirma",
        "title": "Enerji ve Ulaştırma",
        "accent": "#72A4C9",
        "accentSoft": "#AEC4D2",
        "accentInk": "#062D3C",
        "homeImage": "assets/gallery/hibrit-direkler-09.webp?v=20261104c",
        "homePosition": "50% 50%",
        "icon": "energy",
        "topics": [
            topic_v2("hibrit-direkler", "Hibrit Direkler", gallery_keys=("hibrit-direkler",), metrics=(("6 kW", "günlük maksimum üretim"), ("%40", "Abide-i Hürriyet Parkı enerjisi"), ("650 Wh", "11 m/s rüzgârda üretim"), ("950 Wh", "güneş panelleri"))),
            topic_v2("cati-ges", "Yenilenebilir Enerji Üretimi (Çatı GES)", gallery_keys=("cati-ges",), metrics=(("3", "uygulama noktası"), ("362 kWp", "toplam kurulu güç"))),
            topic_v2("arazi-tipi-ges", "Arazi Tipi GES", gallery_keys=("arazi-tipi-ges",), metrics=(("300 kWp", "kurulu güç"),)),
            topic_v2("elektrikli-arac-kullanimi", "Elektrikli Araç Kullanımı", gallery_keys=("elektrikli-arac-kullanimi",), metrics=(("2", "17 kişilik elektrikli minibüs"), ("3", "elektrikli binek araç"), ("1.500 km", "aylık ortalama yol"), ("8.640 kg", "yıllık önlenen CO₂e"))),
            topic_v2("sarj-uniteleri", "Elektrikli Araç Şarj Üniteleri", gallery_keys=("sarj-uniteleri",), metrics=(("2 AC", "mevcut istasyon"), ("2 DC", "hızlı şarj istasyonu"), ("11", "planlanan lokasyon"), ("17", "planlanan şarj ünitesi"), ("10 yıl", "işletme süresi"))),
            topic_v2("aydinlatma-donusumu", "Enerji Tasarrufu ve Aydınlatma Dönüşümü", gallery_keys=("aydinlatma-donusumu",), metrics=(("%40+", "enerji tasarrufu"), ("50.167 kWh", "yıllık daha az tüketim"), ("176.000 TL", "tasarruf"), ("1.020", "ağaç eşdeğeri"), ("21 ton", "yıllık önlenen CO₂e"))),
            topic_v2("akilli-sulama-sistemi", "Abide-i Hürriyet Parkı Akıllı Sulama Sistemi", gallery_keys=("akilli-sulama-sistemi",), metrics=(("Dijital İkiz", "uzaktan kontrol"), ("Nem sensörleri", "ihtiyaca göre sulama"))),
            topic_v2("uluslararasi-uyelikler", "Uluslararası Üyeliklerimiz"),
            topic_v2("kardes-sehirler", "Kardeş Şehirlerimiz", metrics=(("12", "ülke"), ("18", "kardeş şehir"))),
            topic_v2("energy-cities", "Avrupa Enerji Kentleri Ağı Üyeliği (ENERGY CITIES)", metrics=(("30+", "ülke"), ("1.000+", "yerel yönetim"), ("11", "yönetim kurulundaki ülke"))),
        ],
    },
    {
        "id": "dayanikli-sehirler",
        "title": "Dayanıklı Şehirler ve Yapılı Çevre",
        "accent": "#F5A313",
        "accentSoft": "#FEEAAB",
        "accentInk": "#062D3C",
        "homeImage": "assets/gallery/dijital-ikiz-02.webp?v=20261104d",
        "homePosition": "52% 50%",
        "icon": "resilience",
        "topics": [
            topic_v2("dijital-ikiz", "Dijital İkiz", gallery_keys=("dijital-ikiz",), metrics=(("3B", "kent modelleme"), ("Yapay zekâ", "karar desteği"), ("IoT", "canlı veri entegrasyonu"))),
            topic_v2("borneye", "Born-Eye", gallery_keys=("borneye",), metrics=(("VCA", "video analitiği"), ("Anlık", "yol kusuru tespiti"))),
            topic_v2("yoma", "Yoma (Yangın Olaylarına Müdahale Aracı)", gallery_keys=("yoma",), metrics=(("3", "modernize su tankeri"), ("360°", "hareket kabiliyeti"), ("25 m", "önceki menzil"), ("70–80 m", "yeni püskürtme menzili"))),
            topic_v2("bak", "Bornova Belediyesi Arama Kurtarma Ekibi (BAK)", gallery_keys=("bak",), metrics=(("2025", "ekibin kuruluş yılı"), ("AFAD", "hafif seviye akreditasyon"))),
            topic_v2("tulpar", "Bornova Acil Durum Erken Uyarı ve Müdahale Sistemi / TULPAR", lead=True, metrics=(("NASA", "uydu verileri"), ("FWI", "yangın hava indeksi"), ("Telegram + SMS", "anlık uyarı"))),
            topic_v2("akilli-bank", "Akıllı Bank", metrics=(("Med-Point", "Akıllı Kent Bankı"), ("Ücretsiz", "temel sağlık ölçümü"))),
            topic_v2("ust-ortu", "Üst Örtü Projesi", gallery_keys=("ust-ortu",), metrics=(("Atıl ipler", "yeniden kullanım"), ("Büyükpark", "ilk uygulama"))),
        ],
    },
    {
        "id": "insani-sosyal-kalkinma",
        "title": "İnsani ve Sosyal Kalkınma",
        "accent": "#791718",
        "accentSoft": "#921533",
        "accentInk": "#FFFFFF",
        "homeImage": "assets/gallery/gulsah-durbay-genclik-merkezi-04.webp?v=20261104c",
        "homePosition": "22% 45%",
        "icon": "community",
        "topics": [
            topic_v2("bornova-miras", "Bornova Miras", link=("bornovamiras.com", "https://bornovamiras.com"), gallery_keys=("bornova-miras",), metrics=(("8.500 yıl", "Bornova’nın tarihi"),)),
            topic_v2("gulsah-durbay-genclik-merkezi", "Gülşah Durbay Gençlik Merkezi", lead=True, link=("gdgm.bornova.bel.tr", "https://gdgm.bornova.bel.tr"), gallery_keys=("gulsah-durbay-genclik-merkezi",), metrics=(("1.620", "üniversiteli"),)),
            topic_v2("belgem", "BELGEM / Ücretsiz Dershane", metrics=(("4", "BELGEM merkezi"), ("2.5K", "öğrenci"))),
            topic_v2("kent-marketler", "Kent Marketler", lead=True, metrics=(("7", "hizmet noktası"), ("3.910", "desteklenen hane"))),
            topic_v2("kent-lokantalari", "Kent Lokantaları", metrics=(("3", "Kent Lokantası"), ("5.000", "haftalık sunulan yemek"))),
            topic_v2("sicak-yemek-destegi", "Sıcak Yemek Desteği", metrics=(("65+", "desteklenen yaş grubu"), ("12K", "ulaştırılan sıcak öğün"))),
            topic_v2("kent-kasap", "Kent Kasap", metrics=(("1.000", "emekli aile"),)),
            topic_v2("beslenme-paketi", "Miniklere Beslenme Paketi Desteği", metrics=(("7.5K", "sağlıklı kahvaltı öğünü"),)),
            topic_v2("oyuncak-kutuphanesi", "Oyuncak Kütüphanesi", metrics=(("3.000", "toplanan oyuncak"),)),
            topic_v2("altin-bilezik", "Altın Bilezik İstihdam Merkezi", link=("altinbilezikbornova.com", "https://www.altinbilezikbornova.com"), gallery_keys=("altin-bilezik",), metrics=(("110", "toplu iş görüşmesi"), ("~1.000", "iş ilanı"), ("714", "istihdam"), ("77 + 7", "firma ve STK"), ("3 gün", "istihdam fuarı"))),
            topic_v2("cocuk-oyun-aktivite", "Çocuk Oyun ve Aktivite Merkezleri", metrics=(("10", "farklı merkez"), ("1.7K", "çocuk"))),
            topic_v2("danismanlik-destek", "Danışmanlık ve Destek Programları", metrics=(("2.9K", "danışmanlık alan vatandaş"),)),
            topic_v2("adli-yardim", "Adli Yardım Desteği", metrics=(("108", "adli yardım alan kişi"),)),
            topic_v2("hos-geldin-bebek", "Hoş Geldin Bebek Paketi", metrics=(("2K", "paket desteği alan bebek"),)),
            topic_v2("kadin-cocuk-egitim-atolye", "Kadınlar ve Çocuklara Yönelik Eğitim ve Atölyeler", metrics=(("225", "eğitim, atölye ve etkinlik"), ("17K", "katılımcı"))),
            topic_v2("mutfak-atolyesi", "Mutfak Atölyesi", gallery_keys=("mutfak-atolyesi",), metrics=(("30", "farklı workshop"), ("2.5K", "pratik eğitim alan kişi"))),
            topic_v2("hobi-beceri-kurslari", "Hobi ve Beceri Edindirme Kursları", gallery_keys=("hobi-beceri-kurslari",), metrics=(("27", "branş"), ("9.5K", "vatandaş"))),
            topic_v2("kultur-rotalari", "Kültür Rotaları", gallery_keys=("kultur-rotalari",), metrics=(("18 nokta", "uzun rota · yaklaşık 6 saat"), ("15 nokta", "orta rota · yaklaşık 3 saat"), ("10 nokta", "kısa rota · yaklaşık 2 saat"))),
        ],
    },
    {
        "id": "sifir-atik",
        "title": "Sıfır Atık",
        "accent": "#65D7D1",
        "accentSoft": "#65D7D1",
        "accentInk": "#062D3C",
        "homeImage": "assets/gallery/atik-bank-01.webp?v=20261104c",
        "homePosition": "50% 50%",
        "icon": "recycle",
        "topics": [
            topic_v2("belkahve", "BELKAHVE İnşaat Metal Geri Dönüşüm Ticaret ve Sanayi A.Ş.", lead=True),
            topic_v2("atik-bank", "Atık Bank", gallery_keys=("atik-bank",), metrics=(("4.267 kg", "ambalaj atığı"), ("1.077 lt", "bitkisel atık yağ"))),
            topic_v2("depozito-yonetim-sistemi", "Depozito Yönetim Sistemi", metrics=(("6 ay", "kurulum süresi"), ("6", "Depozito İade Makinesi"))),
            topic_v2("atik-toplayicilari-entegrasyonu", "Bağımsız Sıfır Atık Toplayıcılarının Atık Yönetim Sistemine Entegrasyonu", metrics=(("250 ton", "yeniden ekonomiye kazandırılan ambalaj atığı"),)),
            topic_v2("atik-getirme-merkezi", "Atık Getirme Merkezi ve Atıktan Sanata Atölyesi", metrics=(("1. Sınıf", "Atık Getirme Merkezi"),)),
            topic_v2("kompost-uretimi", "Kompost Üretimi", gallery_keys=("kompost-uretimi",), metrics=(("6765 kg", "yıllık katı gübre"), ("565 lt", "yıllık sıvı gübre"))),
            topic_v2("tambur-kompost", "Tambur Kompost Projesi", metrics=(("6 ton", "üretilen kompost"), ("20 ton", "hedeflenen üretim"))),
            topic_v2("bireysel-karbon-ayak-izi", "Bireysel Karbon Ayak İzi", metrics=(("320", "bireysel ölçüm"), ("7.1K kg CO₂e", "Bornova kişi başı yıllık"), ("4.5K kg CO₂e", "Türkiye ortalaması"), ("%44", "Türkiye ortalamasının üzerinde"), ("8.5K kg CO₂e", "İzmir ortalaması"))),
            topic_v2("atik-yonetimi-egitimleri", "İklim Değişikliği ve Atık Yönetimi Eğitimleri", metrics=(("1.4K", "eğitimlerle ulaşılan kişi"),)),
            topic_v2("sifir-atik-belgesi", "Sıfır Atık Belgesi"),
        ],
    },
]


def qn(namespace, name):
    return f"{{{namespace}}}{name}"


def on_off(rpr, name):
    if rpr is None:
        return False
    element = rpr.find(f"w:{name}", NS)
    if element is None:
        return False
    value = element.get(qn(W, "val"))
    return value not in {"0", "false", "off", "none"}


def run_text(run):
    parts = []
    for node in run.iter():
        if node.tag == qn(W, "t"):
            parts.append(node.text or "")
        elif node.tag == qn(W, "tab"):
            parts.append("\t")
        elif node.tag in {qn(W, "br"), qn(W, "cr")}:
            parts.append("\n")
    return "".join(parts)


def extract_runs(paragraph, relationships):
    runs = []

    def visit(container, href=None):
        for child in list(container):
            if child.tag == qn(W, "r"):
                text = run_text(child)
                if not text:
                    continue
                rpr = child.find("w:rPr", NS)
                run = {"text": text}
                if on_off(rpr, "b") or on_off(rpr, "bCs"):
                    run["bold"] = True
                if on_off(rpr, "i") or on_off(rpr, "iCs"):
                    run["italic"] = True
                if on_off(rpr, "u"):
                    run["underline"] = True
                if href:
                    run["href"] = href
                runs.append(run)
            elif child.tag == qn(W, "hyperlink"):
                visit(child, relationships.get(child.get(qn(R, "id"))))
            elif child.tag in {qn(W, "ins"), qn(W, "smartTag"), qn(W, "sdt")}:
                visit(child, href)

    visit(paragraph)
    return trim_runs(runs)


def trim_runs(runs):
    runs = [dict(run) for run in runs if run.get("text")]
    while runs and not runs[0]["text"].strip():
        runs.pop(0)
    while runs and not runs[-1]["text"].strip():
        runs.pop()
    if not runs:
        return []
    runs[0]["text"] = runs[0]["text"].lstrip()
    runs[-1]["text"] = runs[-1]["text"].rstrip()
    runs = [run for run in runs if run["text"]]
    merged = []
    for run in runs:
        formatting = {key: value for key, value in run.items() if key != "text"}
        if merged and {key: value for key, value in merged[-1].items() if key != "text"} == formatting:
            merged[-1]["text"] += run["text"]
        else:
            merged.append(run)
    return merged


def paragraph_text(record):
    return "".join(run["text"] for run in record["runs"]).strip()


def load_records(source_path):
    with zipfile.ZipFile(source_path) as archive:
        document = ET.fromstring(archive.read("word/document.xml"))
        rels_root = ET.fromstring(archive.read("word/_rels/document.xml.rels"))

    relationships = {
        rel.get("Id"): rel.get("Target")
        for rel in rels_root.findall(f"{{{PKG_REL}}}Relationship")
        if rel.get("Type", "").endswith("/hyperlink")
    }

    records = {}
    body = document.find("w:body", NS)
    for index, paragraph in enumerate(body.findall("w:p", NS), start=1):
        ppr = paragraph.find("w:pPr", NS)
        num_id = None
        alignment = None
        if ppr is not None:
            numpr = ppr.find("w:numPr", NS)
            if numpr is not None:
                numid_node = numpr.find("w:numId", NS)
                if numid_node is not None:
                    num_id = numid_node.get(qn(W, "val"))
            alignment_node = ppr.find("w:jc", NS)
            if alignment_node is not None:
                alignment_value = alignment_node.get(qn(W, "val"))
                alignment = {
                    "both": "justify",
                    "distribute": "justify",
                    "center": "center",
                    "right": "right",
                    "left": "left",
                }.get(alignment_value)
        records[index] = {
            "runs": extract_runs(paragraph, relationships),
            "isList": num_id is not None,
            "align": alignment,
        }
    return records


def remove_leading_hyphen(runs):
    runs = [dict(run) for run in runs]
    if runs:
        runs[0]["text"] = runs[0]["text"].lstrip()
        if runs[0]["text"].startswith("-"):
            runs[0]["text"] = runs[0]["text"][1:].lstrip()
    return [run for run in runs if run["text"]]


def numbered_heading_label(text):
    match = re.match(r"^\s*\d+\s*-\s*(.*?)\s*$", text)
    return match.group(1) if match else None


def normalized_heading(text):
    normalized = " ".join(text.replace("–", "-").replace("—", "-").split()).casefold()
    normalized = normalized.replace("ı", "i")
    return "".join(
        character
        for character in unicodedata.normalize("NFKD", normalized)
        if not unicodedata.combining(character)
    )


def find_heading(records, title, start, end):
    expected = normalized_heading(title)
    for index in range(start, end + 1):
        label = numbered_heading_label(paragraph_text(records[index]))
        if label and normalized_heading(label) == expected:
            return index
    raise ValueError(f"Heading not found in DOCX: {title}")


def first_content_index(records, start, end):
    for index in range(start, end + 1):
        if paragraph_text(records[index]):
            return index
    return None


def find_text_index(records, text, start, end):
    expected = normalized_heading(text)
    for index in range(start, end + 1):
        if normalized_heading(paragraph_text(records[index])) == expected:
            return index
    raise ValueError(f"Link label not found in DOCX: {text}")


def build_blocks(records, start, end, *, lead_index=None, link_index=None):
    skip = {start}
    if lead_index:
        skip.add(lead_index)
    if link_index:
        skip.add(link_index)

    blocks = []
    for index in range(start + 1, end + 1):
        if index in skip:
            continue
        record = records.get(index, {"runs": [], "isList": False, "align": None})
        runs = record["runs"]
        text = paragraph_text(record)
        if not text:
            continue

        is_list = record["isList"] or text.startswith("-")
        if is_list:
            list_runs = remove_leading_hyphen(runs)
            if blocks and blocks[-1]["type"] == "list" and blocks[-1].get("align") == record.get("align"):
                blocks[-1]["items"].append(list_runs)
            else:
                block = {"type": "list", "items": [list_runs]}
                if record.get("align"):
                    block["align"] = record["align"]
                blocks.append(block)
        else:
            block = {"type": "paragraph", "runs": runs}
            if record.get("align"):
                block["align"] = record["align"]
            blocks.append(block)
    return blocks


def block_text(block):
    if block.get("type") == "list":
        return " ".join(
            "".join(run.get("text", "") for run in item)
            for item in block.get("items", [])
        ).strip()
    return "".join(run.get("text", "") for run in block.get("runs", [])).strip()


def build_content(records):
    record_end = max(records)
    category_positions = []
    cursor = 1
    for category_config in CATEGORIES:
        category_index = find_heading(records, category_config["title"], cursor, record_end)
        category_positions.append(category_index)
        cursor = category_index + 1

    categories = []
    for category_offset, category_config in enumerate(CATEGORIES):
        category_start = category_positions[category_offset]
        category_end = (
            category_positions[category_offset + 1] - 1
            if category_offset + 1 < len(category_positions)
            else record_end
        )
        category = {
            key: value
            for key, value in category_config.items()
            if key != "topics"
        }
        topic_positions = []
        cursor = category_start + 1
        for config in category_config["topics"]:
            topic_index = find_heading(records, config["title"], cursor, category_end)
            topic_positions.append(topic_index)
            cursor = topic_index + 1

        items = []
        for topic_offset, config in enumerate(category_config["topics"]):
            topic_start = topic_positions[topic_offset]
            topic_end = (
                topic_positions[topic_offset + 1] - 1
                if topic_offset + 1 < len(topic_positions)
                else category_end
            )
            lead_index = (
                first_content_index(records, topic_start + 1, topic_end)
                if config.get("lead")
                else None
            )
            link_index = None
            if config.get("link"):
                link_label, _ = config["link"]
                link_index = find_text_index(records, link_label, topic_start + 1, topic_end)
            lead = paragraph_text(records[lead_index]) if lead_index else ""
            item = {
                "id": config["id"],
                "title": config["title"],
                "image": None,
                "alt": f"{config['title']} çalışmasına ait görsel",
                "lead": lead,
                "blocks": build_blocks(
                    records,
                    topic_start,
                    topic_end,
                    lead_index=lead_index,
                    link_index=link_index,
                ),
                "metrics": config["metrics"],
            }
            if lead_index and records[lead_index].get("align"):
                item["leadAlign"] = records[lead_index]["align"]
            item["galleryKeys"] = config["galleryKeys"] or [config["id"]]
            if config.get("link"):
                link_label, url = config["link"]
                item["link"] = {
                    "label": link_label,
                    "url": url,
                }
            items.append(item)
        category["items"] = items
        categories.append(category)

    # The final lighting-result paragraph follows the smart-irrigation copy in
    # the approved document, but belongs to the lighting transformation topic.
    energy_items = {item["id"]: item for item in categories[1]["items"]}
    irrigation_blocks = energy_items["akilli-sulama-sistemi"]["blocks"]
    moved_blocks = [
        block
        for block in irrigation_blocks
        if block_text(block).startswith("Bu dönüşümle birlikte %40")
    ]
    energy_items["akilli-sulama-sistemi"]["blocks"] = [
        block for block in irrigation_blocks if block not in moved_blocks
    ]
    energy_items["aydinlatma-donusumu"]["blocks"].extend(moved_blocks)
    return categories


def validate_content(content):
    expected_counts = [7, 10, 7, 18, 10]
    actual_counts = [len(category["items"]) for category in content]
    if actual_counts != expected_counts:
        raise ValueError(f"Unexpected topic counts: {actual_counts}")

    item_ids = [
        f"{category['id']}/{item['id']}"
        for category in content
        for item in category["items"]
    ]
    if len(item_ids) != len(set(item_ids)):
        raise ValueError("Duplicate topic IDs found")

    for category in content:
        for item in category["items"]:
            if not item["blocks"]:
                raise ValueError(f"Topic has no body blocks: {category['id']}/{item['id']}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    records = load_records(args.source)
    content = build_content(records)
    validate_content(content)

    payload = json.dumps(content, ensure_ascii=False, indent=2)
    output = (
        "// Generated from the approved COP31 DOCX source.\n"
        "// Run scripts/import_docx_content.py to refresh wording and rich formatting.\n"
        f"window.COP31_CONTENT = {payload};\n"
    )
    args.out.write_text(output, encoding="utf-8")


if __name__ == "__main__":
    main()
