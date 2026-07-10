import pandas as pd
import os

# pandas_01.py'nin bulunduğu klasör (sandbox)
script_dizini = os.path.dirname(os.path.abspath(__file__))

# sandbox'den bir üst dizine çık (proje_klasoru), sonra data/campaign.scv'a in
dosya_yolu = os.path.join(script_dizini, "..", "data", "campaigns.csv")

df = pd.read_csv(dosya_yolu, encoding="utf-8", header = 0)
en_dusuk_kar_payi = df.loc[df["profit_rate"].idxmin(), "bank"]
print(df.head())


print("En düşük kâr payına sahip banka: ",en_dusuk_kar_payi)
print("Kâr payı: ", df["profit_rate"].min())
#print(df["profit_rate"])
#print(df["profit_rate"].min())