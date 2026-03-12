import pandas as pd
from sqlalchemy import create_engine

# STEP A: Excel se data load karo

print("Loading Excel data...")

transactions = pd.read_excel("AML_Raw_Transactions.xlsx", sheet_name="Transactions")
customers    = pd.read_excel("AML_Raw_Transactions.xlsx", sheet_name="Customers")


# STEP B: Transactions + Customers merge karo

df = transactions.merge(customers, on="Customer_ID", how="left")
print(f"Total transactions loaded: {len(df)}")


# STEP C: Risk Scoring — har transaction ko score do

def calculate_risk(row):
    score = 0
    reasons = []

    # Rule 1: PEP customer = high risk
    if row["Category"] == "PEP":
        score += 40
        reasons.append("PEP Customer")

    # Rule 2: Structuring — cash deposit 40k-50k (just below 50k limit)
    if row["TXN_Type"] == "Cash Deposit" and 40000 <= row["Amount"] <= 50000:
        score += 35
        reasons.append("Structuring Suspected")

    # Rule 3: Large wire transfer (above 5 lakh)
    if row["TXN_Type"] == "Wire Transfer" and row["Amount"] >= 500000:
        score += 30
        reasons.append("Large Wire Transfer")

    # Rule 4: High risk country
    high_risk_countries = ["UAE", "Russia", "Cayman Islands", "Panama", "Nigeria"]
    if row["Country"] in high_risk_countries:
        score += 25
        reasons.append("High Risk Country")

    # Rule 5: KYC incomplete
    if row["KYC_Status"] in ["Pending", "Incomplete"]:
        score += 20
        reasons.append("KYC Incomplete")

    # Rule 6: Very large transaction (above 10 lakh)
    if row["Amount"] >= 1000000:
        score += 20
        reasons.append("Very Large Amount")

    return score, ", ".join(reasons) if reasons else "None"

print("Calculating risk scores...")
df[["Risk_Score", "Risk_Reasons"]] = df.apply(
    lambda row: pd.Series(calculate_risk(row)), axis=1
)


# STEP D: Risk Label lagao

def risk_label(score):
    if score >= 50:
        return "HIGH"
    elif score >= 25:
        return "MEDIUM"
    else:
        return "LOW"

df["Risk_Level"] = df["Risk_Score"].apply(risk_label)


# STEP E: Alert flag karo

df["Alert"] = df["Risk_Level"].apply(lambda x: "YES" if x in ["HIGH", "MEDIUM"] else "NO")


# STEP F: Results print karo

print("\n--- RISK SUMMARY ---")
print(df["Risk_Level"].value_counts())

print("\n--- HIGH RISK TRANSACTIONS ---")
high_risk = df[df["Risk_Level"] == "HIGH"][
    ["TXN_ID", "Name", "Amount", "TXN_Type", "Risk_Score", "Risk_Reasons"]
]
print(high_risk.to_string(index=False))


# STEP G: SQLite Database mein save karo

print("\nSaving to database...")
engine = create_engine("sqlite:///AML_Database.db")

df.to_sql("transactions", engine, if_exists="replace", index=False)

alerts_df = df[df["Alert"] == "YES"]
alerts_df.to_sql("alerts", engine, if_exists="replace", index=False)

high_risk_df = df[df["Risk_Level"] == "HIGH"]
high_risk_df.to_sql("high_risk", engine, if_exists="replace", index=False)

print("✅ Database saved: AML_Database.db")
print(f"   Total transactions: {len(df)}")
print(f"   Total alerts: {len(alerts_df)}")
print(f"   High risk: {len(high_risk_df)}")
# Power BI ke liye CSV export
df.to_csv("AML_Final_Data.csv", index=False)
print("✅ CSV exported: AML_Final_Data.csv")