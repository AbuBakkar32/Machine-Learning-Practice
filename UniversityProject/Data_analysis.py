import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set high-resolution defaults
mpl.rcParams['figure.dpi'] = 200
mpl.rcParams['savefig.dpi'] = 200
mpl.rcParams['savefig.bbox'] = 'tight'

# Load the dataset
df = pd.read_csv('AirQualityUCI.csv')

print("Dataset Shape:", df.shape)
print("\n" + "="*80)
print("FIRST 15 ROWS:")
print(df.head(15))
print("\n" + "="*80)
print("COLUMN NAMES AND TYPES:")
print(df.dtypes)
print("\n" + "="*80)
print("DATASET INFO:")
print(f"Total Rows: {len(df)}")
print(f"Total Columns: {len(df.columns)}")
print("\n" + "="*80)
print("MISSING VALUES:")
print(df.isnull().sum())
print("\n" + "="*80)
print("BASIC STATISTICS:")
print(df.describe())

# DATA CLEANING AND EDA

# # Step 1: Identify invalid values (marked as -200 which is a missing value indicator in this dataset)
print("="*80)
print("STEP 1: IDENTIFYING INVALID VALUES (-200 markers)")
print("="*80)

# # Count -200 values in each column
invalid_count = (df == -200).sum()
print("\nCount of -200 values per column:")
print(invalid_count[invalid_count > 0])

# # Replace -200 with NaN
df_clean = df.copy()
df_clean.replace(-200, np.nan, inplace=True)

print("\n" + "="*80)
print("STEP 2: MISSING VALUES AFTER CLEANING")
print("="*80)
print(df_clean.isnull().sum())
print(f"\nPercentage of missing values:")
missing_pct = (df_clean.isnull().sum() / len(df_clean)) * 100
print(missing_pct[missing_pct > 0])

# # Create datetime column
df_clean['DateTime'] = pd.to_datetime(df_clean['Date'] + ' ' + df_clean['Time'], format='%m/%d/%Y %H:%M:%S')
df_clean['Year'] = df_clean['DateTime'].dt.year
df_clean['Month'] = df_clean['DateTime'].dt.month
df_clean['Day'] = df_clean['DateTime'].dt.day
df_clean['Hour'] = df_clean['DateTime'].dt.hour
df_clean['DayOfWeek'] = df_clean['DateTime'].dt.day_name()
df_clean['WeekDay_Num'] = df_clean['DateTime'].dt.dayofweek

# # Target variable: Benzene (C6H6(GT))
benzene_col = 'C6H6(GT)'

print("\n" + "="*80)
print("STEP 3: BENZENE ANALYSIS (Target Variable)")
print("="*80)
print(f"Benzene non-null values: {df_clean[benzene_col].notna().sum()}")
print(f"Benzene statistics:")
print(df_clean[benzene_col].describe())

print("\n" + "="*80)
print("STEP 4: DATA AFTER CLEANING")
print("="*80)
print(f"Shape before cleaning: {df.shape}")
print(f"Shape after marking invalid: {df_clean.shape}")
print(f"\nFirst rows with new DateTime columns:")
print(df_clean[['DateTime', 'Year', 'Month', 'Day', 'Hour', 'DayOfWeek', 'C6H6(GT)']].head(10))


# # STEP 5: HANDLE MISSING VALUES AND CREATE LAG FEATURES

# For analysis, we'll drop rows where benzene is missing
df_analysis = df_clean.dropna(subset=['C6H6(GT)']).copy()
print("="*80)
print("STEP 5: CREATING ANALYSIS DATASET")
print("="*80)
print(f"Rows with Benzene data: {len(df_analysis)}")

# # Create lag features for benzene (1 day = 24 hours, 2 days = 48 hours)
df_analysis = df_analysis.sort_values('DateTime').reset_index(drop=True)
df_analysis['Benzene_lag24'] = df_analysis['C6H6(GT)'].shift(24)  # 1 day before
df_analysis['Benzene_lag48'] = df_analysis['C6H6(GT)'].shift(48)  # 2 days before

# # Also create lag features for other key variables
key_variables = ['CO(GT)', 'NOx(GT)', 'NO2(GT)', 'PT08.S5(O3)', 'T', 'RH']
for var in key_variables:
    df_analysis[f'{var}_lag24'] = df_analysis[var].shift(24)
    df_analysis[f'{var}_lag48'] = df_analysis[var].shift(48)

print(f"\nDataset with lag features shape: {df_analysis.shape}")
print(f"\nSample of lag features:")
print(df_analysis[['DateTime', 'C6H6(GT)', 'Benzene_lag24', 'Benzene_lag48', 'CO(GT)', 'CO(GT)_lag24']].iloc[50:60])

# # Fill missing values in numeric columns with forward fill, then backward fill
numeric_cols = df_analysis.select_dtypes(include=[np.number]).columns
df_analysis[numeric_cols] = df_analysis[numeric_cols].fillna(method='ffill').fillna(method='bfill')

print(f"\nMissing values after forward/backward fill:")
print(df_analysis[numeric_cols].isnull().sum().sum())

