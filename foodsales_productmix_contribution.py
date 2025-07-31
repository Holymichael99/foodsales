import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and prepare data
file_path = "Sampledatafoodslaes.xlsx"
df = pd.read_excel(file_path, sheet_name="FoodSales")
df["Sales"] = df["UnitPrice"] * df["Quantity"]

# Category Contribution
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False).reset_index()

# Product Contribution (Pareto)
product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False).reset_index()
product_sales["CumulativeSales"] = product_sales["Sales"].cumsum()
product_sales["CumulativePerc"] = 100 * product_sales["CumulativeSales"] / product_sales["Sales"].sum()

# Plot 1: Category Contribution
plt.figure(figsize=(10, 5))
sns.barplot(data=category_sales, x="Category", y="Sales", palette="pastel")
plt.title("Category Contribution to Total Sales")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot 2: Pareto Chart (Top Products)
plt.figure(figsize=(12, 6))
sns.barplot(data=product_sales, x="Product", y="Sales", color="skyblue")
plt.plot(product_sales["CumulativePerc"].values, color="red", marker="o")
plt.axhline(80, color="gray", linestyle="--", label="80% Threshold")
plt.title("Pareto Analysis: Product Contribution to Sales")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()