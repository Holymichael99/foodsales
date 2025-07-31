import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = "Sampledatafoodslaes.xlsx"
df = pd.read_excel(file_path, sheet_name="FoodSales")