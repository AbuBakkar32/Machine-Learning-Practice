"""
titian_viz.py

Produces visualizations that answer the five questions using the provided
geocoded CSV (geocoded_titian.csv). Outputs PNG charts and two interactive
HTML maps (using folium) for the geography-related questions.

Requirements:
  pip install pandas matplotlib seaborn folium geopy haversine

Usage:
  Data_Analysis_HCI.py

Outputs:
  - q1_genre_1530_1540.png
  - q2_philipii_genre.png
  - q2_philipii_map.html
  - q3_venice_religious_patrons.png
  - q4_private_outside_myth_1540_1570.png
  - q5_most_distant_unknown.html
  - printed summary of numeric answers
"""

import os
import math
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium import Popup
from haversine import haversine, Unit

# Optional: geocoding for patron origins (used in Q5)
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from geopy.exc import GeopyError

sns.set(style="whitegrid")


def normalize_columns(df):
    df = df.copy()
    new_cols = []
    for c in df.columns:
        nc = c.strip().lower().replace(' ', '_').replace('/', '_').replace('#', 'num')
        new_cols.append(nc)
    df.columns = new_cols
    return df


def ensure_output_dir(d='outputs'):
    if not os.path.exists(d):
        os.makedirs(d)
    return d


def q1_genre_1530_1540(df, outdir):
    df1 = df[(df['original_date_created'].astype(int) >= 1530) &
             (df['original_date_created'].astype(int) <= 1540)]
    counts = df1['original_genre'].str.lower().value_counts()
    print("\nQ1 - genre counts (1530-1540):\n", counts.to_string())

    plt.figure(figsize=(8, 5))
    sns.barplot(x=counts.index, y=counts.values, palette="muted")
    plt.title("Titian: Genre counts (1530-1540)")
    plt.xlabel("Genre")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    out = os.path.join(outdir, 'q1_genre_1530_1540.png')
    plt.savefig(out, dpi=150)
    plt.close()
    print(f"Saved Q1 chart to {out}")


def q2_philipii(df, outdir):
    # Filter Philip II rows (case-insensitive contains)
    mask = df['original_patron'].astype(str).str.lower().str.contains('philip ii')
    phil = df[mask].copy()
    if phil.empty:
        print("Q2 - No Philip II rows found.")
        return

    counts = phil['original_genre'].str.lower().value_counts()
    print("\nQ2 - Philip II genre counts:\n", counts.to_string())

    # Bar chart of genres
    plt.figure(figsize=(8, 5))
    sns.barplot(x=counts.index, y=counts.values, palette="coolwarm")
    plt.title("Philip II patronage by genre (dataset)")
    plt.xlabel("Genre")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    out_png = os.path.join(outdir, 'q2_philipii_genre.png')
    plt.savefig(out_png, dpi=150)
    plt.close()
    print(f"Saved Q2 genre chart to {out_png}")

    # Map of artworks (use available lat/lon columns)
    # center map on mean coords (fallback to Venice)
    try:
        lat_mean = phil['lat'].astype(float).mean()
        lon_mean = phil['lon'].astype(float).mean()
        if math.isnan(lat_mean) or math.isnan(lon_mean):
            raise ValueError
    except Exception:
        lat_mean, lon_mean = 45.43719, 12.33459  # Venice

    fmap = folium.Map(location=[lat_mean, lon_mean], zoom_start=5, tiles='CartoDB Positron')

    # color map for genres
    genre_colors = {
        'religious': 'blue',
        'myth': 'green',
        'portrait': 'purple',
        'history': 'orange',
        'unknown': 'gray',
        'default': 'red'
    }

    for _, r in phil.iterrows():
        try:
            lat = float(r['lat'])
            lon = float(r['lon'])
        except Exception:
            continue
        genre = str(r['original_genre']).lower()
        color = genre_colors.get(genre, genre_colors['default'])
        title = f"{r.get('original_title','')} ({r.get('original_date_created','')})<br>Genre: {r.get('original_genre','')}"
        popup = folium.Popup(title, max_width=400)
        folium.CircleMarker(location=[lat, lon],
                            radius=5,
                            color=color,
                            fill=True,
                            fill_color=color,
                            fill_opacity=0.8,
                            popup=popup).add_to(fmap)

    out_html = os.path.join(outdir, 'q2_philipii_map.html')
    fmap.save(out_html)
    print(f"Saved Q2 Philip II map to {out_html}")


