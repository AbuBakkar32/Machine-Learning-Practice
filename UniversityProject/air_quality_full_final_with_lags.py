"""
================================================================================
FULL AIR QUALITY PROJECT (ALL VISUALIZATIONS + LAGS + MODEL COMPARISON + EXPLAIN)
Benzene (C6H6) Concentration Analysis and Prediction (UCI Air Quality)
================================================================================
Author: ABU BAKKAR SIDDIKK
Refactor/Upgrade: ChatGPT
Date: February 14, 2026
Course: Statistical Inference and Learning
Dataset: Air Quality UCI (March 2004 - February 2005)
================================================================================

WHAT'S INSIDE (Everything in one file):
A) Load + Cleaning (once, no repetition)
B) Feature engineering (DateTime, Hour/Month/DayOfWeek, Season)
C) ALL your original Visualizations (kept, grouped logically):
   1) Distribution
   2) Correlation heatmap
   3) Daily benzene time-series
   4) Hourly pattern
   5) Seasonal pattern
   6) Benzene vs CO
   7) Benzene vs Temperature
   8) Monthly box plot
   9) Day-of-week pattern
   10) Multi-pollutant normalized hourly patterns
   11) Benzene vs PT08.S1 (CO sensor)
   12) Benzene vs RH (colored by temp)
   13) Feature importance (correlation with target)
   14) Model performance comparison (CV + holdout)
   15) Actual vs Predicted (best model)
   16) Residual plot (best model)
   + Additional from your big script:
      - Heatmap (Hour x Day)
      - Weekday vs Weekend comparison tables + plot
      - Intervention scenario plot
      - Monthly normalized patterns (Benzene vs CO vs NOx vs Temp)
      - Seasonal box + seasonal stats table
      - Weather category normalized bars + detailed table
      - Humidity bins bar + table
      - Temperature bins bar + table
      - 3D plot (T, RH, Benzene)
      - Coefficient plots for linear models (optional)
D) NEW additions:
   - Lag features (1h/24h/48h), rolling (24h/48h), driver lags
   - Lag relationship visuals
   - Model comparison: BASE vs BASE+LAGS (TimeSeriesSplit CV)
   - Best model auto-select + holdout evaluation
   - Permutation importance (holdout) + plot
   - Partial Dependence Plots (top 3 raw numeric features)

RUN:
  pip install pandas numpy plotly scikit-learn joblib
  pip install -U kaleido    # optional for PNG export
  python air_quality_full_project_FINAL.py

OUTPUTS:
  outputs_airquality_full_project/
    - all plots: .html (+ .png if kaleido)
    - tables: .csv
    - best model: .joblib (if joblib installed)
================================================================================
"""

# =============================================================================
# 0) IMPORTS
# =============================================================================
import os
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

from dataclasses import dataclass
from typing import Dict, List, Tuple

from sklearn.model_selection import TimeSeriesSplit, cross_validate
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder, PolynomialFeatures
from sklearn.impute import SimpleImputer

from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.inspection import permutation_importance, partial_dependence

try:
    import joblib
    HAS_JOBLIB = True
except Exception:
    HAS_JOBLIB = False


# =============================================================================
# 1) CONFIG
# =============================================================================
@dataclass
class Config:
    data_path: str = "AirQualityUCI.csv"
    sep: str = ","
    decimal: str = "."
    invalid_value: int = -200
    drop_col: str = "NMHC_GT"

    date_col: str = "Date"
    time_col: str = "Time"
    target: str = "C6H6_GT"

    out_dir: str = "outputs_airquality_full_project"
    show_plots: bool = True
    save_html: bool = False
    save_png_if_possible: bool = True  # kaleido required

    # modeling
    holdout_ratio: float = 0.20
    n_splits_cv: int = 5
    random_state: int = 42

    # Base model features
    base_numeric_features: Tuple[str, ...] = (
        "CO_GT", "PT08_S1_CO", "PT08_S2_NMHC", "NOx_GT", "PT08_S3_NOx",
        "NO2_GT", "PT08_S4_NO2", "PT08_S5_O3", "T", "RH", "AH",
        "Hour", "DayOfWeek", "Month"
    )
    categorical_features: Tuple[str, ...] = ("Season",)

    # polynomial subset for linear models
    poly_subset: Tuple[str, ...] = ("CO_GT", "PT08_S1_CO", "NOx_GT")

    # Lag features
    lag_hours: Tuple[int, ...] = (1, 24, 48)
    roll_windows: Tuple[int, ...] = (24, 48)

    # Explainability
    perm_repeats: int = 10
    perm_scoring: str = "r2"
    perm_top_k: int = 20

    # PDP
    pdp_top_n: int = 3
    pdp_grid_resolution: int = 30


CFG = Config()


# =============================================================================
# 2) HELPERS
# =============================================================================
def banner(title: str) -> None:
    print("\n" + "=" * 90)
    print(title)
    print("=" * 90)

def ensure_out_dir(cfg: Config) -> None:
    os.makedirs(cfg.out_dir, exist_ok=True)

def try_save_plot(fig, cfg: Config, name: str) -> None:
    ensure_out_dir(cfg)
    if cfg.save_html:
        fig.write_html(os.path.join(cfg.out_dir, f"{name}.html"))
    if cfg.save_png_if_possible:
        try:
            fig.write_image(os.path.join(cfg.out_dir, f"{name}.png"), scale=2)
        except Exception:
            # PNG export requires kaleido
            pass

def get_season(month: int) -> str:
    if month in (12, 1, 2):
        return "Winter"
    if month in (3, 4, 5):
        return "Spring"
    if month in (6, 7, 8):
        return "Summer"
    return "Autumn"


# =============================================================================
# 3) LOAD + CLEAN + FEATURE ENGINEERING (ONCE)
# =============================================================================
def load_raw(cfg: Config) -> pd.DataFrame:
    banner("STEP 1: LOAD RAW DATA")
    df = pd.read_csv(cfg.data_path, sep=cfg.sep, decimal=cfg.decimal)
    print(f"Raw shape: {df.shape}")
    print("Columns:", df.columns.tolist())
    return df

