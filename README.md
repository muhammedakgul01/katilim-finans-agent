# Katılım Finans Agent

Katılım Finans Agent, katılım bankalarının finansman kampanyalarını analiz etmek amacıyla geliştirilen yapay zekâ destekli bir prototiptir.

Proje kapsamında banka web sayfalarından kampanya içerikleri alınmakta, kampanya metinlerinden önemli bilgiler çıkarılmakta, standartlaştırılmakta ve analiz edilmektedir.

> Bu proje TEKNOFEST 2026 Yapay Zekâ Yarışması ön değerlendirme prototipi olarak geliştirilmektedir.

---

# Proje Amacı

Katılım bankalarının finansman kampanyaları farklı biçimlerde yayınlanmaktadır.

Bu proje;

- kampanya metinlerini otomatik olarak okumayı,
- ürün bilgilerini çıkarmayı,
- kâr payı ve vade bilgilerini standartlaştırmayı,
- kampanyaları karşılaştırmayı

amaçlamaktadır.

---

# Sistem Mimarisi

```
Banka Web Sayfası
        │
        ▼
   scraper.py
        │
        ▼
BeautifulSoup
        │
        ▼
 Temiz Metin
        │
        ▼
 extractor.py
        │
        ▼
 normalizer.py
        │
        ▼
 campaign.json
        │
        ▼
 campaigns.csv
        │
        ▼
 analyzer.py
```

---

# Proje Yapısı

```
katilim-finans-agent/

├── src/
│   ├── main.py
│   ├── extractor.py
│   ├── normalizer.py
│   ├── analyzer.py
│   └── scraper.py
│
├── data/
│   ├── campaign.json
│   └── campaigns.csv
│
├── docs/
│
├── sandbox/
│
├── tests/
│
├── requirements.txt
│
└── README.md
```

---

# Kullanılan Teknolojiler

- Python 3.13
- Regular Expressions (Regex)
- JSON
- Requests
- BeautifulSoup4
- Pandas
- Git
- GitHub

---

# Çalışma Akışı

1. Banka web sayfası alınır.
2. HTML içeriği çekilir.
3. HTML temiz metne dönüştürülür.
4. Kampanya bilgileri Regex ile çıkarılır.
5. Veriler normalize edilir.
6. JSON çıktısı oluşturulur.
7. Kampanyalar CSV üzerinde analiz edilir.

---

# Mevcut Özellikler

- Web sayfası çekme
- HTML temizleme
- Kâr payı çıkarma
- Vade çıkarma
- Ürün tespiti
- Hedef kitle tespiti
- Veri standardizasyonu
- JSON çıktısı oluşturma
- Kampanya karşılaştırma analizi

---

# Kurulum

Projeyi klonlayın.

```bash
git clone <repo-url>
```

Proje klasörüne girin.

```bash
cd katilim-finans-agent
```

Gerekli paketleri yükleyin.

```bash
pip install -r requirements.txt
```

Projeyi çalıştırın.

```bash
python src/main.py
```

---

# Örnek JSON Çıktısı

```json
{
    "banka": "",
    "urun": "Konut Finansmanı",
    "kar_payi": 2.05,
    "vade": 36,
    "hedef": "Yeni Müşteri"
}
```

---

# Geliştirme Durumu

✅ Regex tabanlı bilgi çıkarımı

✅ Veri standardizasyonu

✅ JSON çıktısı

✅ CSV analizi

✅ Web sayfası çekme

✅ HTML temizleme

🚧 Gerçek zamanlı çoklu banka entegrasyonu

🚧 Gelişmiş kampanya karşılaştırmaları

---

# Takım

TEKNOFEST 2026 Yapay Zekâ Yarışması kapsamında geliştirilmektedir.