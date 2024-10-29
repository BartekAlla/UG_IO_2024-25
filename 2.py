from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import numpy as np

# a)
iris = load_iris()
datasets = train_test_split(iris.data, iris.target, test_size=0.3, random_state=298837)

# b)
train_data, test_data, train_labels, test_labels = datasets
# 0 - Setosa, 1 - Versicolor, 2 - Virginica

# c)
scaler = StandardScaler()
scaler.fit(train_data)
train_data = scaler.transform(train_data)
test_data = scaler.transform(test_data)

# d)
mlp = MLPClassifier(hidden_layer_sizes=(2,), max_iter=1000, random_state=298837)
mlp.fit(train_data, train_labels)

# e)
predictions_test = np.round(mlp.predict(test_data))
print("Accuracy - 2 in 1 layer:", accuracy_score(predictions_test, test_labels))
# 95.6%

# f)
mlp1 = MLPClassifier(hidden_layer_sizes=(3,), max_iter=1000, random_state=298837)
mlp1.fit(train_data, train_labels)
predictions_test1 = np.round(mlp1.predict(test_data))
print("Accuracy - 3 in 1 layer:", accuracy_score(predictions_test1, test_labels))
# W przypadku random state dla mojego indeksu działa gorzej. Dla f) 0.88%

# g)
mlp2 = MLPClassifier(hidden_layer_sizes=(3,3), max_iter=1000, random_state=298837)
mlp2.fit(train_data, train_labels)
predictions_test2 = np.round(mlp2.predict(test_data))
print("Accuracy - 3 in 1 layer, 3 in 2 layer:", accuracy_score(predictions_test2, test_labels))
# Dla dwóch warstw po 3 neurony accuracy wynosi 31%, co jest znacznie niższym wynikiem niz w poprzednich podpunktach

