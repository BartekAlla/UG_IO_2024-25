import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("diabetes.csv")
# a)
(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=298837)

# b)
mlp = MLPClassifier(hidden_layer_sizes=(6, 3), max_iter=500, random_state=298837, activation='relu')
x_train = train_set[:, :-1]
y_train = train_set[:, -1]
x_test = test_set[:, :-1]
y_test = test_set[:, -1]
scaler = StandardScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

# c)
mlp.fit(x_train, y_train)

# d)
y_pred = mlp.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion matrix:\n", conf_matrix)

# e)
# K-Neighbors
def knn_classifier(x_train, y_train, x_test, y_test, k):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)
    return accuracy, conf_matrix


knn = [3, 5, 11]
results = {}

for k in knn:
    accuracy, conf_matrix = knn_classifier(x_train, y_train, x_test, y_test, k)
    results[k] = (accuracy, conf_matrix)

print("k-NN:")
for k in results:
    accuracy, conf_matrix = results[k]
    print(f"k={k}: Accuracy = {accuracy * 100:.2f}%")

# Maive Bayes
def naive_bayes_classifier(x_train, y_train, x_test, y_test):
    gnb = GaussianNB()
    gnb.fit(x_train, y_train)
    y_pred = gnb.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)
    return accuracy, conf_matrix


nb_accuracy, nb_conf_matrix = naive_bayes_classifier(x_train, y_train, x_test, y_test)

print("Naive Bayes:")
print(f"Accuracy = {nb_accuracy * 100:.2f}%")
# Neural network - Accuracy: 0.6926406926406926
# Confusion matrix:
# k-NN:
# k=3: Accuracy = 70.13%
# k=5: Accuracy = 71.86%
# k=11: Accuracy = 74.89%
# Naive Bayes:
# Accuracy = 81.39%
# W tym przypadku bayes daje lepsze wyniki, niż sieć neuronowa

mlp1 = MLPClassifier(hidden_layer_sizes=(7,3), max_iter=500, random_state=298837, activation='identity')
mlp1.fit(x_train, y_train)
y_pred1 = mlp1.predict(x_test)
accuracy1 = accuracy_score(y_test, y_pred1)
print("Accuracy:", accuracy1)
conf_matrix = confusion_matrix(y_test, y_pred1)
print("Confusion matrix:\n", conf_matrix)
# Najlepszy wynik - 80,5% udało mi się uzyskać dla dwóch warstw po 7 i 3 neurony, dla funckji aktywacji identity
# f)
# Uważam, że w przypadku diagnozowania cukrzycy gorszy jest błąd FN, ponieważ może doprowadzić, do nie leczenia chorej osoby.
# dla pierwszej sieci wychodzi więcej FN, a dla drugiej FP.
