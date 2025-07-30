import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set(style="whitegrid")

# Load Excel file and select the 'FoodSales' sheet
file_path = "Sampledatafoodslaes.xlsx"  # Ensure this file is in the script's directory
df = pd.read_excel(file_path, sheet_name="FoodSales")

# Convert OrderDate to datetime
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# Feature Engineering
df['TotalSales'] = df['Quantity'] * df['UnitPrice']
df['Month'] = df['OrderDate'].dt.month_name().str[:3]
df['Year'] = df['OrderDate'].dt.year

# --------------------------------------------
# 1. Sales by Region
# --------------------------------------------
sales_by_region = df.groupby('Region')['TotalSales'].sum().reset_index()
print("Sales by Region:\n", sales_by_region, "\n")

plt.figure(figsize=(6, 4))
sns.barplot(x='Region', y='TotalSales', data=sales_by_region, palette="Blues_d")
plt.title("Total Sales by Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# --------------------------------------------
# 2. Sales by City (Top 5)
# --------------------------------------------
sales_by_city = df.groupby('City')['TotalSales'].sum().reset_index()
top_cities = sales_by_city.sort_values(by='TotalSales', ascending=False).head()
print("Top Cities by Total Sales:\n", top_cities, "\n")

plt.figure(figsize=(8, 4))
sns.barplot(x='TotalSales', y='City', data=top_cities, palette="Purples_r")
plt.title("Top 5 Cities by Total Sales")
plt.xlabel("Total Sales")
plt.tight_layout()
plt.show()

# --------------------------------------------
# 3. Sales by Product (Top 5)
# --------------------------------------------
sales_by_product = df.groupby('Product')['TotalSales'].sum().reset_index()
top_products = sales_by_product.sort_values(by='TotalSales', ascending=False).head()
print("Top Products by Total Sales:\n", top_products, "\n")

plt.figure(figsize=(8, 4))
sns.barplot(x='TotalSales', y='Product', data=top_products, palette="Greens_r")
plt.title("Top 5 Products by Total Sales")
plt.xlabel("Total Sales")
plt.tight_layout()
plt.show()

# --------------------------------------------
# 4. Sales by Category
# --------------------------------------------
sales_by_category = df.groupby('Category')['TotalSales'].sum().reset_index()
print("Sales by Category:\n", sales_by_category, "\n")

plt.figure(figsize=(6, 4))
sns.barplot(x='Category', y='TotalSales', data=sales_by_category, palette="Oranges")
plt.title("Total Sales by Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# --------------------------------------------
# 5. Monthly Sales by Year
# --------------------------------------------
sales_by_month_year = df.groupby(['Year', 'Month'])['TotalSales'].sum().reset_index()

# Ensure month order is preserved
month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales_by_month_year['Month'] = pd.Categorical(sales_by_month_year['Month'], categories=month_order, ordered=True)
sales_by_month_year = sales_by_month_year.sort_values(['Year', 'Month'])

print("Monthly Sales by Year:\n", sales_by_month_year.head(), "\n")

plt.figure(figsize=(10, 5))
sns.barplot(x='Month', y='TotalSales', hue='Year', data=sales_by_month_year)
plt.title("Monthly Sales by Year")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()
