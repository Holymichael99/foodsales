import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = "Sampledatafoodslaes.xlsx"
df = pd.read_excel(file_path, sheet_name="FoodSales")

# --- Price Sensitivity Analysis ---
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="UnitPrice", y="Quantity", hue="Category", alpha=0.7)
plt.title("Price Sensitivity: Unit Price vs Quantity")
plt.xlabel("Unit Price")
plt.ylabel("Quantity Sold")
plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()

# Correlation between UnitPrice and Quantity
correlation = df[["UnitPrice", "Quantity"]].corr().iloc[0,1]
print(f"📉 Correlation between Unit Price and Quantity: {correlation:.2f}")

# --- Category-Specific Price Trends ---
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x="Category", y="UnitPrice", palette="Set2")
plt.title("Category-specific Unit Price Distribution")
plt.xlabel("Category")
plt.ylabel("Unit Price")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
