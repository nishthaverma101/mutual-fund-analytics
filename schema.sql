-- Dimension Table

CREATE TABLE dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    plan TEXT
);

-- Date Dimension

CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_date DATE,
    year INTEGER,
    month INTEGER,
    quarter INTEGER
);

-- NAV Fact Table

CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    nav_date DATE,
    nav REAL,

    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)
);

-- Transactions Fact Table

CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    investor_id TEXT,
    amfi_code INTEGER,
    transaction_date DATE,
    transaction_type TEXT,
    amount_inr REAL,
    kyc_status TEXT,

    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)
);

-- Performance Fact Table

CREATE TABLE fact_performance (
    performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    expense_ratio_pct REAL,

    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)
);

-- AUM Fact Table

CREATE TABLE fact_aum (
    aum_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_house TEXT,
    month DATE,
    aum_crore REAL
);