# Data Dictionary

## 1. nav_history_cleaned.csv

| Column | Data Type | Description | Source |
|--------|-----------|-------------|--------|
| amfi_code | Integer | Unique AMFI scheme code | nav_history.csv |
| date | Date | NAV date | nav_history.csv |
| nav | Float | Net Asset Value | nav_history.csv |

---

## 2. investor_transactions_cleaned.csv

| Column | Data Type | Description | Source |
|--------|-----------|-------------|--------|
| investor_id | Integer | Investor ID | investor_transactions.csv |
| transaction_date | Date | Transaction date | investor_transactions.csv |
| amfi_code | Integer | AMFI scheme code | investor_transactions.csv |
| transaction_type | Text | SIP / Lumpsum / Redemption | investor_transactions.csv |
| amount_inr | Float | Transaction amount | investor_transactions.csv |
| state | Text | Investor state | investor_transactions.csv |
| city | Text | Investor city | investor_transactions.csv |
| city_tier | Text | T30/B30 classification | investor_transactions.csv |
| age_group | Text | Investor age group | investor_transactions.csv |
| gender | Text | Investor gender | investor_transactions.csv |
| annual_income_lakh | Float | Annual income (Lakhs) | investor_transactions.csv |
| payment_mode | Text | Payment mode | investor_transactions.csv |
| kyc_status | Text | KYC status | investor_transactions.csv |

---

## 3. scheme_performance_cleaned.csv

| Column | Data Type | Description | Source |
|--------|-----------|-------------|--------|
| amfi_code | Integer | AMFI scheme code | scheme_performance.csv |
| scheme_name | Text | Mutual fund scheme name | scheme_performance.csv |
| fund_house | Text | Fund house | scheme_performance.csv |
| category | Text | Fund category | scheme_performance.csv |
| return_1yr_pct | Float | 1-year return | scheme_performance.csv |
| return_3yr_pct | Float | 3-year return | scheme_performance.csv |
| return_5yr_pct | Float | 5-year return | scheme_performance.csv |
| aum_crore | Float | Assets Under Management | scheme_performance.csv |
| expense_ratio_pct | Float | Expense ratio | scheme_performance.csv |
| risk_grade | Text | Risk category | scheme_performance.csv |