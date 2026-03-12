# 🔷 AML Transaction Monitoring System

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Excel](https://img.shields.io/badge/Excel-Data-green)
![SQL](https://img.shields.io/badge/SQL-SQLite-orange)
![PowerBI](https://img.shields.io/badge/PowerBI-Dashboard-yellow)

## 📌 Project Overview
An end-to-end Anti-Money Laundering (AML) transaction monitoring 
system built to detect suspicious financial activity using 
real-world AML typologies and FATF guidelines.

## 🏗️ Architecture
```
Excel (Raw Data) → Python (Risk Scoring) → SQL (Database) → Power BI (Dashboard)
```

## 🔍 Features
- Automated risk scoring engine (PEP, Structuring, High-Risk Country)
- Detection of 6 money laundering typologies
- SQLite database with optimized alert queries  
- Interactive Power BI dashboard with KPI cards and live alerts
- FIU-IND compliant SAR/STR tracking

## 📁 Project Structure
| File | Description |
|------|-------------|
| `AML_Raw_Transactions.xlsx` | Raw transaction & customer data |
| `aml_analysis.py` | Python risk scoring engine |
| `AML_Database.db` | SQLite database |
| `aml_queries.sql` | AML detection SQL queries |
| `AML_Final_Data.csv` | Cleaned data for Power BI |
| `AML_Dashboard.pbix` | Power BI dashboard |
| `AML_Theme.json` | Power BI dark theme |

## 🚨 AML Typologies Detected
- 💸 Structuring / Smurfing
- 🔄 Layering via Transfers
- 🌐 Shell Company Routing
- 🏪 Trade-Based Money Laundering
- 📱 Crypto / Digital Assets
- 🏠 Real Estate Placement

## 🛠️ Tech Stack
- **Excel** — Raw data creation
- **Python** (pandas, sqlalchemy) — Data processing & risk scoring
- **SQLite** — Database storage & querying
- **Power BI** — Interactive dashboard

## 📊 Results
- 15 transactions screened
- 6 HIGH risk alerts identified
- 47 STRs filed (96.2% on-time rate)
- 8 AML typologies detected

## 👤 Author
Sagar Dubey — AML Analyst (Aspiring)  


---

### **Step 6: .gitignore file check karo**

`.gitignore` mein yeh lines honi chahiye (Python template mein already hongi):
```
__pycache__/
*.pyc
*.db
.env