def clean_engineer(df: pd.DataFrame, cfg: Config) -> pd.DataFrame:
    banner("STEP 2: CLEAN + FEATURE ENGINEERING (ONCE)")

    dfc = df.copy()
    # Sanitize columns to match what the script expects (underscores instead of dots/parens)
    dfc.columns = [c.replace(".", "_").replace("(", "_").replace(")", "").replace("-", "_") for c in dfc.columns]

    # Drop NMHC_GT if exists
    if cfg.drop_col in dfc.columns:
        dfc = dfc.drop(columns=[cfg.drop_col])

    # Replace invalid_value with NaN for numeric columns
    num_cols = dfc.select_dtypes(include=[np.number]).columns
    dfc[num_cols] = dfc[num_cols].replace(cfg.invalid_value, np.nan)

    # Drop rows missing target
    dfc = dfc.dropna(subset=[cfg.target])
    print(dfc.head())

    # Create DateTime
    dfc["DateTime"] = pd.to_datetime(
        dfc[cfg.date_col].astype(str) + " " + dfc[cfg.time_col].astype(str),
        errors="coerce"
    )
    dfc = dfc.dropna(subset=["DateTime"])

    # Sort by time (critical)
    dfc = dfc.sort_values("DateTime").reset_index(drop=True)

    # Time features
    dfc["Year"] = dfc["DateTime"].dt.year
    dfc["Month"] = dfc["DateTime"].dt.month
    dfc["Day"] = dfc["DateTime"].dt.day
    dfc["Hour"] = dfc["DateTime"].dt.hour
    dfc["DayOfWeek"] = dfc["DateTime"].dt.dayofweek
    dfc["IsWeekend"] = (dfc["DayOfWeek"] >= 5).astype(int)
    dfc["Season"] = dfc["Month"].apply(get_season)

    print(f"Cleaned shape: {dfc.shape}")
    miss = (dfc.isna().mean() * 100).sort_values(ascending=False).head(12).round(2)
    print("Top missing % after cleaning:")
    print(miss.to_string())

    return dfc


# =============================================================================
# 4) LAG + ROLLING FEATURES (NEW, leak-free)
# =============================================================================
def add_lag_features(d: pd.DataFrame, cfg: Config) -> pd.DataFrame:
    banner("STEP 3: ADD LAG + ROLLING FEATURES (Leak-free)")
    df = d.copy()

    # Target lags
    for h in cfg.lag_hours:
        df[f"{cfg.target}_lag_{h}h"] = df[cfg.target].shift(h)

    # Rolling stats (shifted by 1 to ensure past-only)
    for w in cfg.roll_windows:
        df[f"{cfg.target}_rollmean_{w}h"] = df[cfg.target].rolling(window=w, min_periods=w).mean().shift(1)
        df[f"{cfg.target}_rollstd_{w}h"] = df[cfg.target].rolling(window=w, min_periods=w).std().shift(1)

    # Lag some drivers (common traffic indicators)
    driver_cols = ["CO_GT", "NOx_GT", "PT08_S2_NMHC"]
    for col in driver_cols:
        if col in df.columns:
            df[f"{col}_lag_24h"] = df[col].shift(24)
            df[f"{col}_rollmean_24h"] = df[col].rolling(window=24, min_periods=24).mean().shift(1)

    new_cols = [c for c in df.columns if ("lag_" in c or "roll" in c)]
    print(f"Added lag/rolling columns: {len(new_cols)}")
    print("Example new columns:", new_cols[:12])

    return df


