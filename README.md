# Bornova COP31 İklim Eylemleri

Bornova Belediyesi'nin COP31 standında yatay dokunmatik kiosk ekranında kullanılmak üzere hazırlanmış, bağımlılıksız statik web sitesi.

## Yapı

- `dist/index.html`: kiosk arayüzü
- `dist/content.js`: 5 ana başlık ve 52 Türkçe alt konu
- `dist/content-en.js`: Türkçe yapıyla birebir eşleşen 52 İngilizce alt konu
- `dist/app.js`: dokunmatik gezinme, yatay galeri ve tam ekran davranışı
- `dist/gallery-manifest.js`: konu başına tüm fotoğrafların eşleştirmesi
- `dist/assets/gallery/`: web için optimize edilmiş 178 görsel dosyası (güncel Türkçe galeriler ve İngilizce TOGG arşivi)
- `scripts/import_docx_content.py`: onaylı DOCX metnini biçimlendirmeleriyle siteye aktaran araç
- `scripts/import_gallery.py`: klasör yapısından galeriyi yeniden üreten aktarım aracı

## İçerik ve görseller

Metinler belediye tarafından iletilen içerik belgesindeki biçimiyle kullanılır; sayısal değerler ayrıca öne çıkarılır. DOCX aktarımı paragraf sırasını, kalın/italik/altı çizili vurguları, listeleri ve bağlantıları korur. Galeri anahtarları metin sırasından bağımsızdır; böylece yeni bir başlık eklendiğinde mevcut fotoğraflar başka bir konuya kaymaz. Drive klasöründeki fotoğraflar, numara gerektirmeden konu klasörü adlarıyla ilgili alt başlıklara bağlanır. Bir konu klasöründeki tek sayfalık PDF belgeler de ilk sayfaları görsele dönüştürülerek aynı galeride gösterilir. Aktarım doğrudan klasör içindeki dosyaları okur; eski alt klasörler veya sistem dosyaları galeriye karışmaz.

COP31 logosu resmî [Kurumsal Kimlik](https://cop31.tr/tr/kurumsal-kimlik) sayfasından alınmıştır.

## Yerel önizleme

`dist/` klasörünü herhangi bir statik web sunucusuyla açın. Birincil hedef, fuarda kullanılacak 32 inç ONVO 32OVM6500X ekranın 1920×1080 çözünürlüğündeki 16:9 yatay görünümüdür; 1366×768 çözünürlüğü ikincil güvenlik hedefi olarak korunur. Arayüz daha küçük yatay ekranlara ve tabletlere de uyumludur.
