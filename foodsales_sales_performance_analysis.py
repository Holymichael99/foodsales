# food_sales_analysis.py

import pandas as pd

# Load Excel file and select the 'FoodSales' sheet
file_path = "Sampledatafoodslaes.xlsx"  # Ensure this file is in the same directory
df = pd.read_excel(file_path, sheet_name="FoodSales")