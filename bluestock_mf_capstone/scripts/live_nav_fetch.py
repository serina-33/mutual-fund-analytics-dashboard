"""
Day 1 - Live NAV Fetch Script
Bluestock Fintech MF Capstone

Fetches live/historical NAV data from the free mfapi.in API for:
  - HDFC Top 100 Direct   (125497)
  - SBI Bluechip          (119551)
  - ICICI Bluechip        (120503)
  - Nippon Large Cap      (118632)
  - Axis Bluechip         (119092)
  - Kotak Bluechip        (120841)

Each scheme's response is parsed from JSON and saved as a raw CSV
into data/raw/live/<scheme_code>.csv
"""

import requests
import pandas as pd
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent.parent / "data" / "raw" / "live"
OUT_DIR.mkdir(parents=True, exist_ok=True)

SCHEMES = {
    125497: "HDFC_Top_100_Direct",
    119551: "SBI_Bluechip",
    120503: "ICICI_Bluechip",
    118632: "Nippon_Large_Cap",
    119092: "Axis_Bluechip",
    120841: "Kotak_Bluechip",
}


def fetch_scheme_nav(code: int) -> pd.DataFrame:
    url = f"https://api.mfapi.in/mf/{code}"
    resp = requests.get(url, timeout=15)
    resp.raise_for_status()
    payload = resp.json()

    meta = payload.get("meta", {})
    nav_data = payload.get("data", [])

    df = pd.DataFrame(nav_data)
    df["amfi_code"] = code
    df["scheme_name"] = meta.get("scheme_name")
    df["fund_house"] = meta.get("fund_house")
    return df


def main():
    for code, label in SCHEMES.items():
        try:
            df = fetch_scheme_nav(code)
            out_path = OUT_DIR / f"{code}_{label}.csv"
            df.to_csv(out_path, index=False)
            print(f"[OK] {label} ({code}): {len(df)} rows saved -> {out_path}")
        except Exception as e:
            print(f"[FAIL] {label} ({code}): {e}")


if __name__ == "__main__":
    main()

import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

data = response.json()

df = pd.DataFrame(data["data"])

df.to_csv("data/raw/HDFC_NAV.csv", index=False)

print("Live NAV downloaded successfully!")