def q3_venice_religious_patrons(df, outdir):
    # Normalize patron origin to string
    origin = df['original_patron_origin'].astype(str).str.lower()
    mask = (origin.str.contains('venice')) & (df['original_genre'].str.lower() == 'religious')
    ven_relig = df[mask].copy()
    counts = ven_relig['original_patron'].fillna('unknown').astype(str).value_counts()
    print("\nQ3 - Venice-based patrons supporting religion (top):\n", counts.head(20).to_string())

    plt.figure(figsize=(10, 6))
    sns.barplot(x=counts.values[:15], y=counts.index[:15], palette='viridis')
    plt.title("Venice-based patrons supporting religious artworks (by count)")
    plt.xlabel("Count")
    plt.ylabel("Patron")
    plt.tight_layout()
    out = os.path.join(outdir, 'q3_venice_religious_patrons.png')
    plt.savefig(out, dpi=150)
    plt.close()
    print(f"Saved Q3 chart to {out}")


def q4_private_outside_myth(df, outdir):
    year = df['original_date_created'].astype(int)
    patron_type = df['original_patron_type'].astype(str).str.lower()
    patron_origin = df['original_patron_origin'].astype(str).str.lower()

    mask = (patron_type == 'private') & (~patron_origin.str.contains('venice')) & \
           (df['original_genre'].str.lower() == 'myth') & (year >= 1540) & (year <= 1570)
    sub = df[mask].copy()
    counts = sub['original_patron'].fillna('unknown').astype(str).value_counts()
    print("\nQ4 - Private patrons outside Venice supporting myth (1540-1570):\n", counts.to_string())

    plt.figure(figsize=(10, 6))
    sns.barplot(x=counts.values[:20], y=counts.index[:20], palette='magma')
    plt.title("Private patrons outside Venice supporting myth (1540-1570)")
    plt.xlabel("Count")
    plt.ylabel("Patron")
    plt.tight_layout()
    out = os.path.join(outdir, 'q4_private_outside_myth_1540_1570.png')
    plt.savefig(out, dpi=150)
    plt.close()
    print(f"Saved Q4 chart to {out}")


def geocode_locations(names):
    """
    Geocode a list of place names using Nominatim (geopy). Returns dict name->(lat,lon)
    Requires internet access. Uses rate limiter.
    """
    geocoded = {}
    try:
        geolocator = Nominatim(user_agent="titian_viz_geocoder", timeout=10)
        geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1, max_retries=2, error_wait_seconds=2.0)
        for n in names:
            if not n or n.lower() in ('nan', 'unknown', ''):
                continue
            try:
                loc = geocode(n + ", Europe")  # hint to get European matches first
                if loc:
                    geocoded[n] = (loc.latitude, loc.longitude)
                else:
                    geocoded[n] = None
            except GeopyError:
                geocoded[n] = None
    except Exception as e:
        print("Geocoding failed (no internet or service error):", e)
    return geocoded


