import pandas as pd
import matplotlib.pyplot as plt

# Read the Iris dataset
df = pd.read_csv('iris.csv')

# Display the first 5 rows of the dataset
print("First 5 rows:")
print(df.head())

# Display the last 5 rows of the dataset
print("\nLast 5 rows:")
print(df.tail())

# Display the information about the dataset
print("\nDataset Information:")
print(df.info())

# Display the overview of the values of each column
print("\nColumn Overview:")
print(df.describe())

# Visualize the dataset using plot()
df.plot()
plt.title("Iris Dataset Visualization")
plt.show()
