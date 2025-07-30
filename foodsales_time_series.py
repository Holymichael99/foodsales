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

# --------------------------------------------
# 2. Weekly Sales Trend
# --------------------------------------------
weekly_sales = df.groupby('Week')['TotalSales'].sum().reset_index()

weekly_sales['Week'] = pd.to_datetime(weekly_sales['Week'].astype(str).str.split('/').str[0])
weekly_sales = weekly_sales.sort_values('Week')

plt.figure(figsize=(12, 4))
sns.lineplot(data=weekly_sales, x='Week', y='TotalSales')
plt.title("Weekly Sales Trend")
plt.xlabel("Week")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# --------------------------------------------
# 3. Year-over-Year Seasonality
# --------------------------------------------
df['MonthName'] = df['OrderDate'].dt.month_name().str[:3]
df['MonthNum'] = df['OrderDate'].dt.month
seasonality = df.groupby(['Year', 'MonthNum', 'MonthName'])['TotalSales'].sum().reset_index()

# Sort months properly
month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
seasonality['MonthName'] = pd.Categorical(seasonality['MonthName'], categories=month_order, ordered=True)
seasonality = seasonality.sort_values(['Year', 'MonthNum'])

plt.figure(figsize=(10, 5))
sns.lineplot(data=seasonality, x='MonthName', y='TotalSales', hue='Year', marker='o')
plt.title("Seasonality: Monthly Sales by Year")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()