def q5_most_distant_unknown(df, outdir):
    # Find rows where patron is 'unknown' (case-insensitive or NaN)
    patron = df['original_patron'].astype(str).str.lower()
    place_created = df['original_place_created'].astype(str).str.lower()
    # Focus on artworks created in Venice
    mask = ((patron == 'unknown') | (patron == 'nan')) & (place_created.str.contains('venice'))
    unknowns = df[mask].copy()

    if unknowns.empty:
        print("Q5 - No 'unknown' patrons supporting artworks created in Venice found in dataset.")
        return

    # Collect unique patron origins for these unknown rows
    candidate_origins = unknowns['original_patron_origin'].dropna().unique()
    candidate_origins = [o for o in candidate_origins if str(o).strip() and str(o).lower() != 'nan']

    print("\nQ5 - candidate 'unknown' patron origins (for Venice-created artworks):", candidate_origins)

    # Geocode the patron origins (may require internet). If geocoding fails, we will try a small
    # manual fallback dictionary for common places used in dataset.
    geocoded = geocode_locations(candidate_origins)
    # Fallback coordinates for some known places (approx)
    fallback = {
        'padua': (45.4064, 11.8768),
        'augustbruck': None,
        'milan': (45.4642, 9.1900),
        'paris': (48.8566, 2.3522),
        'rome': (41.9028, 12.4964),
        'bologna': (44.4949, 11.3426),
        'vienna': (48.2082, 16.3738),
        'besançon': (47.2396, 6.0241),
        'brussels': (50.8503, 4.3517),
        'milan,lombardy,italy': (45.4642, 9.19),
        'padova': (45.4064, 11.8768),
    }

    # For each unknown row, compute distance from patron origin to artwork lat/lon (artwork coords are lat/lon columns)
    best = {'distance_km': -1, 'row': None, 'patron_origin': None, 'patron_origin_coords': None}
    for _, r in unknowns.iterrows():
        origin = str(r['original_patron_origin']).strip()
        if not origin or origin.lower() in ('nan', 'none', ''):
            continue

        patron_coords = geocoded.get(origin, None)
        if patron_coords is None:
            # try fallback keys lowered
            patron_coords = fallback.get(origin.lower(), None)

        # If still None, attempt minimal geocode again with different hint
        if patron_coords is None:
            # try geocode single name without "Europe"
            try:
                geol = Nominatim(user_agent="titian_viz_geocoder_small", timeout=10)
                loc = geol.geocode(origin, exactly_one=True)
                if loc:
                    patron_coords = (loc.latitude, loc.longitude)
            except Exception:
                pass

        if patron_coords is None:
            # cannot compute distance
            continue

        try:
            art_coords = (float(r['lat']), float(r['lon']))
        except Exception:
            continue

        dist = haversine(patron_coords, art_coords, unit=Unit.KILOMETERS)
        if dist > best['distance_km']:
            best.update({'distance_km': dist, 'row': r, 'patron_origin': origin, 'patron_origin_coords': patron_coords})

    if best['row'] is None:
        print("Q5 - Could not compute distances for any unknown patron origins (missing geocodes).")
        return

    r = best['row']
    print("\nQ5 - Most distant unknown patron supporting an artwork created in Venice:")
    print(f"  Painting: {r.get('original_title','')} ({r.get('original_date_created','')})")
    print(f"  Patron origin: {best['patron_origin']}")
    print(f"  Distance (km): {best['distance_km']:.1f}")

    # Create a small folium map showing the artwork location and the patron origin and a line between them
    map_center = [(best['patron_origin_coords'][0] + float(r['lat'])) / 2,
                  (best['patron_origin_coords'][1] + float(r['lon'])) / 2]
    fmap = folium.Map(location=map_center, zoom_start=6, tiles='CartoDB Positron')

    folium.Marker(location=[float(r['lat']), float(r['lon'])],
                  popup=folium.Popup(f"Artwork: {r.get('original_title','')}", max_width=300),
                  icon=folium.Icon(color='blue', icon='info-sign')).add_to(fmap)

    folium.Marker(location=list(best['patron_origin_coords']),
                  popup=folium.Popup(f"Patron origin: {best['patron_origin']}", max_width=300),
                  icon=folium.Icon(color='red', icon='user')).add_to(fmap)

    folium.PolyLine(locations=[list(best['patron_origin_coords']), [float(r['lat']), float(r['lon'])]],
                    color='purple', weight=2.5, opacity=0.8).add_to(fmap)

    out_html = os.path.join(outdir, 'q5_most_distant_unknown.html')
    fmap.save(out_html)
    print(f"Saved Q5 map to {out_html}")


def main():
    outdir = ensure_output_dir('outputs')

    # try to read geocoded_titian.csv first
    fname = 'geocoded_titian.csv'
    if not os.path.exists(fname):
        print(f"Error: {fname} not found in current directory. Please place 'geocoded_titian.csv' here.")
        return

    df = pd.read_csv(fname, dtype=str, encoding='utf-8', low_memory=False)
    df = normalize_columns(df)

    # Some datasets may have missing 'original_date_created' as string; ensure numeric where possible
    # If 'original_date_created' contains ranges like "Rome?" we'll attempt to extract leading 4-digit year
    def parse_year(x):
        try:
            if pd.isna(x):
                return None
            s = str(x)
            # find first 4-digit number
            import re
            m = re.search(r'(\d{4})', s)
            if m:
                return int(m.group(1))
            else:
                return None
        except Exception:
            return None

    if 'original_date_created' in df.columns:
        df['original_date_created'] = df['original_date_created'].apply(parse_year).astype('Int64').fillna(0).astype(int)
    else:
        print("Warning: 'original_date_created' column not present. Some filters will fail.")

    # Ensure genre, patron and other key cols exist
    for col in ['original_genre', 'original_patron', 'original_patron_origin', 'original_patron_type', 'lat', 'lon', 'original_place_created']:
        if col not in df.columns:
            df[col] = ''

    # Q1
    q1_genre_1530_1540(df, outdir)

    # Q2
    q2_philipii(df, outdir)

    # Q3
    q3_venice_religious_patrons(df, outdir)

    # Q4
    q4_private_outside_myth(df, outdir)

    # Q5
    q5_most_distant_unknown(df, outdir)

    print("\nAll visualizations saved into the 'outputs' folder.")


if __name__ == '__main__':
    main()