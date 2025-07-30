# Load required libraries
library(readxl)
library(dplyr)
library(ggplot2)
library(tidyr)
library(lubridate)
library(corrplot)

# Load the Excel file and sheet
data <- read_excel("Sampledatafoodslaes.xlsx", sheet = "FoodSales")

# View structure
str(data)

# Shape of the dataset
cat("Rows:", nrow(data), " Columns:", ncol(data), "\n")

# Check for missing values
sapply(data, function(x) sum(is.na(x)))

# Check for duplicates
cat("Duplicates:", sum(duplicated(data)), "\n")

# Summary statistics for numerical columns
summary(select(data, Quantity, UnitPrice))

