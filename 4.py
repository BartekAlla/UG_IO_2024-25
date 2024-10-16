from sklearn import datasets
from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt

iris = datasets.load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target, name='FlowerType')
print(X.head())
# pca_iris = PCA(n_components=3).fit(iris.data)
pca_iris = PCA(n_components=2).fit(iris.data)
# pca_iris = PCA(n_components=1).fit(iris.data)
# pca_iris = PCA(n_components=4).fit(iris.data)
print("Used PCA:")
print(pca_iris)
print("PCA variance ratio:")
print(pca_iris.explained_variance_ratio_)
print("PCA components:")
print(pca_iris.components_)
print("Dataset after transform:")
print(pca_iris.transform(iris.data))

# Aby zachować minimum 95% wariancji z datasetu iris można usunąc 2 kolumny.
# Wariancja dla 4 kolumn [0.92461872 0.05306648 0.01710261 0.00521218] wynosi: 1
# Wariancja dla 3 kolumn [0.92461872 0.05306648 0.01710261] wynosi około: 0.92 + 0.05 + 0.02 = 0.99 - 1% straty informacji
# Wariancja dla 2 kolumn [0.92461872 0.05306648] wynosi około: 0.92 + 0.05 = 0.97 - 3% straty informacji
# Wariancja dla 1 kolumny [0.92461872] wynosi około: 0.92  - 8% straty informacji
# Jak widać dla 3 kolumn strata informacji strata informacji jest znikoma na poziome 1%, więc można usunąc kolejną
# kolumna. Rozważając usunięcie 3 kolumn strata informacji wyniesie 8% co przekracza założenia.
# Sumaryczna wariancja dla wszystkich komponentów = 1 - [0.92461872 0.05306648 0.01710261 0.00521218]
# Strata informacji dla:
#   - 1 usuniętej kolumny = 0.00521218
#   - 2 usuniętych kolumn = 0.01710261 + 0.00521218 = 0.022313828
#   - 3 usuniętych kolumn = 0.05306648 + 0.01710261 + 0.00521218 = 0.075380308

# Plot
iris_df = pd.DataFrame(pca_iris.transform(iris.data), columns=['PC1', 'PC2'])
iris_df['FlowerType'] = iris.target
plt.figure(figsize=(8, 6))
colors = ['blue', 'cyan', 'orange']
labels = ['Setosa', 'Versicolor', 'Virginica']
for i, color, label in zip([0, 1, 2], colors, labels):
    subset = iris_df[iris_df['FlowerType'] == i]
    plt.scatter(subset['PC1'], subset['PC2'], c=color, label=label, s=50)
plt.title("PCA of IRIS dataset")
plt.legend()
plt.grid(True)
plt.show()