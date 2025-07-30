import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style
sns.set(style="whitegrid")

# Load the Excel data
file_path = "Sampledatafoodslaes.xlsx"
df = pd.read_excel(file_path, sheet_name="FoodSales")

# Preprocessing
df['TotalSales'] = df['Quantity'] * df['UnitPrice']

# ------------------------------------------------------
# 1. Total Volume Sold by Category
# ------------------------------------------------------
volume_by_category = df.groupby('Category')['Quantity'].sum().reset_index()
print("Volume Sold by Category:\n", volume_by_category, "\n")

plt.figure(figsize=(6, 4))
sns.barplot(x='Category', y='Quantity', data=volume_by_category, palette="Blues_d")
plt.title("Total Volume Sold by Category")
plt.ylabel("Quantity Sold")
plt.tight_layout()
plt.show()

# ------------------------------------------------------
# 2. Total Revenue by Category
# ------------------------------------------------------
revenue_by_category = df.groupby('Category')['TotalSales'].sum().reset_index()
print("Revenue by Category:\n", revenue_by_category, "\n")

plt.figure(figsize=(6, 4))
sns.barplot(x='Category', y='TotalSales', data=revenue_by_category, palette="Greens")
plt.title("Total Revenue by Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# ------------------------------------------------------
# 3. Price Distribution by Category
# ------------------------------------------------------
plt.figure(figsize=(8, 5))
sns.boxplot(x='Category', y='UnitPrice', data=df, palette="Oranges")
plt.title("Unit Price Distribution by Category")
plt.ylabel("Unit Price")
plt.tight_layout()
plt.show()
