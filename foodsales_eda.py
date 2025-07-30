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