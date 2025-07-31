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
