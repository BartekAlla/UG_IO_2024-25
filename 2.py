import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

df = pd.read_csv("iris.csv")
# a)
# podzial na zbior testowy (30%) i treningowy (70%), ziarno losowosci = 298837
(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=298837)
print("train_set")
print(train_set)
print("test_set")
print(test_set)

x_train = train_set[:, :-1]
y_train = train_set[:, -1]

x_test = test_set[:, :-1]
y_test = test_set[:, -1]

# b)
clf = DecisionTreeClassifier()

# c)
clf.fit(x_train, y_train)

# d)
tree_text = export_text(clf, feature_names=df.columns[:-1].tolist())
print("DD:")
print(tree_text)

# e)
accuracy = clf.score(x_test, y_test)
print(f"Accuracy using score: {accuracy * 100:.2f}%")

y_pred = clf.predict(x_test)
accuracy1 = accuracy_score(y_test, y_pred)
print(f"Accuracy using predict: {accuracy1 * 100:.2f}%")

# f)
conf_matrix = confusion_matrix(y_test, y_pred)
print(conf_matrix)
