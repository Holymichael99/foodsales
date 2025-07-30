import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style
sns.set(style="whitegrid")

# Load the Excel file
file_path = "Sampledatafoodslaes.xlsx"
df = pd.read_excel(file_path, sheet_name="FoodSales")

# Convert OrderDate to datetime
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# Feature engineering
df['TotalSales'] = df['Quantity'] * df['UnitPrice']
df['Year'] = df['OrderDate'].dt.year
df['Month'] = df['OrderDate'].dt.to_period('M').astype(str)
df['Week'] = df['OrderDate'].dt.to_period('W').astype(str)

# --------------------------------------------
# 1. Monthly Sales Trend
# --------------------------------------------
monthly_sales = df.groupby('Month')['TotalSales'].sum().reset_index()

# Sort by date
monthly_sales['Month'] = pd.to_datetime(monthly_sales['Month'])
monthly_sales = monthly_sales.sort_values('Month')

plt.figure(figsize=(10, 4))
sns.lineplot(data=monthly_sales, x='Month', y='TotalSales', marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()