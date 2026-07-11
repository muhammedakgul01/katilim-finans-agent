import requests
from bs4 import BeautifulSoup


def sayfa_cek(url):
    try:
        response = requests.get(url, timeout = 10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Hata oluştu: {e}")
        return None


def html_metin_ayikla(html):
    soup = BeautifulSoup(html, "html.parser")
    temiz_metin = soup.get_text(separator=" ", strip=True)
    return temiz_metin