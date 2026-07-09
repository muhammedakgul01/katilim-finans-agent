import re

#metin = "Yeni müşterilere özel %2,05 kâr payı ile 36 ay vadeli konut finansmanı."

#sonuc = re.search(r"\d+\s*ay", metin)

#print(sonuc.group())

metin ="Yeni müşterilere özel %2,05 kâr payı ile 36 ay vadeli konut finansmanı."

vadeSonuc = re.search(r"\d+\s*ay", metin)

karSonuc = re.search(r"%\d+,\d+\s*kâr payı", metin)

print(vadeSonuc.group())
print(karSonuc.group())