from extractor import vade_bul, kar_payi_bul, urun_bul, hedef_kitle_bul
from normalizer import normalize_vade, normalize_kar_payi


def main():
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




if __name__ == "__main__":
    main()