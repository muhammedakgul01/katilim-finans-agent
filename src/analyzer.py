def en_dusuk_kar_payi(df):
    min_index = df["profit_rate"].idxmin()

    sonuc = {
        "bank": df.loc[min_index, "bank"],
        "profit_rate": float(df.loc[min_index, "profit_rate"]),
    }

    return sonuc

def en_uzun_vade(df):
    max_index = df["term"].idxmax()

    sonuc = {
        "bank": df.loc[max_index, "bank"],
        "term": int(df.loc[max_index, "term"])
    }

    return sonuc