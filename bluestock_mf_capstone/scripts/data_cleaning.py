import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(exist_ok=True)
nav = pd.read_csv(RAW_DIR / "02_nav_history.csv")

print(nav.head())
# Convert date column to datetime
nav["date"] = pd.to_datetime(nav["date"])

# Sort by AMFI code and date
nav = nav.sort_values(["amfi_code", "date"])

# Forward fill missing NAV values
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

# Remove duplicate rows
nav = nav.drop_duplicates()

# Check for invalid NAV values
invalid_nav = nav[nav["nav"] <= 0]

print("Invalid NAV records:")
print(invalid_nav)
nav.to_csv(
    PROCESSED_DIR / "nav_history_cleaned.csv",
    index=False
)

print("nav_history_cleaned.csv saved successfully!")
nav.to_csv(PROCESSED_DIR / "nav_history_cleaned.csv", index=False)

print("nav_history_cleaned.csv saved successfully!")
# ------------------------------
# Clean investor_transactions.csv
# ------------------------------

trans = pd.read_csv(RAW_DIR / "08_investor_transactions.csv")

print("Columns in investor_transactions.csv:")
print(trans.columns.tolist())

# Convert transaction date to datetime
trans["transaction_date"] = pd.to_datetime(trans["transaction_date"])

# Standardize transaction type
trans["transaction_type"] = (
    trans["transaction_type"]
    .str.strip()
    .str.upper()
)

# Validate amount
invalid_amount = trans[trans["amount_inr"] <= 0]

print("Invalid Amount Records:")
print(invalid_amount)

# Check KYC values
print("KYC Status:")
print(trans["kyc_status"].unique())

# Save cleaned file
trans.to_csv(
    PROCESSED_DIR / "investor_transactions_cleaned.csv",
    index=False
)

print("investor_transactions_cleaned.csv saved successfully!")
# ------------------------------
# Clean scheme_performance.csv
# ------------------------------

perf = pd.read_csv(RAW_DIR / "07_scheme_performance.csv")

print("Columns in scheme_performance.csv:")
print(perf.columns.tolist())
# Convert return columns to numeric
return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_columns:
    perf[col] = pd.to_numeric(perf[col], errors="coerce")

# Check expense ratio
invalid_expense = perf[
    (perf["expense_ratio_pct"] < 0.1) |
    (perf["expense_ratio_pct"] > 2.5)
]

print("Invalid Expense Ratio Records:")
print(invalid_expense)

# Save cleaned file
perf.to_csv(
    PROCESSED_DIR / "scheme_performance_cleaned.csv",
    index=False
)

print("scheme_performance_cleaned.csv saved successfully!")