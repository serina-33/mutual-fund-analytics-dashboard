import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED = BASE_DIR / "data" / "processed"
DB = BASE_DIR / "db" / "bluestock_mf.db"

engine = create_engine(f"sqlite:///{DB}")

nav = pd.read_csv(PROCESSED / "nav_history_cleaned.csv")
trans = pd.read_csv(PROCESSED / "investor_transactions_cleaned.csv")
perf = pd.read_csv(PROCESSED / "scheme_performance_cleaned.csv")

nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
trans.to_sql("fact_transactions", engine, if_exists="replace", index=False)
perf.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("SQLite database created successfully!")