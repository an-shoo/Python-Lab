import pandas as pd
import matplotlib.pyplot as plt

# Assuming we have a dataset 'data.csv'
df = pd.read_csv('data.csv')

# Visualize the dataset using plot()
df.plot()
plt.title("Dataset Visualization")
plt.show()

# Draw the Scatter plot for the dataset on any column
df.plot.scatter(x='column1', y='column2')
plt.title("Scatter Plot")
plt.show()

# Display the scatter plot with different colors
colors = ['red', 'green', 'blue']
df.plot.scatter(x='column1', y='column2', c=colors)
plt.title("Scatter Plot with Colors")
plt.show()

# Draw the Histogram for the dataset on any column
df['column1'].plot.hist()
plt.title("Histogram")
plt.show()
