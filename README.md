# influvia-site

Influvia uygulamasının tanıtım sitesi (statik). GitHub Pages ile yayınlanır.

- `build.py` — tüm sayfaları üretir (`python build.py`). Kaynak metinler `content/` altında.
- Çıktılar: `index.html`, `gizlilik/`, `hesap-silme/`, `kullanim-kosullari/`, `destek/`, `404.html`.
- Alan adı değişince `build.py` içindeki `DOMAIN` güncellenir ve `CNAME` dosyası eklenir.
