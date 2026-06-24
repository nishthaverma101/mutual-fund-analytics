# Mutual Fund Analytics - Data Dictionary

## 1. Fund Master (01_fund_master.csv)

| Column      | Data Type | Business Definition                                   |
| ----------- | --------- | ----------------------------------------------------- |
| amfi_code   | INTEGER   | Unique identifier assigned to each mutual fund scheme |
| scheme_name | TEXT      | Name of the mutual fund scheme                        |
| fund_house  | TEXT      | Asset Management Company (AMC)                        |
| category    | TEXT      | Fund category (Large Cap, Mid Cap, Hybrid, etc.)      |
| plan        | TEXT      | Direct or Regular plan                                |
| risk_grade  | TEXT      | Risk classification of the scheme                     |

Source: AMFI Fund Master Dataset

---

## 2. NAV History (02_nav_history.csv)

| Column    | Data Type | Business Definition      |
| --------- | --------- | ------------------------ |
| amfi_code | INTEGER   | Fund identifier          |
| date      | DATE      | NAV observation date     |
| nav       | REAL      | Net Asset Value per unit |

Source: Historical NAV Dataset

---

## 3. Investor Transactions (08_investor_transactions.csv)

| Column           | Data Type | Business Definition                 |
| ---------------- | --------- | ----------------------------------- |
| investor_id      | TEXT      | Unique investor identifier          |
| transaction_date | DATE      | Date of transaction                 |
| amfi_code        | INTEGER   | Fund identifier                     |
| transaction_type | TEXT      | SIP, Lumpsum, or Redemption         |
| amount_inr       | REAL      | Transaction amount in Indian Rupees |
| state            | TEXT      | Investor state                      |
| city             | TEXT      | Investor city                       |
| city_tier        | TEXT      | Tier classification of city         |
| age_group        | TEXT      | Investor age segment                |
| gender           | TEXT      | Investor gender                     |
| payment_mode     | TEXT      | Mode of payment                     |
| kyc_status       | TEXT      | KYC verification status             |

Source: Investor Transaction Dataset

---

## 4. Scheme Performance (07_scheme_performance.csv)

| Column            | Data Type | Business Definition                  |
| ----------------- | --------- | ------------------------------------ |
| amfi_code         | INTEGER   | Fund identifier                      |
| return_1yr_pct    | REAL      | One-year return percentage           |
| return_3yr_pct    | REAL      | Three-year return percentage         |
| return_5yr_pct    | REAL      | Five-year return percentage          |
| expense_ratio_pct | REAL      | Annual expense ratio charged by fund |

Source: Scheme Performance Dataset

---

## Business Terms

### NAV

Net Asset Value - price of one mutual fund unit.

### AMFI Code

Unique identifier assigned by the Association of Mutual Funds in India.

### SIP

Systematic Investment Plan - periodic investment into a mutual fund.

### AUM

Assets Under Management - total assets managed by a fund or AMC.

### KYC

Know Your Customer - investor identity verification process.