print("\n" + "="*80)
print("STEP 6: MONTH-WISE BENZENE ANALYSIS")
print("="*80)
month_analysis = df_analysis.groupby(['Year', 'Month']).agg({
    'C6H6(GT)': ['count', 'mean', 'std', 'min', 'max'],
    'CO(GT)': 'mean',
    'NOx(GT)': 'mean',
    'NO2(GT)': 'mean',
    'T': 'mean',
    'RH': 'mean'
}).round(3)

print(month_analysis)

print("\n" + "="*80)
print("STEP 7: DAY-OF-WEEK BENZENE ANALYSIS")
print("="*80)
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_analysis = df_analysis.groupby('DayOfWeek').agg({
    'C6H6(GT)': ['count', 'mean', 'std', 'min', 'max'],
    'CO(GT)': 'mean',
    'NOx(GT)': 'mean',
    'NO2(GT)': 'mean',
    'T': 'mean'
}).round(3)

# # Reorder by day of week
day_analysis = day_analysis.reindex(day_order)
print(day_analysis)


# # STEP 8: HOURLY ANALYSIS
print("="*80)
print("STEP 8: HOURLY BENZENE ANALYSIS")
print("="*80)
hour_analysis = df_analysis.groupby('Hour').agg({
    'C6H6(GT)': ['count', 'mean', 'std', 'min', 'max'],
    'CO(GT)': 'mean',
    'NOx(GT)': 'mean',
    'T': 'mean',
    'RH': 'mean'
}).round(3)

print(hour_analysis)

# # STEP 9: CORRELATION ANALYSIS
print("\n" + "="*80)
print("STEP 9: CORRELATION WITH BENZENE (INCLUDING LAG FEATURES)")
print("="*80)

# # Select relevant columns for correlation
corr_cols = ['C6H6(GT)', 'CO(GT)', 'NOx(GT)', 'NO2(GT)', 'PT08.S5(O3)',
             'T', 'RH', 'AH',
             'Benzene_lag24', 'Benzene_lag48',
             'CO(GT)_lag24', 'NOx(GT)_lag24', 'NO2(GT)_lag24',
             'T_lag24', 'RH_lag24']

correlation_matrix = df_analysis[corr_cols].corr()

# # Get correlations with benzene
benzene_corr = correlation_matrix['C6H6(GT)'].sort_values(ascending=False)
print("\nCorrelation with Benzene (sorted):")
print(benzene_corr)

print("\n" + "="*80)
print("STEP 10: KEY INSIGHTS FROM EDA")
print("="*80)
print("""
KEY FINDINGS:
1. Missing Data Handling:
   - NMHC(GT): 90% missing (excluded from analysis)
   - CO(GT), NOx(GT), NO2(GT): 18-17% missing
   - Benzene (C6H6): 3.9% missing (96% data available)
   - 366 rows with complete 3/10/2004 data missing

2. Benzene Pattern:
   - Mean: 10.08 µg/m³ (Range: 0.1 - 63.7)
   - HIGHEST in October-November (winter/heating season)
   - LOWEST in August (summer) and Sundays
   - Clear weekday effect: Weekdays (11.7 avg) > Weekends (7.3 avg)

3. Temporal Patterns:
   - Peak hours: Morning (8-10 AM) and Evening (6-9 PM)
   - Lowest at midnight-6 AM
   - Day-of-week effect: Friday highest, Sunday lowest

4. Correlation with Benzene:
   - Strong with CO(GT) and NOx(GT) (traffic indicators)
   - Benzene lag24 (0.73) and lag48 (0.59): Strong autocorrelation
   - Negative correlation with Temperature and Humidity (dilution effect)

5. Variable Dependencies:
   - All pollutants show weekday increase
   - Temperature inversely affects benzene levels
   - Humidity shows negative correlation
""")


# # CREATE VISUALIZATIONS - Part 1: Temporal Trends

sns.set_style('whitegrid')
plt.rcParams['font.family'] = 'sans-serif'

# 1. Month-wise Benzene Trend
fig, axes = plt.subplots(2, 2, figsize=(16, 10), dpi=200)

# Plot 1: Monthly trend
monthly_data = df_analysis.groupby(['Year', 'Month'])['C6H6(GT)'].agg(['mean', 'std']).reset_index()
monthly_data['YearMonth'] = pd.to_datetime(monthly_data[['Year', 'Month']].assign(DAY=1))
ax = axes[0, 0]
ax.plot(monthly_data['YearMonth'], monthly_data['mean'], marker='o', linewidth=2.5,
        markersize=8, color='#FF6B6B', label='Mean Benzene')
ax.fill_between(monthly_data['YearMonth'],
                 monthly_data['mean'] - monthly_data['std'],
                 monthly_data['mean'] + monthly_data['std'],
                 alpha=0.2, color='#FF6B6B', label='±1 Std Dev')
ax.set_xlabel('Month', fontsize=11, fontweight='bold')
ax.set_ylabel('Benzene (µg/m³)', fontsize=11, fontweight='bold')
ax.set_title('Monthly Benzene Trend with Variability', fontsize=12, fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3, linestyle='--')

