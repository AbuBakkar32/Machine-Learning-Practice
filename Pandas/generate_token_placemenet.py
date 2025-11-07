# generate_token_placement.py
import pandas as pd
import math

xlsx_path = "2025_artists_updated_with_countries.xlsx"  # place in same folder
xls = pd.ExcelFile(xlsx_path)
gauguin_df = pd.read_excel(xls, sheet_name='Gauguin final')
vangogh_df = pd.read_excel(xls, sheet_name='Van Gogh final')

def cluster_by_period(df):
    df = df.copy()
    df["PeriodStart"] = (df["Year"] // 5) * 5
    grouped = df.groupby("PeriodStart").agg({
        "Est. Paintings": "sum",
        "Est. Drawings": "sum",
        "Est. Sculptures": "sum",
        "Total Artworks": "sum",
        "Exhibitions": "sum",
        "Number of Artistic Essays/Letters": "sum",
        "Country of Residence": lambda x: x.mode()[0] if not x.mode().empty else "Unknown",
        "Artists in Contact": lambda x: ", ".join(set(x.dropna().astype(str)))
    }).reset_index()
    return grouped

g = cluster_by_period(gauguin_df)
v = cluster_by_period(vangogh_df)

max_artworks = int(max(g["Total Artworks"].max(), v["Total Artworks"].max()))
artwork_scale = math.ceil(max_artworks / 12) if max_artworks>0 else 1

def placement_table(clustered, artist_name):
    rows = []
    for _, r in clustered.iterrows():
        period = int(r["PeriodStart"])
        artworks_tokens = int(math.ceil(r["Total Artworks"] / artwork_scale)) if r["Total Artworks"]>0 else 0
        exhibitions = int(r["Exhibitions"])
        letters_tokens = int(math.ceil(r["Number of Artistic Essays/Letters"] / 5)) if r["Number of Artistic Essays/Letters"]>0 else 0
        country = r["Country of Residence"]
        contacts = 0
        if isinstance(r["Artists in Contact"], str) and r["Artists in Contact"].strip():
            contacts = len([c.strip() for c in r["Artists in Contact"].split(",") if c.strip()])
        rows.append({
            "Artist": artist_name,
            "PeriodStart": period,
            "Artworks": int(r["Total Artworks"]),
            "ArtworksTokens": artworks_tokens,
            "Exhibitions": exhibitions,
            "Letters": int(r["Number of Artistic Essays/Letters"]),
            "LettersTokens": letters_tokens,
            "Country": country,
            "Contacts": contacts
        })
    return pd.DataFrame(rows)

gau_table = placement_table(g, "Gauguin")
van_table = placement_table(v, "VanGogh")
token_table = pd.concat([gau_table, van_table], ignore_index=True).sort_values(["Artist","PeriodStart"])
token_table.to_csv("token_placement.csv", index=False)

print("Wrote token_placement.csv")
print("Artworks token scale: 1 artwork token =", artwork_scale, "artworks")
