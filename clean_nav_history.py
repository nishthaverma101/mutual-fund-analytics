import pandas as pd

print("Loading NAV History Dataset...")

df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

# ------------------------------
# Convert date column
# ------------------------------

df["date"] = pd.to_datetime(df["date"])

print("\nDate converted to datetime.")

# ------------------------------
# Sort data
# ------------------------------

df = df.sort_values(
    by=["amfi_code", "date"]
)

print("Data sorted by AMFI code and date.")

# ------------------------------
# Remove duplicates
# ------------------------------

before = len(df)

df = df.drop_duplicates()

after = len(df)

print(f"Duplicates Removed: {before - after}")

# ------------------------------
# Forward fill NAV
# ------------------------------

df["nav"] = df.groupby(
    "amfi_code"
)["nav"].ffill()

print("Missing NAV values forward-filled.")

# ------------------------------
# Validate NAV > 0
# ------------------------------

invalid_nav = df[df["nav"] <= 0]

print(
    f"Invalid NAV Records: {len(invalid_nav)}"
)

# ------------------------------
# Save cleaned file
# ------------------------------

df.to_csv(
    "data/processed/nav_history_cleaned.csv",
    index=False
)

print("\nCleaned dataset saved.")
print("Final Shape:", df.shape)