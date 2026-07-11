import requests
from bs4 import BeautifulSoup

url = "https://www.kuveytturk.com.tr/kendim-icin/finansmanlar/konut-finansmanlari/konut-finansmani"

response = requests.get(url, timeout = 10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")


# Durum kodu
print("Durum kodu: ", response.status_code)

# Sayfa başlığı
print("Sayfa Başlığı: ", soup.title.text)

# Temiz metin (ilk 1000 karakter)
temiz_metin = soup.get_text(separator=" ", strip=True)
print("Temiz metnin ilk 1000 karakteri:")
print(temiz_metin[:1000])


print("Konut Finansmanı" in temiz_metin)

index = temiz_metin.find("Konut Finansmanı")
print("Index: ", index)
print(temiz_metin[index:index + 1000])