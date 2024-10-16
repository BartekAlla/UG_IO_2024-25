import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Load the iris dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris_data = pd.read_csv(url, names=column_names)

# Set the colors for each species
species_colors = {'Iris-setosa': 'r', 'Iris-versicolor': 'g', 'Iris-virginica': 'b'}

# Function to plot data
def plot_data(data, title, ax):
    for species, color in species_colors.items():
        subset = data[data['species'] == species]
        ax.scatter(subset['sepal_length'], subset['sepal_width'],
                   color=color, label=species)
    ax.set_title(title)
    ax.set_xlabel('Sepal Length')
    ax.set_ylabel('Sepal Width')
    ax.legend()

# Plot original data
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

plot_data(iris_data, 'Original Iris Dataset', axs[0])

# Min-Max normalization
scaler_min_max = MinMaxScaler()
iris_data[['sepal_length', 'sepal_width']] = scaler_min_max.fit_transform(iris_data[['sepal_length', 'sepal_width']])
plot_data(iris_data, 'Min-Max Normalized Iris Dataset', axs[1])

# Z-score scaling
scaler_z_score = StandardScaler()
iris_data[['sepal_length', 'sepal_width']] = scaler_z_score.fit_transform(iris_data[['sepal_length', 'sepal_width']])
plot_data(iris_data, 'Z-Score Scaled Iris Dataset', axs[2])

plt.tight_layout()
plt.show()
