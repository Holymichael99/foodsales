import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style
sns.set(style="whitegrid")

# Load Excel data
file_path = "Sampledatafoodslaes.xlsx"  # Make sure this file is in the same folder
df = pd.read_excel(file_path, sheet_name="FoodSales")

# Convert OrderDate to datetime and create TotalSales
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['TotalSales'] = df['Quantity'] * df['UnitPrice']