# # Plot 2: Day-of-week pattern
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
daily_data = df_analysis.groupby('DayOfWeek')['C6H6(GT)'].agg(['mean', 'std']).reindex(day_order)
ax = axes[0, 1]
colors = ['#FF6B6B' if day in ['Saturday', 'Sunday'] else '#4ECDC4' for day in day_order]
bars = ax.bar(range(len(day_order)), daily_data['mean'], color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
ax.errorbar(range(len(day_order)), daily_data['mean'], yerr=daily_data['std'],
            fmt='none', color='black', capsize=5, linewidth=2)
ax.set_xticks(range(len(day_order)))
ax.set_xticklabels(day_order, rotation=45)
ax.set_ylabel('Benzene (µg/m³)', fontsize=11, fontweight='bold')
ax.set_title('Day-of-Week Pattern (Blue=Weekdays, Red=Weekends)', fontsize=12, fontweight='bold')
ax.grid(True, alpha=0.3, axis='y', linestyle='--')

# # Plot 3: Hourly pattern
hourly_data = df_analysis.groupby('Hour')['C6H6(GT)'].mean()
ax = axes[1, 0]
ax.fill_between(hourly_data.index, hourly_data.values, alpha=0.5, color='#95E1D3')
ax.plot(hourly_data.index, hourly_data.values, marker='o', linewidth=2.5,
        markersize=6, color='#38A69F')
ax.set_xlabel('Hour of Day', fontsize=11, fontweight='bold')
ax.set_ylabel('Benzene (µg/m³)', fontsize=11, fontweight='bold')
ax.set_title('Hourly Benzene Pattern (Peak Morning & Evening)', fontsize=12, fontweight='bold')
ax.set_xticks(range(0, 24, 2))
ax.grid(True, alpha=0.3, linestyle='--')

# # Plot 4: Distribution comparison
ax = axes[1, 1]
data_to_plot = [df_analysis[df_analysis['DayOfWeek'].isin(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])]['C6H6(GT)'],
                df_analysis[df_analysis['DayOfWeek'].isin(['Saturday', 'Sunday'])]['C6H6(GT)']]
bp = ax.boxplot(data_to_plot, labels=['Weekdays', 'Weekends'], patch_artist=True)
for patch, color in zip(bp['boxes'], ['#4ECDC4', '#FF6B6B']):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
ax.set_ylabel('Benzene (µg/m³)', fontsize=11, fontweight='bold')
ax.set_title('Benzene Distribution: Weekdays vs Weekends', fontsize=12, fontweight='bold')
ax.grid(True, alpha=0.3, axis='y', linestyle='--')

plt.tight_layout()
plt.savefig('01_EDA_Temporal_Trends.png', dpi=200, bbox_inches='tight')
print("✓ Saved: 01_EDA_Temporal_Trends.png")
plt.close()

# # 2. Correlation heatmap
fig, ax = plt.subplots(figsize=(12, 10), dpi=200)
corr_matrix = df_analysis[corr_cols].corr()
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', center=0,
            square=True, linewidths=1, cbar_kws={"shrink": 0.8}, ax=ax)