# =============================================================================
# 5) VISUALIZATIONS: ALL ORIGINAL + NEW ONES
# =============================================================================
def viz_all(d: pd.DataFrame, cfg: Config) -> None:
    """
    Contains ALL visualizations from your script (kept) + a few extra helpful ones.
    Uses the cleaned data d (no repeated cleaning).
    """
    banner("STEP 4: RUN ALL VISUALIZATIONS (FULL SET)")

    # -------------------------
    # VIZ 1: Benzene Distribution
    # -------------------------
    fig = px.histogram(d, x=cfg.target, nbins=50,
                       title="VIZ 1 — Distribution of Benzene (C6H6)",
                       labels={cfg.target: "Benzene (µg/m³)"})
    fig.update_layout(height=420, showlegend=False)
    try_save_plot(fig, cfg, "viz_01_benzene_distribution")
    if cfg.show_plots: fig.show()

    # -------------------------
    # VIZ 2: Correlation Heatmap
    # -------------------------
    pollutant_cols = [
        "C6H6_GT", "CO_GT", "NOx_GT", "NO2_GT",
        "PT08_S1_CO", "PT08_S2_NMHC", "PT08_S3_NOx", "PT08_S4_NO2", "PT08_S5_O3",
        "T", "RH", "AH"
    ]
    cols = [c for c in pollutant_cols if c in d.columns]
    corr = d[cols].dropna().corr()
    fig = px.imshow(corr, zmin=-1, zmax=1, color_continuous_scale="RdBu_r",
                    title="VIZ 2 — Correlation Matrix of Air Quality Variables")
    fig.update_layout(height=650, width=850)
    try_save_plot(fig, cfg, "viz_02_corr_heatmap")
    if cfg.show_plots: fig.show()

    # -------------------------
    # VIZ 3: Benzene Daily Time Series
    # -------------------------
    daily = d.groupby(d["DateTime"].dt.date)[cfg.target].mean().reset_index()
    daily.columns = ["Date", "Avg_C6H6"]
    fig = px.line(daily, x="Date", y="Avg_C6H6",
                  title="VIZ 3 — Daily Average Benzene Over Time",
                  labels={"Avg_C6H6": "Avg Benzene (µg/m³)"})
    fig.update_layout(height=420)
    try_save_plot(fig, cfg, "viz_03_daily_timeseries")
    if cfg.show_plots: fig.show()

    # -------------------------
    # VIZ 4: Hourly Benzene Pattern
    # -------------------------
    hourly_avg = d.groupby("Hour")[cfg.target].mean().reset_index()
    fig = px.bar(hourly_avg, x="Hour", y=cfg.target, color=cfg.target,
                 title="VIZ 4 — Average Benzene by Hour of Day",
                 color_continuous_scale="Reds")
    fig.update_layout(height=420, showlegend=False)
    try_save_plot(fig, cfg, "viz_04_hourly_benzene")
    if cfg.show_plots: fig.show()

    # -------------------------
    # VIZ 5: Seasonal Benzene Pattern
    # -------------------------
    season_order = ["Spring", "Summer", "Autumn", "Winter"]
    seasonal = d.groupby("Season")[cfg.target].mean().reindex(season_order).reset_index()
    fig = px.bar(seasonal, x="Season", y=cfg.target, color=cfg.target,
                 title="VIZ 5 — Average Benzene by Season",
                 color_continuous_scale="Viridis")
    fig.update_layout(height=420, showlegend=False)
    try_save_plot(fig, cfg, "viz_05_seasonal_benzene")
    if cfg.show_plots: fig.show()

    # -------------------------
    # VIZ 6: Benzene vs CO
    # -------------------------
    if "CO_GT" in d.columns:
        dd = d.dropna(subset=["CO_GT", cfg.target])
        fig = px.scatter(dd, x="CO_GT", y=cfg.target, opacity=0.55,
                         title="VIZ 6 — Benzene vs Carbon Monoxide (CO)",
                         labels={"CO_GT": "CO (mg/m³)", cfg.target: "Benzene (µg/m³)"})
        fig.update_layout(height=420)
        try_save_plot(fig, cfg, "viz_06_benzene_vs_co")
        if cfg.show_plots: fig.show()

    # -------------------------
    # VIZ 7: Benzene vs Temperature
    # -------------------------
    if "T" in d.columns:
        dd = d.dropna(subset=["T", cfg.target])
        fig = px.scatter(dd, x="T", y=cfg.target, opacity=0.55,
                         title="VIZ 7 — Benzene vs Temperature",
                         labels={"T": "Temp (°C)", cfg.target: "Benzene (µg/m³)"})
        fig.update_layout(height=420)
        try_save_plot(fig, cfg, "viz_07_benzene_vs_temp")
        if cfg.show_plots: fig.show()

    # -------------------------
    # VIZ 8: Monthly Box Plot
    # -------------------------
    month_names = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    dd = d.dropna(subset=[cfg.target, "Month"]).copy()
    dd["Month_Name"] = dd["Month"].apply(lambda x: month_names[x-1])
    fig = px.box(dd, x="Month_Name", y=cfg.target, color="Month_Name",
                 category_orders={"Month_Name": month_names},
                 title="VIZ 8 — Benzene Distribution by Month")
    fig.update_layout(height=420, showlegend=False)
    try_save_plot(fig, cfg, "viz_08_monthly_box")
    if cfg.show_plots: fig.show()

    # -------------------------
    # VIZ 9: Day-of-week Pattern
    # -------------------------
    day_names = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    dd = d.dropna(subset=[cfg.target, "DayOfWeek"]).copy()
    dd["Day_Name"] = dd["DayOfWeek"].apply(lambda x: day_names[x])
    weekday_avg = dd.groupby("Day_Name")[cfg.target].mean().reindex(day_names).reset_index()
    weekday_avg.columns = ["Day", "Avg_C6H6"]
    fig = px.bar(weekday_avg, x="Day", y="Avg_C6H6", color="Avg_C6H6",
                 title="VIZ 9 — Average Benzene by Day of Week",
                 color_continuous_scale="Blues")
    fig.update_layout(height=420, showlegend=False)
    try_save_plot(fig, cfg, "viz_09_dayofweek")
    if cfg.show_plots: fig.show()

    # -------------------------
    # VIZ 10: Multi-Pollutant Normalized Hourly Patterns
    # -------------------------
    needed = [cfg.target, "CO_GT", "NOx_GT", "NO2_GT", "Hour"]
    if all(c in d.columns for c in needed):
        hp = d.dropna(subset=needed).groupby("Hour")[[cfg.target,"CO_GT","NOx_GT","NO2_GT"]].mean().reset_index()
        for c in [cfg.target,"CO_GT","NOx_GT","NO2_GT"]:
            hp[c+"_n"] = (hp[c]-hp[c].min())/(hp[c].max()-hp[c].min()+1e-12)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=hp["Hour"], y=hp[cfg.target+"_n"], mode="lines+markers", name="Benzene"))
        fig.add_trace(go.Scatter(x=hp["Hour"], y=hp["CO_GT_n"], mode="lines+markers", name="CO"))
        fig.add_trace(go.Scatter(x=hp["Hour"], y=hp["NOx_GT_n"], mode="lines+markers", name="NOx"))
        fig.add_trace(go.Scatter(x=hp["Hour"], y=hp["NO2_GT_n"], mode="lines+markers", name="NO2"))
        fig.update_layout(title="VIZ 10 — Normalized Hourly Patterns (Benzene/CO/NOx/NO2)", height=450)
        try_save_plot(fig, cfg, "viz_10_multi_pollutant_hourly_norm")
        if cfg.show_plots: fig.show()

    # -------------------------
    # VIZ 11: Benzene vs PT08_S1_CO
    # -------------------------
    if "PT08_S1_CO" in d.columns:
        dd = d.dropna(subset=["PT08_S1_CO", cfg.target])
        fig = px.scatter(dd, x="PT08_S1_CO", y=cfg.target, opacity=0.55,
                         title="VIZ 11 — Benzene vs CO Sensor Response (PT08.S1)")
        fig.update_layout(height=420)
        try_save_plot(fig, cfg, "viz_11_benzene_vs_pt08s1")
        if cfg.show_plots: fig.show()

    # -------------------------
    # VIZ 12: Benzene vs RH color Temp
    # -------------------------
    if all(c in d.columns for c in ["RH","T",cfg.target]):
        dd = d.dropna(subset=["RH","T",cfg.target])
        fig = px.scatter(dd, x="RH", y=cfg.target, color="T",
                         title="VIZ 12 — Benzene vs Relative Humidity (colored by Temperature)",
                         opacity=0.55, color_continuous_scale="Turbo")
        fig.update_layout(height=420)
        try_save_plot(fig, cfg, "viz_12_benzene_vs_rh_tempcolor")
        if cfg.show_plots: fig.show()

    # -------------------------
    # VIZ 13: Feature Importance (Correlation with Target)
    # -------------------------
    feature_cols = [
        "CO_GT","PT08_S1_CO","PT08_S2_NMHC","NOx_GT","PT08_S3_NOx",
        "NO2_GT","PT08_S4_NO2","PT08_S5_O3","T","RH","AH"
    ]
    feat_avail = [c for c in feature_cols if c in d.columns]
    rows = []
    for c in feat_avail:
        tmp = d[[cfg.target, c]].dropna()
        if len(tmp) > 10:
            corr_val = tmp.corr().iloc[0,1]
            rows.append({"Feature": c, "Correlation": corr_val, "Abs_Correlation": abs(corr_val)})
    if rows:
        corr_df = pd.DataFrame(rows).sort_values("Abs_Correlation", ascending=False)
        fig = px.bar(corr_df, x="Correlation", y="Feature", orientation="h",
                     title="VIZ 13 — Feature Importance (Correlation with Benzene)",
                     color="Correlation", color_continuous_scale="RdBu_r",
                     color_continuous_midpoint=0)
        fig.update_layout(height=520)
        try_save_plot(fig, cfg, "viz_13_feature_importance_corr")
        if cfg.show_plots: fig.show()

    # -------------------------
    # Extra: Heatmap Hour x Day
    # -------------------------
    if all(c in d.columns for c in [cfg.target,"Hour","DayOfWeek"]):
        dd = d.dropna(subset=[cfg.target,"Hour","DayOfWeek"]).copy()
        dd["Day_Name"] = dd["DayOfWeek"].apply(lambda x: day_names[x])
        heat = dd.pivot_table(values=cfg.target, index="Day_Name", columns="Hour", aggfunc="mean").reindex(day_names)
        fig = px.imshow(heat, aspect="auto", color_continuous_scale="YlOrRd",
                        title="Extra — Benzene Heatmap: Hour vs Day of Week",
                        labels=dict(x="Hour", y="Day", color="Benzene"))
        fig.update_layout(height=520)
        try_save_plot(fig, cfg, "viz_extra_heatmap_hour_day")
        if cfg.show_plots: fig.show()

    # -------------------------
    # Extra: Weekday vs Weekend Hourly
    # -------------------------
    if all(c in d.columns for c in [cfg.target,"Hour","DayOfWeek"]):
        dd = d.dropna(subset=[cfg.target,"Hour","DayOfWeek"]).copy()
        dd["Day_Type"] = dd["DayOfWeek"].apply(lambda x: "Weekend" if x >= 5 else "Weekday")
        hw = dd.groupby(["Hour","Day_Type"])[cfg.target].mean().reset_index()
        fig = px.line(hw, x="Hour", y=cfg.target, color="Day_Type", markers=True,
                      title="Extra — Hourly Benzene: Weekday vs Weekend")
        fig.update_layout(height=480, legend=dict(orientation="h", y=1.12))
        try_save_plot(fig, cfg, "viz_extra_weekday_weekend_hourly")
        if cfg.show_plots: fig.show()

        # Simple comparison table
        comp = dd.groupby("Day_Type").agg({
            cfg.target:"mean","CO_GT":"mean","NOx_GT":"mean","NO2_GT":"mean","T":"mean"
        }).round(3)
        comp.to_csv(os.path.join(cfg.out_dir, "table_weekday_weekend_means.csv"))

    # -------------------------
    # Extra: Intervention Scenario (rush hour reductions)
    # -------------------------
    if all(c in d.columns for c in [cfg.target,"Hour","DayOfWeek"]):
        dd = d.dropna(subset=[cfg.target,"Hour","DayOfWeek"]).copy()
        dd["Day_Type"] = dd["DayOfWeek"].apply(lambda x: "Weekend" if x >= 5 else "Weekday")
        weekday_hourly = dd[dd["Day_Type"]=="Weekday"].groupby("Hour")[cfg.target].mean().reindex(range(24)).values

        peak_hours = [7,8,9,17,18,19,20]
        current = weekday_hourly.copy()
        intervention_20 = weekday_hourly.copy()
        intervention_50 = weekday_hourly.copy()
        for h in peak_hours:
            intervention_20[h] = current[h]*0.8
            intervention_50[h] = current[h]*0.5

        hours = list(range(24))
        scen = pd.DataFrame({
            "Hour": hours*3,
            "Benzene": list(current)+list(intervention_20)+list(intervention_50),
            "Scenario": ["Current Baseline"]*24 + ["20% Traffic Reduction"]*24 + ["50% Traffic Reduction"]*24
        })
        fig = px.line(scen, x="Hour", y="Benzene", color="Scenario", markers=True,
                      title="Extra — Intervention Impact on Benzene (Rush Hour Reduction)")
        for x0, x1 in [(7,10),(17,21)]:
            fig.add_vrect(x0=x0, x1=x1, fillcolor="lightgray", opacity=0.2, layer="below", line_width=0)
        fig.update_layout(height=480)
        try_save_plot(fig, cfg, "viz_extra_intervention_scenarios")
        if cfg.show_plots: fig.show()

    # -------------------------
    # Extra: Monthly normalized patterns (Benzene vs CO vs NOx vs Temp)
    # -------------------------
    if all(c in d.columns for c in [cfg.target,"CO_GT","NOx_GT","T","Month"]):
        m = d.dropna(subset=[cfg.target,"CO_GT","NOx_GT","T","Month"]).groupby("Month").agg({
            cfg.target:"mean","CO_GT":"mean","NOx_GT":"mean","T":"mean"
        }).reset_index()
        m["Month_Name"] = m["Month"].apply(lambda x: month_names[x-1])
        m["Benzene_Pct"] = m[cfg.target]/m[cfg.target].max()*100
        m["CO_Pct"] = m["CO_GT"]/m["CO_GT"].max()*100
        m["NOx_Pct"] = m["NOx_GT"]/m["NOx_GT"].max()*100
        m["Temp_Pct"] = m["T"]/m["T"].max()*100

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=m["Month_Name"], y=m["Benzene_Pct"], mode="lines+markers", name="Benzene"))
        fig.add_trace(go.Scatter(x=m["Month_Name"], y=m["CO_Pct"], mode="lines+markers", name="CO", line=dict(dash="dash")))
        fig.add_trace(go.Scatter(x=m["Month_Name"], y=m["NOx_Pct"], mode="lines+markers", name="NOx", line=dict(dash="dash")))
        fig.add_trace(go.Scatter(x=m["Month_Name"], y=m["Temp_Pct"], mode="lines+markers", name="Temp", line=dict(dash="dot")))
        fig.update_layout(title="Extra — Monthly Patterns (Normalized % of Max)", height=520, hovermode="x unified")
        try_save_plot(fig, cfg, "viz_extra_monthly_normalized_patterns")
        if cfg.show_plots: fig.show()

    # -------------------------
    # Extra: Weather category analysis + normalized bars
    # -------------------------
    if all(c in d.columns for c in [cfg.target,"CO_GT","NOx_GT","NO2_GT","T","RH"]):
        dd = d.dropna(subset=[cfg.target,"CO_GT","NOx_GT","NO2_GT","T","RH"]).copy()
        dd["Weather_Category"] = "Unknown"
        dd.loc[(dd["T"] < 15) & (dd["RH"] >= 60), "Weather_Category"] = "Cold & Humid"
        dd.loc[(dd["T"] < 15) & (dd["RH"] < 60),  "Weather_Category"] = "Cold & Dry"
        dd.loc[(dd["T"] >= 15) & (dd["RH"] >= 60), "Weather_Category"] = "Warm & Humid"
        dd.loc[(dd["T"] >= 15) & (dd["RH"] < 60),  "Weather_Category"] = "Warm & Dry"

        ws = dd.groupby("Weather_Category").agg({
            cfg.target:["mean","std","count"],
            "T":"mean","RH":"mean","CO_GT":"mean","NOx_GT":"mean","NO2_GT":"mean"
        }).round(2)
        ws.columns = ["Benzene_Mean","Benzene_Std","Count","Avg_T","Avg_RH","Avg_CO","Avg_NOx","Avg_NO2"]
        ws = ws.reset_index()
        ws.to_csv(os.path.join(cfg.out_dir, "table_weather_category_details.csv"), index=False)

        # normalized grouped bars
        norm = dd.groupby("Weather_Category").agg({cfg.target:"mean","CO_GT":"mean","NOx_GT":"mean"}).reset_index()
        norm["Benzene_Norm"] = norm[cfg.target]/norm[cfg.target].max()*100
        norm["CO_Norm"] = norm["CO_GT"]/norm["CO_GT"].max()*100
        norm["NOx_Norm"] = norm["NOx_GT"]/norm["NOx_GT"].max()*100

        plot_rows = []
        for _, r in norm.iterrows():
            plot_rows += [
                {"Weather": r["Weather_Category"], "Pollutant":"Benzene", "Value": r["Benzene_Norm"]},
                {"Weather": r["Weather_Category"], "Pollutant":"CO", "Value": r["CO_Norm"]},
                {"Weather": r["Weather_Category"], "Pollutant":"NOx","Value": r["NOx_Norm"]},
            ]
        plot_df = pd.DataFrame(plot_rows)

        fig = px.bar(plot_df, x="Weather", y="Value", color="Pollutant", barmode="group",
                     title="Extra — Normalized Pollutants by Weather Category (% of Max)")
        fig.update_layout(height=520)
        try_save_plot(fig, cfg, "viz_extra_weather_category_normalized")
        if cfg.show_plots: fig.show()

    # -------------------------
    # Extra: Humidity bins (bar) + table
    # -------------------------
    if all(c in d.columns for c in [cfg.target,"RH","T","CO_GT","NOx_GT"]):
        dd = d.dropna(subset=[cfg.target,"RH","T","CO_GT","NOx_GT"]).copy()
        dd["RH_Bin"] = pd.cut(dd["RH"],
                              bins=[0,20,30,40,50,60,70,100],
                              labels=["<20%","20-30%","30-40%","40-50%","50-60%","60-70%",">70%"])
        rh_viz = dd.groupby("RH_Bin")[cfg.target].mean().reset_index()
        fig = px.bar(rh_viz, x="RH_Bin", y=cfg.target, color=cfg.target,
                     title="Extra — Average Benzene by Humidity Range",
                     color_continuous_scale="Blues")
        fig.update_layout(height=450, showlegend=False)
        try_save_plot(fig, cfg, "viz_extra_humidity_bins")
        if cfg.show_plots: fig.show()

        rh_tbl = dd.groupby("RH_Bin").agg({
            cfg.target:["mean","std","count"],
            "T":"mean","CO_GT":"mean","NOx_GT":"mean"
        }).round(2)
        rh_tbl.columns = ["Benzene_Mean","Benzene_Std","Count","Avg_T","Avg_CO","Avg_NOx"]
        rh_tbl.reset_index().to_csv(os.path.join(cfg.out_dir, "table_humidity_bins.csv"), index=False)

    # -------------------------
    # Extra: Temperature bins (bar) + table
    # -------------------------
    if all(c in d.columns for c in [cfg.target,"T","RH","CO_GT","NOx_GT"]):
        dd = d.dropna(subset=[cfg.target,"T","RH","CO_GT","NOx_GT"]).copy()
        dd["Temp_Bin"] = pd.cut(dd["T"],
                                bins=[-5,5,10,15,20,25,30,50],
                                labels=["<5°C","5-10°C","10-15°C","15-20°C","20-25°C","25-30°C",">30°C"])
        temp_viz = dd.groupby("Temp_Bin")[cfg.target].mean().reset_index()
        fig = px.bar(temp_viz, x="Temp_Bin", y=cfg.target, color=cfg.target,
                     title="Extra — Average Benzene by Temperature Range",
                     color_continuous_scale="RdYlBu_r")
        fig.update_layout(height=450, showlegend=False)
        try_save_plot(fig, cfg, "viz_extra_temperature_bins")
        if cfg.show_plots: fig.show()

        temp_tbl = dd.groupby("Temp_Bin").agg({
            cfg.target:["mean","std","count"],
            "CO_GT":"mean","NOx_GT":"mean","RH":"mean"
        }).round(2)
        temp_tbl.columns = ["Benzene_Mean","Benzene_Std","Count","Avg_CO","Avg_NOx","Avg_RH"]
        temp_tbl.reset_index().to_csv(os.path.join(cfg.out_dir, "table_temperature_bins.csv"), index=False)

    # -------------------------
    # Extra: 3D Benzene vs T & RH
    # -------------------------
    if all(c in d.columns for c in [cfg.target,"T","RH"]):
        dd = d.dropna(subset=[cfg.target,"T","RH"]).iloc[::5].copy()
        fig = px.scatter_3d(dd, x="T", y="RH", z=cfg.target, color=cfg.target,
                            title="Extra — 3D: Benzene vs Temperature and Humidity",
                            opacity=0.6, color_continuous_scale="Viridis")
        fig.update_layout(height=650)
        try_save_plot(fig, cfg, "viz_extra_3d_temp_rh_benzene")
        if cfg.show_plots: fig.show()


