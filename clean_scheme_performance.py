import pandas as pd

print("Loading Scheme Performance Dataset...")

df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

print("Original Shape:", df.shape)

# ----------------------------------
# Return columns
# ----------------------------------

return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

# ----------------------------------
# Convert returns to numeric
# ----------------------------------

for col in return_columns:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

print("\nReturn columns converted to numeric.")

# ----------------------------------
# Check missing numeric values
# ----------------------------------

print("\nMissing Return Values:")

print(
    df[return_columns]
    .isnull()
    .sum()
)

# ----------------------------------
# Expense Ratio Validation
# ----------------------------------

invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1)
    |
    (df["expense_ratio_pct"] > 2.5)
]

print(
    f"\nExpense Ratio Anomalies: {len(invalid_expense)}"
)

# ----------------------------------
# Duplicate Check
# ----------------------------------

before = len(df)

df = df.drop_duplicates()

after = len(df)

print(
    f"Duplicates Removed: {before-after}"
)

# ----------------------------------
# Save cleaned dataset
# ----------------------------------

df.to_csv(
    "data/processed/scheme_performance_cleaned.csv",
    index=False
)

print("\nCleaned dataset saved.")
print("Final Shape:", df.shape)