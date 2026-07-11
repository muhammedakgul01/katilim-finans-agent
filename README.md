# Katılım Finans Agent

Katılım Finans Agent, katılım bankalarının finansman kampanyalarını toplamak, yapılandırmak ve karşılaştırmak amacıyla geliştirilen modüler bir ön değerlendirme prototipidir.

Proje, TEKNOFEST 2026 kapsamında hazırlanmıştır.

---

## Proje Amacı

Katılım bankalarının finansman ürünleri farklı web sayfalarında ve farklı metin biçimlerinde yayımlanmaktadır. Bu durum kullanıcıların ürünleri karşılaştırmasını zorlaştırmaktadır.

Bu proje;

- banka web sayfalarından içerik almayı,
- HTML içeriğini okunabilir metne dönüştürmeyi,
- kampanya metinlerinden temel bilgileri çıkarmayı,
- kâr payı ve vade değerlerini standartlaştırmayı,
- kampanyaları karşılaştırmayı

amaçlamaktadır.

---

## Mevcut PoC Kapsamı

Prototipte iki ayrı teknik akış doğrulanmıştır.

### Web verisi alma akışı

```text
Kuveyt Türk Web Sayfası
        │
        ▼
     Requests
        │
        ▼
    scraper.py
        │
        ▼
  BeautifulSoup
        │
        ▼
 Okunabilir Metin
```

Bu akışta gerçek bir banka web sayfasından HTML içeriği alınmakta ve okunabilir metne dönüştürülmektedir.

### Bilgi çıkarımı ve analiz akışı

```text
Örnek Kampanya Metni
        │
        ▼
   extractor.py
        │
        ▼
  normalizer.py
        │
        ▼
   Python Dict
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

Bu akışta örnek kampanya metinlerinden ürün, kâr payı, vade ve hedef kitle bilgileri çıkarılmakta; veriler standartlaştırılarak JSON ve CSV formatlarında işlenmektedir.

> Gerçek web sayfasından alınan temiz metin ile bilgi çıkarımı modüllerinin tam uçtan uca entegrasyonu henüz tamamlanmamıştır. Bu entegrasyon sonraki geliştirme aşaması olarak planlanmaktadır.

---

## Proje Yapısı

```text
katilim-finans-agent/

├── src/
│   ├── main.py
│   ├── scraper.py
│   ├── extractor.py
│   ├── normalizer.py
│   └── analyzer.py
│
├── data/
│   ├── campaign.json
│   └── campaigns.csv
│
├── sandbox/
│   ├── regex_01.py
│   ├── pandas_01.py
│   ├── requests_01.py
│   └── beautifulsoup_01.py
│
├── docs/
├── tests/
├── requirements.txt
├── .gitignore
└── README.md
```

`sandbox/` klasörü, proje geliştirme sürecinde kullanılan deneysel çalışmalar ve kütüphane denemelerini içerir.

---

## Kullanılan Teknolojiler

- Python 3.13
- Regular Expressions
- JSON
- Pandas
- Requests
- BeautifulSoup4
- Git
- GitHub

---

## Modüller

### `scraper.py`

- Web sayfasına HTTP GET isteği gönderir.
- İstek hatalarını yakalar.
- HTML içeriğini okunabilir metne dönüştürür.

### `extractor.py`

Kampanya metninden şu bilgileri çıkarır:

- Kâr payı
- Vade
- Ürün
- Hedef kitle

### `normalizer.py`

Çıkarılan ham değerleri standart biçime dönüştürür.

```text
%2,05 → 2.05
36 ay → 36
```

### `analyzer.py`

CSV verileri üzerinde karşılaştırma yapar.

Mevcut analizler:

- En düşük kâr payına sahip banka
- En uzun vadeye sahip banka

### `main.py`

Modülleri çağırır, JSON çıktısını üretir ve analiz sonuçlarını gösterir.

---

## Kurulum

Projeyi klonlayın:

```bash
git clone https://github.com/muhammedakgul01/katilim-finans-agent.git
```

Proje klasörüne geçin:

```bash
cd katilim-finans-agent
```

Sanal ortam oluşturun:

```bash
python -m venv .venv
```

macOS veya Linux üzerinde sanal ortamı etkinleştirin:

```bash
source .venv/bin/activate
```

Windows üzerinde etkinleştirin:

```powershell
.venv\Scripts\activate
```

Gerekli paketleri yükleyin:

```bash
python -m pip install -r requirements.txt
```

Projeyi çalıştırın:

```bash
python src/main.py
```

---

## Örnek JSON Çıktısı

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

## Örnek Analiz Çıktısı

```text
Kuveyt Türk sayfası başarıyla çekildi.
HTML uzunluğu: ...

Konut Finansmanı metinde var mı?: True

En düşük kâr payı:
{'bank': 'Kuveyt Türk', 'profit_rate': 2.05}

En uzun vade:
{'bank': 'Albaraka Türk', 'term': 48}
```

CSV dosyasındaki değerler prototip amaçlı örnek verilerdir ve güncel banka teklifi olarak değerlendirilmemelidir.

---

## Tamamlanan Özellikler

- Web sayfasından HTML çekme
- HTTP hata kontrolü
- HTML içeriğini okunabilir metne dönüştürme
- Regex tabanlı bilgi çıkarımı
- Ürün ve hedef kitle tespiti
- Kâr payı ve vade standardizasyonu
- JSON çıktısı oluşturma
- CSV verisi okuma
- Kampanya karşılaştırma analizi
- Git ve GitHub tabanlı sürüm kontrolü

---

## Gelecek Çalışmalar

- Gerçek web metni ile extractor modülünün uçtan uca entegrasyonu
- Birden fazla katılım bankasının sisteme eklenmesi
- Siteye özel içerik seçicilerin geliştirilmesi
- Dinamik web sayfaları için alternatif veri toplama yöntemleri
- Daha fazla ürün ve hedef kitle sınıfının desteklenmesi
- Gelişmiş karşılaştırma ve öneri mekanizması
- Otomatik testlerin eklenmesi
- Yapay zekâ ve doğal dil işleme modelleriyle esnek bilgi çıkarımı

---

## Takım

Bu proje, TEKNOFEST 2026 ön değerlendirme süreci kapsamında iki kişilik takım tarafından geliştirilmektedir.