# =============================================================================
# 6) MODELING: PREPROCESSORS + MODELS
# =============================================================================
def build_preprocessor_scaled(cfg: Config, df_ref: pd.DataFrame, numeric_features: List[str]) -> ColumnTransformer:
    num_all = [c for c in numeric_features if c in df_ref.columns]
    cat_all = [c for c in cfg.categorical_features if c in df_ref.columns]

    poly = [c for c in cfg.poly_subset if c in num_all]
    other_num = [c for c in num_all if c not in poly]

    poly_pipe = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
        ("poly", PolynomialFeatures(degree=2, include_bias=False))
    ])
    num_pipe = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])
    cat_pipe = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore"))
    ])

    return ColumnTransformer(
        transformers=[
            ("poly_num", poly_pipe, poly),
            ("num", num_pipe, other_num),
            ("cat", cat_pipe, cat_all),
        ],
        remainder="drop"
    )

def build_preprocessor_tree(cfg: Config, df_ref: pd.DataFrame, numeric_features: List[str]) -> ColumnTransformer:
    num_all = [c for c in numeric_features if c in df_ref.columns]
    cat_all = [c for c in cfg.categorical_features if c in df_ref.columns]

    num_pipe = Pipeline(steps=[("imputer", SimpleImputer(strategy="median"))])
    cat_pipe = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore"))
    ])

    return ColumnTransformer(
        transformers=[
            ("num", num_pipe, num_all),
            ("cat", cat_pipe, cat_all),
        ],
        remainder="drop"
    )

