import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
file_path = "Sampledatafoodslaes.xlsx"
df = pd.read_excel(file_path, sheet_name="FoodSales")

# Create 'Sales' column

# Sales by Region
plt.subplot(1, 2, 1)
sns.barplot(data=region_summary, x="Region", y="Sales", palette="Blues_d")
plt.title("Total Sales by Region")
plt.ylabel("Sales")
plt.grid(True)

# Quantity by Region
plt.subplot(1, 2, 2)
sns.barplot(data=region_summary, x="Region", y="Quantity", palette="Greens_d")
plt.title("Total Quantity by Region")
plt.ylabel("Quantity")
plt.grid(True)

plt.tight_layout()
plt.show()

# --- City-wise Performance ---
city_summary = df.groupby("City")[["Sales", "Quantity"]].sum().reset_index()

plt.figure(figsize=(12, 5))

# Sales by City
plt.subplot(1, 2, 1)
sns.barplot(data=city_summary, x="City", y="Sales", palette="Purples_d")
plt.title("Total Sales by City")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid(True)

# Quantity by City
plt.subplot(1, 2, 2)
sns.barplot(data=city_summary, x="City", y="Quantity", palette="Oranges_d")
plt.title("Total Quantity by City")
plt.ylabel("Quantity")
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()