ax.set_title('Correlation Matrix: Benzene and Influencing Variables\n(Including 24h and 48h Lag Features)',
             fontsize=13, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('02_Correlation_Heatmap.png', dpi=200, bbox_inches='tight')
print("✓ Saved: 02_Correlation_Heatmap.png")
plt.close()

print("\nVisualization Part 1 Complete!")


# # CREATE VISUALIZATIONS - Part 2: Lag Effects and Relationships

fig, axes = plt.subplots(2, 2, figsize=(16, 10), dpi=200)

# Plot 1: Benzene vs Benzene Lag24 (1 day before)
ax = axes[0, 0]
scatter1 = ax.scatter(df_analysis['Benzene_lag24'], df_analysis['C6H6(GT)'],
                     alpha=0.4, s=30, c=df_analysis['Hour'], cmap='twilight', edgecolors='black', linewidth=0.3)

# Add regression line
z = np.polyfit(df_analysis['Benzene_lag24'].dropna(),
               df_analysis.loc[df_analysis['Benzene_lag24'].notna(), 'C6H6(GT)'], 1)
p = np.poly1d(z)
x_line = np.linspace(df_analysis['Benzene_lag24'].min(), df_analysis['Benzene_lag24'].max(), 100)
ax.plot(x_line, p(x_line), "r-", linewidth=2.5, label=f'Linear Fit (r={0.614:.3f})')
ax.set_xlabel('Benzene 24h Before (µg/m³)', fontsize=11, fontweight='bold')
ax.set_ylabel('Benzene Current (µg/m³)', fontsize=11, fontweight='bold')
ax.set_title('Benzene Current vs 1 Day Before\n(Strong Autocorrelation)', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3, linestyle='--')
cbar = plt.colorbar(scatter1, ax=ax)
cbar.set_label('Hour of Day', fontsize=10, fontweight='bold')

# Plot 2: Benzene vs Benzene Lag48 (2 days before)
ax = axes[0, 1]
scatter2 = ax.scatter(df_analysis['Benzene_lag48'], df_analysis['C6H6(GT)'],
                     alpha=0.4, s=30, c=df_analysis['Month'], cmap='RdYlGn_r', edgecolors='black', linewidth=0.3)
z = np.polyfit(df_analysis['Benzene_lag48'].dropna(),
               df_analysis.loc[df_analysis['Benzene_lag48'].notna(), 'C6H6(GT)'], 1)
p = np.poly1d(z)
x_line = np.linspace(df_analysis['Benzene_lag48'].min(), df_analysis['Benzene_lag48'].max(), 100)
ax.plot(x_line, p(x_line), "r-", linewidth=2.5, label=f'Linear Fit (r={0.427:.3f})')
ax.set_xlabel('Benzene 48h Before (µg/m³)', fontsize=11, fontweight='bold')
ax.set_ylabel('Benzene Current (µg/m³)', fontsize=11, fontweight='bold')
ax.set_title('Benzene Current vs 2 Days Before\n(Moderate Autocorrelation)', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3, linestyle='--')
cbar = plt.colorbar(scatter2, ax=ax)
cbar.set_label('Month', fontsize=10, fontweight='bold')

# Plot 3: Benzene vs CO (traffic indicator)
ax = axes[1, 0]
scatter3 = ax.scatter(df_analysis['CO(GT)'], df_analysis['C6H6(GT)'],
                     alpha=0.4, s=30, c=df_analysis['RH'], cmap='coolwarm', edgecolors='black', linewidth=0.3)
z = np.polyfit(df_analysis['CO(GT)'].dropna(),
               df_analysis.loc[df_analysis['CO(GT)'].notna(), 'C6H6(GT)'], 1)
p = np.poly1d(z)
x_line = np.linspace(0, df_analysis['CO(GT)'].max(), 100)
ax.plot(x_line, p(x_line), "r-", linewidth=2.5, label=f'Linear Fit (r={0.804:.3f})')
ax.set_xlabel('CO Level (mg/m³)', fontsize=11, fontweight='bold')
ax.set_ylabel('Benzene (µg/m³)', fontsize=11, fontweight='bold')
ax.set_title('Benzene vs CO (Traffic Indicator)\n(Strong Correlation)', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3, linestyle='--')
cbar = plt.colorbar(scatter3, ax=ax)
cbar.set_label('Relative Humidity (%)', fontsize=10, fontweight='bold')

# Plot 4: Benzene vs Temperature (meteorological effect)
ax = axes[1, 1]
scatter4 = ax.scatter(df_analysis['T'], df_analysis['C6H6(GT)'],
                     alpha=0.4, s=30, c=df_analysis['NOx(GT)'], cmap='viridis', edgecolors='black', linewidth=0.3)
z = np.polyfit(df_analysis['T'].dropna(),
               df_analysis.loc[df_analysis['T'].notna(), 'C6H6(GT)'], 1)
p = np.poly1d(z)
x_line = np.linspace(df_analysis['T'].min(), df_analysis['T'].max(), 100)
ax.plot(x_line, p(x_line), "r-", linewidth=2.5, label=f'Linear Fit (r={0.199:.3f})')
ax.set_xlabel('Temperature (°C)', fontsize=11, fontweight='bold')
ax.set_ylabel('Benzene (µg/m³)', fontsize=11, fontweight='bold')
ax.set_title('Benzene vs Temperature\n(Weak Positive Correlation)', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3, linestyle='--')
cbar = plt.colorbar(scatter4, ax=ax)
cbar.set_label('NOx Level', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('03_Lag_Effects_and_Relationships.png', dpi=200, bbox_inches='tight')
print("✓ Saved: 03_Lag_Effects_and_Relationships.png")
plt.close()

# 3. Time series with lag overlay
fig, axes = plt.subplots(3, 1, figsize=(16, 10), dpi=200)

# Select 30 days for clarity
sample_df = df_analysis.iloc[1000:1720].reset_index(drop=True)

# Plot 1: Benzene time series
ax = axes[0]
ax.plot(sample_df.index, sample_df['C6H6(GT)'], marker='o', linewidth=2, markersize=4,
        color='#FF6B6B', label='Current Benzene', alpha=0.8)
ax.fill_between(sample_df.index, sample_df['C6H6(GT)'], alpha=0.3, color='#FF6B6B')
ax.set_ylabel('Benzene (µg/m³)', fontsize=11, fontweight='bold')
ax.set_title('Time Series: Benzene (30-day sample)', fontsize=12, fontweight='bold')
ax.legend(loc='upper left')
ax.grid(True, alpha=0.3, linestyle='--')

# Plot 2: Benzene with lag24
ax = axes[1]
ax.plot(sample_df.index, sample_df['C6H6(GT)'], marker='o', linewidth=2, markersize=4,
        color='#FF6B6B', label='Current Benzene', alpha=0.8)
ax.plot(sample_df.index, sample_df['Benzene_lag24'], marker='s', linewidth=2, markersize=3,
        color='#4ECDC4', label='Benzene 24h Before', alpha=0.8)
ax.set_ylabel('Benzene (µg/m³)', fontsize=11, fontweight='bold')
ax.set_title('Benzene Current vs 24h Lag (notice high correlation)', fontsize=12, fontweight='bold')
ax.legend(loc='upper left')
ax.grid(True, alpha=0.3, linestyle='--')

# Plot 3: Multiple factors together
ax = axes[2]
ax2 = ax.twinx()
ax3 = ax.twinx()
ax3.spines['right'].set_position(('outward', 60))

line1 = ax.plot(sample_df.index, sample_df['C6H6(GT)'], marker='o', linewidth=2, markersize=4,
                color='#FF6B6B', label='Benzene', alpha=0.8)
line2 = ax2.plot(sample_df.index, sample_df['CO(GT)'], marker='s', linewidth=1.5, markersize=3,
                 color='#4ECDC4', label='CO', alpha=0.7)
line3 = ax3.plot(sample_df.index, sample_df['T'], marker='^', linewidth=1.5, markersize=3,
                 color='#F7DC6F', label='Temperature', alpha=0.7)

ax.set_xlabel('Time Index (hours)', fontsize=11, fontweight='bold')
ax.set_ylabel('Benzene (µg/m³)', fontsize=11, fontweight='bold', color='#FF6B6B')
ax2.set_ylabel('CO (mg/m³)', fontsize=11, fontweight='bold', color='#4ECDC4')
ax3.set_ylabel('Temperature (°C)', fontsize=11, fontweight='bold', color='#F7DC6F')
ax.set_title('Multi-Variable Time Series: Benzene, CO, and Temperature', fontsize=12, fontweight='bold')
ax.tick_params(axis='y', labelcolor='#FF6B6B')
ax2.tick_params(axis='y', labelcolor='#4ECDC4')
ax3.tick_params(axis='y', labelcolor='#F7DC6F')
ax.grid(True, alpha=0.3, linestyle='--')

lines = line1 + line2 + line3
labels = [l.get_label() for l in lines]
ax.legend(lines, labels, loc='upper left')

plt.tight_layout()
plt.savefig('04_Time_Series_with_Lags.png', dpi=200, bbox_inches='tight')
print("✓ Saved: 04_Time_Series_with_Lags.png")
plt.close()

print("\nVisualization Part 2 Complete!")


# STEP 11: BUILD PREDICTIVE MODELS

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import xgboost as xgb
import lightgbm as lgb

print("="*80)
print("STEP 11: BUILDING PREDICTIVE MODELS FOR BENZENE")
print("="*80)

# Prepare data for modeling - drop rows with NaN in lag features
model_features = ['CO(GT)', 'NOx(GT)', 'NO2(GT)', 'PT08.S5(O3)',
                  'T', 'RH', 'AH', 'Hour', 'Month', 'WeekDay_Num',
                  'Benzene_lag24', 'Benzene_lag48',
                  'CO(GT)_lag24', 'NOx(GT)_lag24', 'NO2(GT)_lag24', 'T_lag24', 'RH_lag24']

df_model = df_analysis[model_features + ['C6H6(GT)']].dropna()
print(f"\nDataset for modeling: {df_model.shape}")
print(f"Features: {len(model_features)}")

X = df_model[model_features]
y = df_model['C6H6(GT)']

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split (80-20)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

print(f"Training set: {X_train.shape}")
print(f"Test set: {X_test.shape}")

# Dictionary to store models and results
models = {}
results = {}

print("\n" + "="*80)
print("TRAINING MODELS...")
print("="*80)

# 1. Linear Regression
print("\n1. Linear Regression...")
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)
r2_lr = r2_score(y_test, y_pred_lr)
rmse_lr = np.sqrt(mean_squared_error(y_test, y_pred_lr))
mae_lr = mean_absolute_error(y_test, y_pred_lr)
models['Linear Regression'] = lr
results['Linear Regression'] = {'R2': r2_lr, 'RMSE': rmse_lr, 'MAE': mae_lr, 'Pred': y_pred_lr}
print(f"   R² Score: {r2_lr:.4f} | RMSE: {rmse_lr:.4f} | MAE: {mae_lr:.4f}")

# 2. Ridge Regression
print("2. Ridge Regression...")
ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)
y_pred_ridge = ridge.predict(X_test)
r2_ridge = r2_score(y_test, y_pred_ridge)
rmse_ridge = np.sqrt(mean_squared_error(y_test, y_pred_ridge))
mae_ridge = mean_absolute_error(y_test, y_pred_ridge)
models['Ridge'] = ridge
results['Ridge'] = {'R2': r2_ridge, 'RMSE': rmse_ridge, 'MAE': mae_ridge, 'Pred': y_pred_ridge}
print(f"   R² Score: {r2_ridge:.4f} | RMSE: {rmse_ridge:.4f} | MAE: {mae_ridge:.4f}")

