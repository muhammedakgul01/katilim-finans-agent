import re


def vade_bul(metin):
    sonuc = re.search(r"\d+\s*ay", metin)

    if sonuc:
        return sonuc.group()

    return None


def kar_payi_bul(metin):
    sonuc = re.search(r"%\d+,\d+", metin)

    if sonuc:
        return sonuc.group()

    return None

def urun_bul(metin):
    if re.search(r"konut", metin, re.IGNORECASE):
        return "Konut Finansmanı"
    elif re.search(r"taşıt", metin, re.IGNORECASE):
        return "Taşıt Finansmanı"
    elif re.search(r"ihtiyaç", metin, re.IGNORECASE):
        return "İhtiyaç Finansmanı"
    return None

def hedef_kitle_bul(metin):
    if re.search(r"yeni müşteri", metin, re.IGNORECASE) or re.search(r"yeni müşterilere", metin, re.IGNORECASE):
        return "Yeni Müşteri"
    return None
