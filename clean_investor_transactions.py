import pandas as pd

print("Loading Investor Transactions Dataset...")

df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

print("Original Shape:", df.shape)

# ----------------------------------
# Convert date column
# ----------------------------------

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

print("Date format standardized.")

# ----------------------------------
# Standardize transaction types
# ----------------------------------

df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

print(
    "\nTransaction Types Found:"
)

print(
    df["transaction_type"].unique()
)

# ----------------------------------
# Validate amount
# ----------------------------------

invalid_amounts = df[
    df["amount_inr"] <= 0
]

print(
    f"\nInvalid Amount Records: {len(invalid_amounts)}"
)

# ----------------------------------
# Validate KYC
# ----------------------------------

print(
    "\nKYC Status Values:"
)

print(
    df["kyc_status"].unique()
)

# ----------------------------------
# Remove duplicates
# ----------------------------------

before = len(df)

df = df.drop_duplicates()

after = len(df)

print(
    f"\nDuplicates Removed: {before-after}"
)

# ----------------------------------
# Save cleaned dataset
# ----------------------------------

df.to_csv(
    "data/processed/investor_transactions_cleaned.csv",
    index=False
)

print(
    "\nCleaned dataset saved."
)

print(
    "Final Shape:",
    df.shape
)