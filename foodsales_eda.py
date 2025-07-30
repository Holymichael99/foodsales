# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Optional: set plot style
sns.set(style="whitegrid")

# Load the Excel file
file_path = "Sampledatafoodslaes.xlsx"
data = pd.read_excel(file_path, sheet_name="FoodSales")

# --------------------------------------------
# 1. Dataset Overview
# --------------------------------------------

print("Data Shape:", data.shape)
print("\nData Types:\n", data.dtypes)
print("\nMissing Values:\n", data.isnull().sum())
print("\nDuplicate Rows:", data.duplicated().sum())

# --------------------------------------------
# 2. Descriptive Statistics
# --------------------------------------------

print("\nSummary Statistics:\n", data.describe())

# --------------------------------------------
# 3. Frequency Counts
# --------------------------------------------

print("\nRegion Counts:\n", data['Region'].value_counts())
print("\nCity Counts:\n", data['City'].value_counts())
print("\nCategory Counts:\n", data['Category'].value_counts())

# --------------------------------------------
# 4. Feature Engineering
# --------------------------------------------

# Ensure OrderDate is datetime
data['OrderDate'] = pd.to_datetime(data['OrderDate'])

# Create new features
data['TotalSales'] = data['Quantity'] * data['UnitPrice']
data['Month'] = data['OrderDate'].dt.month_name().str[:3]
data['Year'] = data['OrderDate'].dt.year

# --------------------------------------------
# 5. Distributions (Histograms & Box Plots)
# --------------------------------------------

# Histogram: Quantity
plt.figure(figsize=(6, 4))
sns.histplot(data['Quantity'], bins=30, color='skyblue', kde=False)
plt.title("Distribution of Quantity")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Histogram: Unit Price
plt.figure(figsize=(6, 4))
sns.histplot(data['UnitPrice'], bins=30, color='salmon', kde=False)
plt.title("Distribution of Unit Price")
plt.xlabel("Unit Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Boxplot: Quantity by Category
plt.figure(figsize=(6, 4))
sns.boxplot(x='Category', y='Quantity', data=data, palette='Greens')
plt.title("Quantity by Category")
plt.tight_layout()
plt.show()

# Boxplot: Unit Price by Category
plt.figure(figsize=(6, 4))
sns.boxplot(x='Category', y='UnitPrice', data=data, palette='Reds')
plt.title("Unit Price by Category")
plt.tight_layout()
plt.show()


# --------------------------------------------
# 6. Correlation Matrix
# --------------------------------------------

plt.figure(figsize=(5, 4))
corr = data[['Quantity', 'UnitPrice', 'TotalSales']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()

# --------------------------------------------
# 7. Visualizations of Trends
# --------------------------------------------

# Line plot: Sales over time
plt.figure(figsize=(8, 4))
daily_sales = data.groupby('OrderDate')['TotalSales'].sum().reset_index()
sns.lineplot(x='OrderDate', y='TotalSales', data=daily_sales, color='blue')
plt.title("Sales Over Time")
plt.tight_layout()
plt.show()

# Bar plot: Monthly sales by year
monthly_sales = data.groupby(['Year', 'Month'])['TotalSales'].sum().reset_index()
# Order months
months_ordered = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
monthly_sales['Month'] = pd.Categorical(monthly_sales['Month'], categories=months_ordered, ordered=True)
monthly_sales = monthly_sales.sort_values(['Year', 'Month'])

plt.figure(figsize=(10, 5))
sns.barplot(x='Month', y='TotalSales', hue='Year', data=monthly_sales)
plt.title("Monthly Sales by Year")
plt.tight_layout()
plt.show()