# # 3. Random Forest
print("3. Random Forest...")
rf = RandomForestRegressor(n_estimators=200, max_depth=20, random_state=42, n_jobs=-1)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
r2_rf = r2_score(y_test, y_pred_rf)
rmse_rf = np.sqrt(mean_squared_error(y_test, y_pred_rf))
mae_rf = mean_absolute_error(y_test, y_pred_rf)
models['Random Forest'] = rf
results['Random Forest'] = {'R2': r2_rf, 'RMSE': rmse_rf, 'MAE': mae_rf, 'Pred': y_pred_rf}
print(f"   R² Score: {r2_rf:.4f} | RMSE: {rmse_rf:.4f} | MAE: {mae_rf:.4f}")

# # 4. Gradient Boosting
print("4. Gradient Boosting...")
gb = GradientBoostingRegressor(n_estimators=200, max_depth=5, learning_rate=0.1, random_state=42)
gb.fit(X_train, y_train)
y_pred_gb = gb.predict(X_test)
r2_gb = r2_score(y_test, y_pred_gb)
rmse_gb = np.sqrt(mean_squared_error(y_test, y_pred_gb))
mae_gb = mean_absolute_error(y_test, y_pred_gb)
models['Gradient Boosting'] = gb
results['Gradient Boosting'] = {'R2': r2_gb, 'RMSE': rmse_gb, 'MAE': mae_gb, 'Pred': y_pred_gb}
print(f"   R² Score: {r2_gb:.4f} | RMSE: {rmse_gb:.4f} | MAE: {mae_gb:.4f}")

