import requests

response = requests.get("https://www.kuveytturk.com.tr/kendim-icin/finansmanlar/konut-finansmanlari/konut-finansmani", timeout = 10)

print(response.status_code)
print(response.text[:1000])

if "Konut Finansmanı" in response.text:
    print("Var")
else:
    print("Yok")