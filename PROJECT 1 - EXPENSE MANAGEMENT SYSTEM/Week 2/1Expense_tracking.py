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
grouped = df.groupby(['user_id', 'month'])['amount']
monthly_total = grouped.sum()
monthly_avg = round(grouped.mean(),2)
summary = pd.DataFrame({
    'monthly_total': monthly_total,
    'monthly_average': monthly_avg
}).reset_index()
# # - Use pandas to create a breakdown of expenses by category
category_breakdown = df.groupby('category_id')['amount'].sum()
print("category breakdown:\n",category_breakdown)
df.to_csv("cleaned_expenses.csv",index = False)
# monthly summary
summary.to_csv("monthly_summary.csv",index = False)
