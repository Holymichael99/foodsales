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