def get_models(cfg: Config) -> Dict[str, object]:
    return {
        "LinearRegression": LinearRegression(),
        "Ridge(alpha=1.0)": Ridge(alpha=1.0, random_state=cfg.random_state),
        "Ridge(alpha=10.0)": Ridge(alpha=10.0, random_state=cfg.random_state),
        "Lasso(alpha=0.001)": Lasso(alpha=0.001, random_state=cfg.random_state, max_iter=10000),
        "ElasticNet(a=0.001,l1=0.5)": ElasticNet(alpha=0.001, l1_ratio=0.5, random_state=cfg.random_state, max_iter=10000),
        "RandomForest": RandomForestRegressor(
            n_estimators=300, random_state=cfg.random_state, n_jobs=-1, min_samples_leaf=2
        ),
        "GradientBoosting": GradientBoostingRegressor(random_state=cfg.random_state),
    }

def time_holdout_split(d: pd.DataFrame, cfg: Config) -> Tuple[pd.DataFrame, pd.DataFrame]:
    cut = int((1 - cfg.holdout_ratio) * len(d))
    return d.iloc[:cut].copy(), d.iloc[cut:].copy()


# =============================================================================
# 7) MODEL EVALUATION (CV + HOLDOUT) for BASE vs BASE+LAGS
# =============================================================================
def evaluate_feature_set_cv(
    train_df: pd.DataFrame,
    cfg: Config,
    feature_set_name: str,
    numeric_features: List[str]
) -> pd.DataFrame:
    banner(f"CV: FeatureSet = {feature_set_name}")

    feature_cols = [c for c in (numeric_features + list(cfg.categorical_features)) if c in train_df.columns]
    X = train_df[feature_cols]
    y = train_df[cfg.target].values

    tscv = TimeSeriesSplit(n_splits=cfg.n_splits_cv)
    scoring = {"r2":"r2","neg_mae":"neg_mean_absolute_error","neg_rmse":"neg_root_mean_squared_error"}

    rows = []
    for name, model in get_models(cfg).items():
        is_tree = name in ("RandomForest", "GradientBoosting")
        pre = build_preprocessor_tree(cfg, train_df, numeric_features) if is_tree else build_preprocessor_scaled(cfg, train_df, numeric_features)
        pipe = Pipeline(steps=[("preprocess", pre), ("model", model)])

        cv = cross_validate(pipe, X, y, cv=tscv, scoring=scoring, n_jobs=-1)

        row = {
            "FeatureSet": feature_set_name,
            "Model": name,
            "CV_R2": float(np.mean(cv["test_r2"])),
            "CV_MAE": float(-np.mean(cv["test_neg_mae"])),
            "CV_RMSE": float(-np.mean(cv["test_neg_rmse"]))
        }
        rows.append(row)
        print(f"{feature_set_name} | {name} => R2={row['CV_R2']:.4f}, RMSE={row['CV_RMSE']:.4f}")

    return pd.DataFrame(rows)

