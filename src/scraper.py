import requests

def sayfa_cek(url):
    try:
        response = requests.get(url, timeout = 10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Hata oluştu: {e}")
        return None
