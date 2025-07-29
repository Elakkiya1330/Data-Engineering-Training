# - Load expense data from CSV or API
import pandas as pd
import numpy as np
df = pd.read_csv('expenses.csv')
# - Clean and standardize formats (e.g., dates, amounts)
df['amount'] = df['amount'].astype(str).str.replace('₹', '', regex=False)
df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
df['expense_date'] = pd.to_datetime(df['expense_date'], format='mixed', errors='coerce', dayfirst=False)
# # - Use numpy to calculate monthly totals and averages
df['month'] = df['expense_date'].dt.to_period('M')
monthly_total = df.groupby('month')['amount'].sum()
monthly_avg = df.groupby('month')['amount'].mean()
print("Monthly Totals:\n", monthly_total)
print("Monthly Averages:\n", round(monthly_avg,2))
# # - Use pandas to create a breakdown of expenses by category
category_breakdown = df.groupby('category_id')['amount'].sum()
print("category breakdown:\n",category_breakdown)
df.to_csv("cleaned_expenses.csv",index = False)
# monthly summary
monthly_summary = df.groupby('month')['amount'].sum()
monthly_summary.to_csv("monthly_summary.csv")