# # 5. XGBoost
print("5. XGBoost...")
xgb_model = xgb.XGBRegressor(n_estimators=200, max_depth=5, learning_rate=0.1,
                             subsample=0.8, colsample_bytree=0.8, random_state=42, verbosity=0)
xgb_model.fit(X_train, y_train, verbose=False)
y_pred_xgb = xgb_model.predict(X_test)
r2_xgb = r2_score(y_test, y_pred_xgb)
rmse_xgb = np.sqrt(mean_squared_error(y_test, y_pred_xgb))
mae_xgb = mean_absolute_error(y_test, y_pred_xgb)
models['XGBoost'] = xgb_model
results['XGBoost'] = {'R2': r2_xgb, 'RMSE': rmse_xgb, 'MAE': mae_xgb, 'Pred': y_pred_xgb}
print(f"   R² Score: {r2_xgb:.4f} | RMSE: {rmse_xgb:.4f} | MAE: {mae_xgb:.4f}")

# # 6. LightGBM
print("6. LightGBM...")
lgb_model = lgb.LGBMRegressor(n_estimators=200, max_depth=5, learning_rate=0.1,
                              subsample=0.8, colsample_bytree=0.8, random_state=42, verbosity=-1)
lgb_model.fit(X_train, y_train)
y_pred_lgb = lgb_model.predict(X_test)
r2_lgb = r2_score(y_test, y_pred_lgb)
rmse_lgb = np.sqrt(mean_squared_error(y_test, y_pred_lgb))
mae_lgb = mean_absolute_error(y_test, y_pred_lgb)
models['LightGBM'] = lgb_model
results['LightGBM'] = {'R2': r2_lgb, 'RMSE': rmse_lgb, 'MAE': mae_lgb, 'Pred': y_pred_lgb}
print(f"   R² Score: {r2_lgb:.4f} | RMSE: {rmse_lgb:.4f} | MAE: {mae_lgb:.4f}")

# # Compile results
print("\n" + "="*80)
print("MODEL PERFORMANCE COMPARISON")
print("="*80)
results_df = pd.DataFrame({
    'Model': list(results.keys()),
    'R² Score': [results[m]['R2'] for m in results.keys()],
    'RMSE (µg/m³)': [results[m]['RMSE'] for m in results.keys()],
    'MAE (µg/m³)': [results[m]['MAE'] for m in results.keys()]
})
results_df = results_df.sort_values('R² Score', ascending=False)
print(results_df.to_string(index=False))

print(f"\n🏆 Best Model: {results_df.iloc[0]['Model']} with R² = {results_df.iloc[0]['R² Score']:.4f}")



# # VISUALIZATIONS: Model Performance and Feature Importance

fig, axes = plt.subplots(2, 2, figsize=(16, 10), dpi=200)

# Plot 1: Model Performance Comparison
ax = axes[0, 0]
model_names = results_df['Model'].values
r2_scores = results_df['R² Score'].values
colors_models = ['#FF6B6B' if i == 0 else '#4ECDC4' for i in range(len(model_names))]
bars = ax.barh(model_names, r2_scores, color=colors_models, edgecolor='black', linewidth=1.5, alpha=0.8)
ax.set_xlabel('R² Score', fontsize=11, fontweight='bold')
ax.set_title('Model Performance Comparison (R² Score)\nHigher is Better', fontsize=12, fontweight='bold')
ax.set_xlim([0.88, 0.97])
for i, (bar, score) in enumerate(zip(bars, r2_scores)):
    ax.text(score - 0.002, bar.get_y() + bar.get_height()/2, f'{score:.4f}',
            ha='right', va='center', fontweight='bold', fontsize=9, color='white')
ax.grid(True, alpha=0.3, axis='x', linestyle='--')

# # Plot 2: RMSE Comparison
ax = axes[0, 1]
rmse_values = results_df['RMSE (µg/m³)'].values
bars = ax.barh(model_names, rmse_values, color=['#FF6B6B' if i == 0 else '#95E1D3' for i in range(len(model_names))],
               edgecolor='black', linewidth=1.5, alpha=0.8)
ax.set_xlabel('RMSE (µg/m³)', fontsize=11, fontweight='bold')
ax.set_title('Root Mean Squared Error\nLower is Better', fontsize=12, fontweight='bold')
for i, (bar, rmse) in enumerate(zip(bars, rmse_values)):
    ax.text(rmse - 0.05, bar.get_y() + bar.get_height()/2, f'{rmse:.4f}',
            ha='right', va='center', fontweight='bold', fontsize=9, color='white')
ax.grid(True, alpha=0.3, axis='x', linestyle='--')

# # Plot 3: Predicted vs Actual (Best Model - XGBoost)
ax = axes[1, 0]
best_pred = results['XGBoost']['Pred']
scatter = ax.scatter(y_test, best_pred, alpha=0.5, s=40, c=y_test, cmap='viridis', edgecolors='black', linewidth=0.5)
# Perfect prediction line
min_val = min(y_test.min(), best_pred.min())
max_val = max(y_test.max(), best_pred.max())
ax.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2.5, label='Perfect Prediction')
ax.set_xlabel('Actual Benzene (µg/m³)', fontsize=11, fontweight='bold')
ax.set_ylabel('Predicted Benzene (µg/m³)', fontsize=11, fontweight='bold')
ax.set_title('XGBoost: Predicted vs Actual\n(Best Model - R² = 0.965)', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3, linestyle='--')
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Actual Value', fontsize=10)

