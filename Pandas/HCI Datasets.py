import pandas as pd
import numpy as np
from io import StringIO  # For simulating data loads

# Simulate/load sample data (replace with pd.read_csv from actual downloads)
# Real workflow: Download CSVs from links above, then merge on 'country' and 'year'

np.random.seed(42)  # For reproducibility
countries = ['USA', 'China', 'India', 'Brazil', 'Germany', 'South Africa', 'Nigeria'] * 50  # ~350 rows sample; expand for full
years = np.repeat(np.arange(1980, 2025), len(countries)//45)
print(years)

data = pd.DataFrame({
    'country': np.tile(countries, 45)[:len(years)],
    'year': years,
    'region': np.random.choice(['North America', 'Asia', 'Africa', 'Europe', 'Latin America'], len(years)),
    'income_group': np.random.choice(['High', 'Upper-Middle', 'Lower-Middle', 'Low'], len(years)),
    'gini': np.random.uniform(0.25, 0.65, len(years)),  # From WIID/OECD
    'palma_ratio': np.random.uniform(0.8, 2.5, len(years)),
    'share_bottom50': np.random.uniform(0.05, 0.25, len(years)),
    'share_middle40': np.random.uniform(0.4, 0.5, len(years)),
    'share_top10': np.random.uniform(0.3, 0.6, len(years)),
    'share_top1': np.random.uniform(0.1, 0.25, len(years)),  # WID
    'wealth_share_top10': np.random.uniform(0.6, 0.85, len(years)),  # UBS
    'wealth_share_top1': np.random.uniform(0.3, 0.5, len(years)),
    'avg_income_bottom50_usd': np.random.uniform(1000, 15000, len(years)),
    'avg_income_top10_usd': np.random.uniform(50000, 200000, len(years)),
    'co2_per_capita_decile_avg': np.random.uniform(1, 20, len(years)),  # UNDP/WID
    'gender_pay_gap': np.random.uniform(0.1, 0.3, len(years)),
    'female_share_parliament': np.random.uniform(0.2, 0.5, len(years)),
    'hdi': np.random.uniform(0.4, 0.95, len(years)),  # UNDP
    'multidim_poverty_index': np.random.uniform(0.0, 0.4, len(years))
})

# Add correlations for realism (e.g., higher Gini -> lower bottom50)
data['share_bottom50'] = data['gini'].apply(lambda x: max(0.05, 0.3 - x*0.4))

data = data.sort_values(['country', 'year']).reset_index(drop=True)  # ~1.3k rows sample; full = 12k+
data.to_csv('inequality_2025_full.csv', index=False)
print(data.head())
print(f"Dataset shape: {data.shape} (expand with full downloads for 10k+ rows)")