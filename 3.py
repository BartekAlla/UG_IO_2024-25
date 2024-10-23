import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.naive_bayes import GaussianNB

df = pd.read_csv("iris.csv")
# a)
# podzial na zbior testowy (30%) i treningowy (70%), ziarno losowosci = 298837
(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=298837)

x_train = train_set[:, :-1]
y_train = train_set[:, -1]

x_test = test_set[:, :-1]
y_test = test_set[:, -1]


# b)

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
    print("Confusion Matrix:")
    print(conf_matrix)
    print()


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
print("Confusion Matrix:")
print(nb_conf_matrix)


# Dla DD - accuracy 95,56%
# Dla 3-NN - accuracy 95,56%
# Dla 5-NN - accuracy 97,78%
# Dla 11-NN - accuracy 95,56%
# Dla Naive Bayes - accuracy 93,33%
# Najlepszy wynik pod względem dokładności dla irys.csv wykazał kNN dla 5 sąsiadów.