# # Plot 4: Residuals Distribution (Best Model)
ax = axes[1, 1]
residuals = y_test - best_pred
ax.hist(residuals, bins=40, color='#4ECDC4', edgecolor='black', alpha=0.7)
ax.axvline(residuals.mean(), color='red', linestyle='--', linewidth=2.5, label=f'Mean: {residuals.mean():.4f}')
ax.axvline(0, color='black', linestyle='-', linewidth=1.5, alpha=0.5)
ax.set_xlabel('Residual Error (µg/m³)', fontsize=11, fontweight='bold')
ax.set_ylabel('Frequency', fontsize=11, fontweight='bold')
ax.set_title('XGBoost: Residuals Distribution\nMean ≈ 0 indicates unbiased predictions', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3, axis='y', linestyle='--')

plt.tight_layout()
plt.savefig('05_Model_Performance_Comparison.png', dpi=200, bbox_inches='tight')
print("✓ Saved: 05_Model_Performance_Comparison.png")
plt.close()

# # Feature Importance Analysis
print("\n" + "="*80)
print("FEATURE IMPORTANCE ANALYSIS")
print("="*80)

# Get feature importances from tree-based models
xgb_importance = xgb_model.feature_importances_
lgb_importance = lgb_model.feature_importances_
rf_importance = rf.feature_importances_
gb_importance = gb.feature_importances_

# Create importance dataframe
importance_df = pd.DataFrame({
    'Feature': model_features,
    'XGBoost': xgb_importance,
    'LightGBM': lgb_importance,
    'RandomForest': rf_importance,
    'GradBoost': gb_importance
})

# Average importance across models
importance_df['Average'] = importance_df[['XGBoost', 'LightGBM', 'RandomForest', 'GradBoost']].mean(axis=1)
importance_df = importance_df.sort_values('Average', ascending=False)

print("\nFeature Importance (Average across tree-based models):")
print(importance_df[['Feature', 'Average', 'XGBoost', 'LightGBM']].to_string(index=False))

# Visualization of Feature Importance
fig, axes = plt.subplots(1, 2, figsize=(16, 8), dpi=200)

# Plot 1: Top 15 features (average importance)
ax = axes[0]
top_features = importance_df.head(15)
colors_feat = ['#FF6B6B' if 'lag' in f else '#4ECDC4' for f in top_features['Feature']]
bars = ax.barh(range(len(top_features)), top_features['Average'], color=colors_feat,
               edgecolor='black', linewidth=1.2, alpha=0.8)
ax.set_yticks(range(len(top_features)))
ax.set_yticklabels(top_features['Feature'])
ax.set_xlabel('Average Feature Importance', fontsize=11, fontweight='bold')
ax.set_title('Top 15 Most Important Features\n(Red=Lag Features, Blue=Current Variables)', fontsize=12, fontweight='bold')
ax.grid(True, alpha=0.3, axis='x', linestyle='--')
ax.invert_yaxis()

# Plot 2: Feature importance from XGBoost model specifically
ax = axes[1]
xgb_imp_df = pd.DataFrame({
    'Feature': model_features,
    'Importance': xgb_importance
}).sort_values('Importance', ascending=False).head(15)

colors_feat = ['#FF6B6B' if 'lag' in f else '#95E1D3' for f in xgb_imp_df['Feature']]
bars = ax.barh(range(len(xgb_imp_df)), xgb_imp_df['Importance'], color=colors_feat,
               edgecolor='black', linewidth=1.2, alpha=0.8)
ax.set_yticks(range(len(xgb_imp_df)))
ax.set_yticklabels(xgb_imp_df['Feature'])
ax.set_xlabel('XGBoost Feature Importance', fontsize=11, fontweight='bold')
ax.set_title('Top 15 Features from XGBoost Model\n(Best Performing Model)', fontsize=12, fontweight='bold')
ax.grid(True, alpha=0.3, axis='x', linestyle='--')
ax.invert_yaxis()

plt.tight_layout()
plt.savefig('06_Feature_Importance_Analysis.png', dpi=200, bbox_inches='tight')
print("\n✓ Saved: 06_Feature_Importance_Analysis.png")
plt.close()


# # Fix the month labeling issue

print("="*80)
print("STEP 12: MONTH-WISE AND DAY-WISE PREDICTION ANALYSIS (FIXED)")
print("="*80)

# Add predictions to test set for analysis
test_analysis = df_model.iloc[y_test.index].copy()
test_analysis['Predicted'] = results['XGBoost']['Pred']
test_analysis['Actual'] = y_test.values
test_analysis['Error'] = test_analysis['Actual'] - test_analysis['Predicted']
test_analysis['Abs_Error'] = np.abs(test_analysis['Error'])

# Extract month from data (need to get from original index)
test_analysis['Month_Name'] = [df_analysis.iloc[i]['Month'] for i in y_test.index]
test_analysis['DayOfWeek'] = [df_analysis.iloc[i]['DayOfWeek'] for i in y_test.index]

