## Purpose

Build an end-to-end pipeline that extracts OpenFEMA data, loads it into postfres and models it for analytics:

API → Python → PostgreSQL → dbt → Power BI

## Tools

- Python
- PostgreSQL
- dbt
- Power BI

## Architecture

RAW
↓
STAGING
↓
MODEL
↓
BI