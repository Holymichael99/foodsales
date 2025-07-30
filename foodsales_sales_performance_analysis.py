# food_sales_analysis.py

import pandas as pd

# Load Excel file and select the 'FoodSales' sheet
file_path = "Sampledatafoodslaes.xlsx"  # Ensure this file is in the same directory
df = pd.read_excel(file_path, sheet_name="FoodSales")

# Convert OrderDate to datetime format
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# Feature Engineering
df['TotalSales'] = df['Quantity'] * df['UnitPrice']
df['Month'] = df['OrderDate'].dt.month_name().str[:3]
df['Year'] = df['OrderDate'].dt.year

# Sales by Region
sales_by_region = df.groupby('Region')['TotalSales'].sum().reset_index()
print("Sales by Region:\n", sales_by_region, "\n")

# Sales by City
sales_by_city = df.groupby('City')['TotalSales'].sum().reset_index()
print("Top Cities by Total Sales:\n", sales_by_city.sort_values(by='TotalSales', ascending=False).head(), "\n")

# Sales by Product
sales_by_product = df.groupby('Product')['TotalSales'].sum().reset_index()
print("Top Products by Total Sales:\n", sales_by_product.sort_values(by='TotalSales', ascending=False).head(), "\n")
