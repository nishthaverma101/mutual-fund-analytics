import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Extract unique AMFI codes
fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

# Find codes present in fund_master but missing in nav_history
missing_codes = fund_codes - nav_codes

print("=" * 60)
print("AMFI CODE VALIDATION")
print("=" * 60)

print(f"Total Fund Master Codes: {len(fund_codes)}")
print(f"Total NAV History Codes: {len(nav_codes)}")
print(f"Missing Codes Count: {len(missing_codes)}")

if len(missing_codes) == 0:
    print("\nAll AMFI codes are present in NAV history.")
else:
    print("\nMissing AMFI Codes:")
    for code in missing_codes:
        print(code)