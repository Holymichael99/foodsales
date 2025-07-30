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