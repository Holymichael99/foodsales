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
