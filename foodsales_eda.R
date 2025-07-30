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

# Frequency counts for categorical variables
table(data$Region)
table(data$City)
table(data$Category)

# Feature Engineering
data <- data %>%
  mutate(
    TotalSales = Quantity * UnitPrice,
    OrderDate = as.Date(OrderDate),
    Month = month(OrderDate, label = TRUE),
    Year = year(OrderDate)
  )

# Histograms for Quantity and UnitPrice
ggplot(data, aes(x = Quantity)) + 
  geom_histogram(bins = 30, fill = "skyblue", color = "black") +
  theme_minimal() + ggtitle("Distribution of Quantity")

ggplot(data, aes(x = UnitPrice)) + 
  geom_histogram(bins = 30, fill = "salmon", color = "black") +
  theme_minimal() + ggtitle("Distribution of Unit Price")

 #Box plots for UnitPrice and Quantity by Category
ggplot(data, aes(x = Category, y = Quantity)) + 
  geom_boxplot(fill = "lightgreen") + 
  theme_minimal() + ggtitle("Quantity by Category")

ggplot(data, aes(x = Category, y = UnitPrice)) + 
  geom_boxplot(fill = "lightcoral") + 
  theme_minimal() + ggtitle("Unit Price by Category")

  # Correlation matrix (numerical only)
num_data <- select(data, Quantity, UnitPrice, TotalSales)
cor_matrix <- cor(num_data)
corrplot(cor_matrix, method = "circle", type = "lower")