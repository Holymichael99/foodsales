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

# --------------------------------------------
# Top/Bottom Products by Quantity Sold
# --------------------------------------------
quantity_summary = df.groupby('Product')['Quantity'].sum().reset_index()

top_quantity = quantity_summary.sort_values(by='Quantity', ascending=False).head(5)
bottom_quantity = quantity_summary.sort_values(by='Quantity', ascending=True).head(5)

print("Top 5 Products by Quantity Sold:\n", top_quantity, "\n")
print("Bottom 5 Products by Quantity Sold:\n", bottom_quantity, "\n")

# Plot Top 5 by Quantity
plt.figure(figsize=(8, 4))
sns.barplot(x='Quantity', y='Product', data=top_quantity, palette="Greens_r")
plt.title("Top 5 Products by Quantity Sold")
plt.tight_layout()
plt.show()

# Plot Bottom 5 by Quantity
plt.figure(figsize=(8, 4))
sns.barplot(x='Quantity', y='Product', data=bottom_quantity, palette="Reds_r")
plt.title("Bottom 5 Products by Quantity Sold")
plt.tight_layout()
plt.show()