def plot_model_comparison(cv_all: pd.DataFrame, cfg: Config) -> None:
    banner("VIZ 14 — MODEL COMPARISON (CV)")

    fig = px.bar(cv_all, x="Model", y="CV_R2", color="FeatureSet", barmode="group",
                 title="VIZ 14 — TimeSeriesSplit CV: R² (Base vs Base+Lags)",
                 labels={"CV_R2":"Mean CV R²"})
    fig.add_hline(y=0, line_dash="dash", line_color="red")
    fig.update_layout(height=520)
    try_save_plot(fig, cfg, "viz_14_cv_r2_compare")
    if cfg.show_plots: fig.show()

    fig = px.bar(cv_all, x="Model", y="CV_RMSE", color="FeatureSet", barmode="group",
                 title="VIZ 14b — TimeSeriesSplit CV: RMSE (lower is better)",
                 labels={"CV_RMSE":"Mean CV RMSE"})
    fig.update_layout(height=520)
    try_save_plot(fig, cfg, "viz_14b_cv_rmse_compare")
    if cfg.show_plots: fig.show()


# =============================================================================
# 8) EXPLAINABILITY: Permutation Importance + PDP
# =============================================================================
def get_transformed_feature_names(pipe: Pipeline) -> List[str]:
    try:
        pre = pipe.named_steps["preprocess"]
        return list(pre.get_feature_names_out())
    except Exception:
        return []

def run_permutation_importance(pipe: Pipeline, X_test: pd.DataFrame, y_test: np.ndarray, cfg: Config, tag: str) -> pd.DataFrame:
    banner(f"EXPLAIN: Permutation Importance (Holdout) => {tag}")

    pre = pipe.named_steps["preprocess"]
    model = pipe.named_steps["model"]

    X_trans = pre.transform(X_test)
    feat_names = get_transformed_feature_names(pipe)
    if len(feat_names) != X_trans.shape[1]:
        feat_names = [f"feature_{i}" for i in range(X_trans.shape[1])]

    r = permutation_importance(
        model, X_trans, y_test,
        n_repeats=cfg.perm_repeats,
        random_state=cfg.random_state,
        scoring=cfg.perm_scoring
    )

    imp = pd.DataFrame({
        "Feature": feat_names,
        "Importance_Mean": r.importances_mean,
        "Importance_Std": r.importances_std
    }).sort_values("Importance_Mean", ascending=False).reset_index(drop=True)

    imp.to_csv(os.path.join(cfg.out_dir, f"permutation_importance__{tag}.csv"), index=False)

    topk = imp.head(cfg.perm_top_k).copy()
    fig = px.bar(topk.iloc[::-1], x="Importance_Mean", y="Feature", orientation="h",
                 error_x="Importance_Std",
                 title=f"Permutation Importance (Holdout) — Top {cfg.perm_top_k} — {tag}",
                 labels={"Importance_Mean":"Mean importance (Δ score)"})
    fig.update_layout(height=700)
    try_save_plot(fig, cfg, f"viz_explain_perm_importance_top{cfg.perm_top_k}__{tag}")
    if cfg.show_plots: fig.show()

    return imp