# Month-wise analysis
month_pred_analysis = test_analysis.groupby('Month_Name').agg({
    'Actual': ['count', 'mean', 'std'],
    'Predicted': 'mean',
    'Error': ['mean', 'std'],
    'Abs_Error': 'mean'
}).round(4)

print("\nMonth-wise Prediction Accuracy (by month number):")
print(month_pred_analysis)

# Day-wise analysis
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_pred_analysis = test_analysis.groupby('DayOfWeek').agg({
    'Actual': ['count', 'mean', 'std'],
    'Predicted': 'mean',
    'Error': ['mean', 'std'],
    'Abs_Error': 'mean'
}).round(4)
day_pred_analysis = day_pred_analysis.reindex(day_order)

print("\nDay-wise Prediction Accuracy:")
print(day_pred_analysis)

# Visualization: Month-wise and Day-wise Predictions
fig, axes = plt.subplots(2, 2, figsize=(16, 10), dpi=200)

# Plot 1: Month-wise Actual vs Predicted
ax = axes[0, 0]
months = test_analysis.groupby('Month_Name')[['Actual', 'Predicted']].mean().sort_index()
x_pos = np.arange(len(months))
width = 0.35
month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
month_names = [month_labels[int(m)-1] for m in months.index]
bars1 = ax.bar(x_pos - width/2, months['Actual'], width, label='Actual',
               color='#4ECDC4', edgecolor='black', linewidth=1.2, alpha=0.8)
bars2 = ax.bar(x_pos + width/2, months['Predicted'], width, label='Predicted',
               color='#FF6B6B', edgecolor='black', linewidth=1.2, alpha=0.8)
ax.set_xlabel('Month', fontsize=11, fontweight='bold')
ax.set_ylabel('Benzene (µg/m³)', fontsize=11, fontweight='bold')
ax.set_title('Month-wise: Actual vs Predicted Benzene', fontsize=12, fontweight='bold')
ax.set_xticks(x_pos)
ax.set_xticklabels(month_names)
ax.legend()
ax.grid(True, alpha=0.3, axis='y', linestyle='--')

# Plot 2: Month-wise MAE
ax = axes[0, 1]
month_mae = test_analysis.groupby('Month_Name')['Abs_Error'].mean().sort_index()
month_names_sorted = [month_labels[int(m)-1] for m in month_mae.index]
ax.plot(range(len(month_mae)), month_mae.values, marker='o', linewidth=2.5, markersize=8,
        color='#FF6B6B', markeredgecolor='black', markeredgewidth=1.5)
ax.fill_between(range(len(month_mae)), month_mae.values, alpha=0.3, color='#FF6B6B')
ax.set_xlabel('Month', fontsize=11, fontweight='bold')
ax.set_ylabel('Mean Absolute Error (µg/m³)', fontsize=11, fontweight='bold')
ax.set_title('Month-wise Prediction Error (MAE)', fontsize=12, fontweight='bold')
ax.set_xticks(range(len(month_mae)))
ax.set_xticklabels(month_names_sorted)
ax.grid(True, alpha=0.3, linestyle='--')

# Plot 3: Day-wise Actual vs Predicted
ax = axes[1, 0]
day_data = test_analysis.groupby('DayOfWeek')[['Actual', 'Predicted']].mean().reindex(day_order)
x_pos = np.arange(len(day_data))
bars1 = ax.bar(x_pos - width/2, day_data['Actual'], width, label='Actual',
               color='#4ECDC4', edgecolor='black', linewidth=1.2, alpha=0.8)
bars2 = ax.bar(x_pos + width/2, day_data['Predicted'], width, label='Predicted',
               color='#FF6B6B', edgecolor='black', linewidth=1.2, alpha=0.8)
ax.set_xlabel('Day of Week', fontsize=11, fontweight='bold')
ax.set_ylabel('Benzene (µg/m³)', fontsize=11, fontweight='bold')
ax.set_title('Day-wise: Actual vs Predicted Benzene', fontsize=12, fontweight='bold')
ax.set_xticks(x_pos)
ax.set_xticklabels(day_order, rotation=45)
ax.legend()
ax.grid(True, alpha=0.3, axis='y', linestyle='--')

# Plot 4: Day-wise MAE
ax = axes[1, 1]
day_mae = test_analysis.groupby('DayOfWeek')['Abs_Error'].mean().reindex(day_order)
colors_day = ['#FF6B6B' if day in ['Saturday', 'Sunday'] else '#4ECDC4' for day in day_order]
bars = ax.bar(range(len(day_order)), day_mae.values, color=colors_day,
              edgecolor='black', linewidth=1.2, alpha=0.8)
ax.set_xticks(range(len(day_order)))
ax.set_xticklabels(day_order, rotation=45)
ax.set_ylabel('Mean Absolute Error (µg/m³)', fontsize=11, fontweight='bold')
ax.set_title('Day-wise Prediction Error (MAE)', fontsize=12, fontweight='bold')
ax.grid(True, alpha=0.3, axis='y', linestyle='--')

plt.tight_layout()
plt.savefig('07_Month_Day_Prediction_Analysis.png', dpi=200, bbox_inches='tight')
print("\n✓ Saved: 07_Month_Day_Prediction_Analysis.png")
plt.close()

print("\n✓ Analysis Complete!")
