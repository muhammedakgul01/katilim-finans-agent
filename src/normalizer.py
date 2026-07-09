def normalize_vade(vade):
    return int(vade.replace("ay", "").strip())

def normalize_kar_payi(kar_payi):
    kar_payi_normalize = kar_payi.replace("%", "").replace(",", ".")
    return float(kar_payi_normalize)