def run_pdp(pipe: Pipeline, X_test: pd.DataFrame, cfg: Config, tag: str, candidates: List[str]) -> None:
    banner(f"EXPLAIN: Partial Dependence (Holdout) => {tag}")

    chosen = []
    for f in candidates:
        if f in X_test.columns and pd.api.types.is_numeric_dtype(X_test[f]):
            chosen.append(f)
        if len(chosen) >= cfg.pdp_top_n:
            break

    if not chosen:
        print("No numeric raw features available for PDP — skipping.")
        return

    for feat in chosen:
        try:
            pd_res = partial_dependence(
                estimator=pipe,
                X=X_test,
                features=[feat],
                grid_resolution=cfg.pdp_grid_resolution,
                kind="average"
            )
        except TypeError:
            pd_res = partial_dependence(
                estimator=pipe,
                X=X_test,
                features=[feat],
                grid_resolution=cfg.pdp_grid_resolution
            )

        grid = pd_res["grid_values"][0]
        avg = pd_res["average"][0]

        out = pd.DataFrame({feat: grid, "PartialDependence": avg})
        out.to_csv(os.path.join(cfg.out_dir, f"pdp_values__{tag}__{feat}.csv"), index=False)

        fig = px.line(out, x=feat, y="PartialDependence",
                      title=f"PDP: {feat} → Predicted Benzene ({tag})",
                      labels={"PartialDependence":"Avg Predicted Benzene"})
        fig.update_layout(height=450)
        try_save_plot(fig, cfg, f"viz_explain_pdp__{tag}__{feat}")
        if cfg.show_plots: fig.show()


# =============================================================================
# 9) FIT BEST MODEL ON HOLDOUT + PLOTS (Actual vs Pred, Residuals)
# =============================================================================
def fit_best_holdout(
    d: pd.DataFrame,
    cfg: Config,
    best_row: pd.Series,
    numeric_features: List[str]
) -> Dict[str, object]:
    feature_set = best_row["FeatureSet"]
    model_name = best_row["Model"]
    tag = f"{feature_set}__{model_name}"

    banner(f"BEST MODEL FIT + HOLDOUT => {tag}")

    train_df, test_df = time_holdout_split(d, cfg)

    feature_cols = [c for c in (numeric_features + list(cfg.categorical_features)) if c in d.columns]
    X_train = train_df[feature_cols]
    y_train = train_df[cfg.target].values
    X_test = test_df[feature_cols]
    y_test = test_df[cfg.target].values

    model = get_models(cfg)[model_name]
    is_tree = model_name in ("RandomForest", "GradientBoosting")
    pre = build_preprocessor_tree(cfg, train_df, numeric_features) if is_tree else build_preprocessor_scaled(cfg, train_df, numeric_features)

    pipe = Pipeline(steps=[("preprocess", pre), ("model", model)])
    pipe.fit(X_train, y_train)

    y_pred = pipe.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = mean_squared_error(y_test, y_pred, squared=False)

    print(f"HOLDOUT R2:   {r2:.4f}")
    print(f"HOLDOUT MAE:  {mae:.4f}")
    print(f"HOLDOUT RMSE: {rmse:.4f}")

    ensure_out_dir(cfg)

    # Save model
    if HAS_JOBLIB:
        joblib.dump(pipe, os.path.join(cfg.out_dir, f"best_model__{tag}.joblib"))

    pred_df = pd.DataFrame({
        "DateTime": test_df["DateTime"].values,
        "Actual": y_test,
        "Predicted": y_pred
    })
    pred_df["Residual"] = pred_df["Actual"] - pred_df["Predicted"]
    pred_df.to_csv(os.path.join(cfg.out_dir, f"best_holdout_predictions__{tag}.csv"), index=False)

    # -------------------------
    # VIZ 15: Actual vs Predicted
    # -------------------------
    fig = px.scatter(pred_df, x="Actual", y="Predicted", opacity=0.6,
                     title=f"VIZ 15 — Actual vs Predicted (Holdout) — {tag}",
                     labels={"Actual":"Actual Benzene", "Predicted":"Predicted Benzene"})
    minv = float(min(pred_df["Actual"].min(), pred_df["Predicted"].min()))
    maxv = float(max(pred_df["Actual"].max(), pred_df["Predicted"].max()))
    fig.add_trace(go.Scatter(x=[minv,maxv], y=[minv,maxv], mode="lines",
                             name="Perfect Prediction", line=dict(color="red", dash="dash")))
    fig.update_layout(height=520)
    try_save_plot(fig, cfg, f"viz_15_actual_vs_pred__{tag}")
    if cfg.show_plots: fig.show()

    # -------------------------
    # VIZ 16: Residual Plot
    # -------------------------
    fig = px.scatter(pred_df, x="Predicted", y="Residual", opacity=0.55,
                     title=f"VIZ 16 — Residual Plot (Holdout) — {tag}",
                     labels={"Residual":"Actual - Predicted"})
    fig.add_hline(y=0, line_dash="dash", line_color="red")
    fig.update_layout(height=420)
    try_save_plot(fig, cfg, f"viz_16_residuals__{tag}")
    if cfg.show_plots: fig.show()

    # Time overlay
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=pred_df["DateTime"], y=pred_df["Actual"], mode="lines", name="Actual"))
    fig.add_trace(go.Scatter(x=pred_df["DateTime"], y=pred_df["Predicted"], mode="lines", name="Predicted"))
    fig.update_layout(title=f"Holdout Time-Series: Actual vs Predicted — {tag}",
                      xaxis_title="Time", yaxis_title="Benzene (µg/m³)", height=480)
    try_save_plot(fig, cfg, f"viz_16b_holdout_timeseries__{tag}")
    if cfg.show_plots: fig.show()

    # Explainability
    imp_df = run_permutation_importance(pipe, X_test, y_test, cfg, tag=tag)

    # PDP candidates (prefer interpretable drivers + lag signals)
    priority = [
        "CO_GT", "PT08_S2_NMHC", "NOx_GT", "T", "RH",
        f"{cfg.target}_lag_24h", f"{cfg.target}_rollmean_24h"
    ]
    candidates = []
    for p in priority:
        if p in X_test.columns:
            candidates.append(p)
    # then add remaining numeric columns
    for c in X_test.columns:
        if c not in candidates and pd.api.types.is_numeric_dtype(X_test[c]):
            candidates.append(c)

    run_pdp(pipe, X_test, cfg, tag, candidates)

    return {
        "tag": tag,
        "metrics": {"R2": r2, "MAE": mae, "RMSE": rmse},
        "pipe": pipe,
        "pred_df": pred_df,
        "perm_importance": imp_df
    }


