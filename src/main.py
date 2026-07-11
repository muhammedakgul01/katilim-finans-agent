import pandas as pd
import json
import os
from extractor import vade_bul, kar_payi_bul, urun_bul, hedef_kitle_bul
from normalizer import normalize_vade, normalize_kar_payi
from analyzer import en_dusuk_kar_payi, en_uzun_vade
from scraper import sayfa_cek



def main():
    # main.py'nin bulunduğu klasör (src)
    script_dizini = os.path.dirname(os.path.abspath(__file__))

    # src'den bir üst dizine çık (proje_klasoru), sonra data/campaign.json'a in
    dosya_yolu = os.path.join(script_dizini, "..", "data", "campaign.json")
    dosya_yolu_csv = os.path.join(script_dizini, "..", "data", "campaigns.csv")

    df = pd.read_csv(dosya_yolu_csv, encoding = "utf-8", header = 0)

    kuveyt_turk_url = "https://www.kuveytturk.com.tr/kendim-icin/finansmanlar/konut-finansmanlari/konut-finansmani"

    html = sayfa_cek(kuveyt_turk_url)

    if html is not None:
        print("Kuveyt Türk sayfası başarıyla çekildi.")
        print(f"HTML uzunluğu: {len(html)}")
    else:
        print("Kuveyt Türk sayfası çekilemedi")


    metin = "Yeni müşterilere özel %2,05 kâr payı ile 36 ay vadeli konut finansmanı."

    #Extractor ile bilgiler çıkarılır
    vade = vade_bul(metin)
    kar_payi = kar_payi_bul(metin)
    urun = urun_bul(metin)
    hedef = hedef_kitle_bul(metin)

    #Normalizer ile bilgiler temizlenir
    vade = normalize_vade(vade)
    kar_payi = normalize_kar_payi(kar_payi)

#    print("Vade:", normalize_vade(vade))
#    print("Kâr Payı:", normalize_kar_payi(kar_payi))
#    print("Ürün:", urun)
#    print("Hedef:", hedef)

    #Bilgiler bir dict'e eklenir
    kampanya = {"banka": "", "urun": urun, "kar_payi": kar_payi, "vade": vade, "hedef": hedef}

    #Bilgiler yazdırılır
    print(kampanya)

    kampanya_json = json.dumps(kampanya, indent = 4, ensure_ascii=False)

    with open(dosya_yolu, "w", encoding="utf-8") as f:
        f.write(kampanya_json)

    print("\nEn düşük kâr payı:")
    print(en_dusuk_kar_payi(df))

    print("\nEn uzun vade:")
    print(en_uzun_vade(df))

if __name__ == "__main__":
    main()