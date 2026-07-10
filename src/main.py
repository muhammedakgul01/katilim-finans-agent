from extractor import vade_bul, kar_payi_bul, urun_bul, hedef_kitle_bul
from normalizer import normalize_vade, normalize_kar_payi
import json
import os


def main():
    # main.py'nin bulunduğu klasör (src)
    script_dizini = os.path.dirname(os.path.abspath(__file__))

    # src'den bir üst dizine çık (proje_klasoru), sonra data/campaign.json'a in
    dosya_yolu = os.path.join(script_dizini, "..", "data", "campaign.json")

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



if __name__ == "__main__":
    main()