# =============================================================================
# 10) LAG VISUALS (NEW)
# =============================================================================
def viz_lag_features(d: pd.DataFrame, cfg: Config) -> None:
    banner("EXTRA (NEW): Lag Feature Visualizations")

    # Scatter: current vs lag24h
    c = f"{cfg.target}_lag_24h"
    if c in d.columns:
        dd = d.dropna(subset=[cfg.target, c])
        fig = px.scatter(dd, x=c, y=cfg.target, opacity=0.55,
                         title="Lag VIZ — Benzene today vs Benzene lag 24h")
        fig.update_layout(height=450)
        try_save_plot(fig, cfg, "lag_viz_scatter_target_vs_lag24h")
        if cfg.show_plots: fig.show()

    # Time overlay: actual vs rollmean24h
    rcol = f"{cfg.target}_rollmean_24h"
    if rcol in d.columns:
        dd = d.dropna(subset=["DateTime", cfg.target, rcol]).iloc[::3].copy()
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dd["DateTime"], y=dd[cfg.target], mode="lines", name="Actual"))
        fig.add_trace(go.Scatter(x=dd["DateTime"], y=dd[rcol], mode="lines", name="RollingMean24h (past-only)"))
        fig.update_layout(title="Lag VIZ — Actual Benzene vs Rolling Mean (24h, past-only)",
                          height=500)
        try_save_plot(fig, cfg, "lag_viz_timeseries_actual_vs_rollmean24h")
        if cfg.show_plots: fig.show()

    # Autocorr proxy bars for selected lags
    rows = []
    for h in cfg.lag_hours:
        lc = f"{cfg.target}_lag_{h}h"
        if lc in d.columns:
            tmp = d[[cfg.target, lc]].dropna()
            if len(tmp) > 50:
                rows.append({"LagHours": h, "Corr": tmp.corr().iloc[0,1]})
    if rows:
        ac = pd.DataFrame(rows).sort_values("LagHours")
        fig = px.bar(ac, x="LagHours", y="Corr",
                     title="Lag VIZ — Corr(Benzene, Lagged Benzene)",
                     labels={"LagHours":"Lag (hours)", "Corr":"Correlation"})
        fig.add_hline(y=0, line_dash="dash", line_color="red")
        fig.update_layout(height=420)
        try_save_plot(fig, cfg, "lag_viz_autocorr_proxy")
        if cfg.show_plots: fig.show()


# =============================================================================
# 11) MAIN: EVERYTHING RUNS HERE
# =============================================================================
def run_full(cfg: Config) -> None:
    ensure_out_dir(cfg)

    df = load_raw(cfg)
    banner("RAW PREVIEW (head)")
    print(df.head(5))

    # Clean + engineer once
    dfc = clean_engineer(df, cfg)

    # ALL visualizations (original + extras)
    viz_all(dfc, cfg)

    # Add lag features
    dlag = add_lag_features(dfc, cfg)

    # Lag visuals
    viz_lag_features(dlag, cfg)

    # Prepare Feature Sets
    banner("STEP 5: PREPARE FEATURE SETS (BASE vs BASE+LAGS)")

    base_num = [c for c in cfg.base_numeric_features if c in dlag.columns]

    lag_cols = [f"{cfg.target}_lag_{h}h" for h in cfg.lag_hours if f"{cfg.target}_lag_{h}h" in dlag.columns]
    roll_cols = []
    for w in cfg.roll_windows:
        m = f"{cfg.target}_rollmean_{w}h"
        s = f"{cfg.target}_rollstd_{w}h"
        if m in dlag.columns: roll_cols.append(m)
        if s in dlag.columns: roll_cols.append(s)

    driver_lags = [c for c in dlag.columns if (c.endswith("_lag_24h") or c.endswith("_rollmean_24h")) and c not in (lag_cols + roll_cols)]
    lag_feature_set = base_num + lag_cols + roll_cols + driver_lags

    base_subset = list(dict.fromkeys(base_num + list(cfg.categorical_features) + [cfg.target]))
    lag_subset = list(dict.fromkeys(lag_feature_set + list(cfg.categorical_features) + [cfg.target]))

    base_df = dlag.dropna(subset=base_subset).copy()
    lag_df = dlag.dropna(subset=lag_subset).copy()

    print(f"Base_df shape: {base_df.shape}")
    print(f"Lag_df shape:  {lag_df.shape}")
    print(f"Base feature count: {len(base_num)}")
    print(f"Lag feature count:  {len(lag_feature_set)}")

    # CV uses train only (time split)
    base_train, _ = time_holdout_split(base_df, cfg)
    lag_train, _ = time_holdout_split(lag_df, cfg)

    cv_base = evaluate_feature_set_cv(base_train, cfg, "BASE", base_num)
    cv_lag = evaluate_feature_set_cv(lag_train, cfg, "BASE+LAGS", lag_feature_set)

    cv_all = pd.concat([cv_base, cv_lag], ignore_index=True)
    cv_all.to_csv(os.path.join(cfg.out_dir, "cv_comparison_all_models_base_vs_lags.csv"), index=False)

    banner("CV SUMMARY (Top by CV_R2)")
    print(cv_all.sort_values("CV_R2", ascending=False).head(20).to_string(index=False))

    # VIZ 14: model comparison
    plot_model_comparison(cv_all, cfg)

    # Pick best model by CV_R2
    best_row = cv_all.sort_values("CV_R2", ascending=False).iloc[0]
    banner("BEST MODEL SELECTED (by CV_R2)")
    print(best_row.to_string())

    # Fit best on HOLDOUT + VIZ 15/16 + explainability
    if best_row["FeatureSet"] == "BASE":
        fit_best_holdout(base_df, cfg, best_row, base_num)
    else:
        fit_best_holdout(lag_df, cfg, best_row, lag_feature_set)

    banner("DONE ✅ FULL PROJECT COMPLETE")
    print(f"All outputs saved to: {cfg.out_dir}")
    print("PNG missing? install kaleido: pip install -U kaleido")


if __name__ == "__main__":
    run_full(CFG)
