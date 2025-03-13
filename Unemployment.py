# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("Unemployment_Rate_upto_11_2020.csv")

# Display the first five rows
print("Dataset Preview:")
print(data.head())

# Data Cleaning
data.columns = ["Region", "Date", "Frequency", "Estimated Unemployment Rate", 
                "Estimated Employed", "Estimated Labour Participation Rate", "Area"]
data["Date"] = pd.to_datetime(data["Date"], format="%d-%m-%Y")

# Data Overview
print("\nData Info:")
print(data.info())

# Handling Missing Values
print("\nMissing Values:")
print(data.isnull().sum())

# Visualizing the Unemployment Rate
plt.figure(figsize=(12, 6))
sns.lineplot(data=data, x="Date", y="Estimated Unemployment Rate", hue="Region")
plt.title("Unemployment Rate Trends Across Regions")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.legend(title="Region")
plt.grid(True)
plt.show()

# Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Matrix")
plt.show()

# Regional Analysis
plt.figure(figsize=(10, 6))
sns.barplot(data=data, x='Region', y='Estimated Unemployment Rate')
plt.xticks(rotation=90)
plt.title("Unemployment Rate by Region")
plt.show()
