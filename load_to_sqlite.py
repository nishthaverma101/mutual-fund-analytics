import pandas as pd
from sqlalchemy import create_engine

print("Creating SQLite Database...")

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

# -----------------------------
# Load Cleaned CSVs
# -----------------------------

nav_df = pd.read_csv(
    "data/processed/nav_history_cleaned.csv"
)

txn_df = pd.read_csv(
    "data/processed/investor_transactions_cleaned.csv"
)

perf_df = pd.read_csv(
    "data/processed/scheme_performance_cleaned.csv"
)

fund_df = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

# -----------------------------
# Load Tables
# -----------------------------

fund_df.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav_df.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

txn_df.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

perf_df.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("\nTables Loaded Successfully!")

print("\nRow Counts:")

print(
    "dim_fund:",
    len(fund_df)
)

print(
    "fact_nav:",
    len(nav_df)
)

print(
    "fact_transactions:",
    len(txn_df)
)

print(
    "fact_performance:",
    len(perf_df)
)