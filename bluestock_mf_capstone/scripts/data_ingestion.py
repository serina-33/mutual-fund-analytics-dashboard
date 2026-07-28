"""
Day 1 - Data Ingestion Script
Bluestock Fintech MF Capstone

Loads all 10 provided CSV datasets, prints shape/dtypes/head for each,
and runs basic anomaly checks (nulls, negative values, code mismatches).
"""

import pandas as pd
from pathlib import Path

RAW_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"

FILES = {
    "fund_master": "01_fund_master.csv",
    "nav_history": "02_nav_history.csv",
    "aum_by_fund_house": "03_aum_by_fund_house.csv",
    "monthly_sip_inflows": "04_monthly_sip_inflows.csv",
    "category_inflows": "05_category_inflows.csv",
    "industry_folio_count": "06_industry_folio_count.csv",
    "scheme_performance": "07_scheme_performance.csv",
    "investor_transactions": "08_investor_transactions.csv",
    "portfolio_holdings": "09_portfolio_holdings.csv",
    "benchmark_indices": "10_benchmark_indices.csv",
}


def load_all():
    """Load every CSV into a dict of DataFrames."""
    dataframes = {}
    for name, filename in FILES.items():
        path = RAW_DIR / filename
        try:
            df = pd.read_csv(path)
            dataframes[name] = df
        except Exception as e:
            print(f"[ERROR] Could not load {filename}: {e}")
    return dataframes


def inspect(dataframes):
    """Print shape, dtypes, and head for each DataFrame."""
    for name, df in dataframes.items():
        print("=" * 70)
        print(f"DATASET: {name}")
        print("-" * 70)
        print("Shape:", df.shape)
        print("\nDtypes:\n", df.dtypes)
        print("\nHead:\n", df.head(3))
        print()


def check_anomalies(dataframes):
    """Basic anomaly / data-quality checks across all datasets."""
    print("=" * 70)
    print("ANOMALY / DATA QUALITY SUMMARY")
    print("=" * 70)

    for name, df in dataframes.items():
        nulls = df.isnull().sum()
        nulls = nulls[nulls > 0]
        dupes = df.duplicated().sum()
        print(f"\n[{name}]")
        print(f"  Duplicate rows: {dupes}")
        if not nulls.empty:
            print(f"  Columns with nulls:\n{nulls}")
        else:
            print("  No nulls found.")

    # Specific numeric sanity checks
    nav = dataframes.get("nav_history")
    if nav is not None and "nav" in nav.columns:
        bad_nav = (nav["nav"] <= 0).sum()
        print(f"\n[nav_history] Non-positive NAV values: {bad_nav}")

    tx = dataframes.get("investor_transactions")
    if tx is not None and "amount_inr" in tx.columns:
        bad_amt = (tx["amount_inr"] <= 0).sum()
        print(f"[investor_transactions] Non-positive transaction amounts: {bad_amt}")
        print(f"[investor_transactions] transaction_type values: {tx['transaction_type'].unique()}")
        if "kyc_status" in tx.columns:
            print(f"[investor_transactions] kyc_status values: {tx['kyc_status'].unique()}")

    fm = dataframes.get("fund_master")
    if fm is not None:
        print(f"\n[fund_master] Unique fund houses: {fm['fund_house'].nunique()}")
        print(fm['fund_house'].unique())
        print(f"\n[fund_master] Unique categories: {fm['category'].unique()}")
        print(f"[fund_master] Unique sub_categories: {fm['sub_category'].unique()}")
        print(f"[fund_master] Unique risk_category: {fm['risk_category'].unique()}")


def validate_amfi_codes(dataframes):
    """Confirm every amfi_code in fund_master exists in nav_history, and vice versa."""
    print("\n" + "=" * 70)
    print("AMFI CODE VALIDATION")
    print("=" * 70)

    fm = dataframes["fund_master"]
    nav = dataframes["nav_history"]

    master_codes = set(fm["amfi_code"])
    nav_codes = set(nav["amfi_code"])

    missing_in_nav = master_codes - nav_codes
    missing_in_master = nav_codes - master_codes

    print(f"Total funds in fund_master: {len(master_codes)}")
    print(f"Total unique funds in nav_history: {len(nav_codes)}")
    print(f"Fund master codes missing from nav_history: {len(missing_in_nav)} -> {missing_in_nav}")
    print(f"NAV codes missing from fund_master: {len(missing_in_master)} -> {missing_in_master}")

    if not missing_in_nav and not missing_in_master:
        print("RESULT: PASS - all AMFI codes match perfectly between fund_master and nav_history.")
    else:
        print("RESULT: MISMATCH FOUND - investigate before proceeding to Day 2 cleaning.")


if __name__ == "__main__":
    dfs = load_all()
    inspect(dfs)
    check_anomalies(dfs)
    validate_amfi_codes(dfs)
