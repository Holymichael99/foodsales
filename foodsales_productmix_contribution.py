import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and prepare data
file_path = "Sampledatafoodslaes.xlsx"
df = pd.read_excel(file_path, sheet_name="FoodSales")
df["Sales"] = df["UnitPrice"] * df["Quantity"]

# Category Contribution
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False).reset_index()