import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import plot_model


# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Preprocess the data
# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Encode the labels
encoder = OneHotEncoder(sparse_output=False)
y_encoded = encoder.fit_transform(y.reshape(-1, 1))

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.3, random_state=42)

# Define the model
model = Sequential([
    Dense(64, activation='tanh', input_shape=(X_train.shape[1],)),
    Dense(64, activation='tanh'),
    Dense(y_encoded.shape[1], activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=100, batch_size=16, validation_split=0.2)

# Evaluate the model on the test set
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Accuracy: {test_accuracy*100:.2f}%")

# Plot the learning curve
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='train accuracy')
plt.plot(history.history['val_accuracy'], label='validation accuracy')
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.grid(True, linestyle='--', color='grey')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='train loss')
plt.plot(history.history['val_loss'], label='validation loss')
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.grid(True, linestyle='--', color='grey')
plt.legend()

plt.tight_layout()
plt.show()

# Save the model
model.save('iris_model.h5')

# Plot and save the model architecture
plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)

# a) Skaluje każdą cechę, aby miała średnią 0 i odchylenie standardowe 1. Zmniejsza to ryzyko zdominowania cech innymi.

# b) Zamienia typ irysa na wktor w reprezentacji [-1, 0, 1], zamiast ciągu znaków. Kodowanie "one hot" zamienia wartości kategorii na wektor binarny.

# c) Warstwa wejściowa ma tyle  neuronów ile jest cech w zbiorze wejściowym - dla irysów 4. X_train_shape[1] - liczba kolumn w X_trai. Warstwa
# wyjściowa ma tyle neuronów ile klas wyjściowych - ile one hot tworzy kolumns - 3

# d) przed zmianą daje: accuracy: 0.9665 - loss: 0.0837 - val_accuracy: 0.9048 - val_loss: 0.2885
# dla tanh: accuracy: 0.9704 - loss: 0.0762 - val_accuracy: 1.0000 - val_loss: 0.0634
# dla sigmoid: accuracy: 0.9565 - loss: 0.2193 - val_accuracy: 0.8095 - val_loss: 0.3540

# e) Dla Adam: 0.9704 - loss: 0.0762 - val_accuracy: 1.0000 - val_loss: 0.0634
# dla SGD: accuracy: 0.9174 - loss: 0.2791 - val_accuracy: 0.9048 - val_loss: 0.3163
# dla ftrl: accuracy: 0.3348 - loss: 1.0986 - val_accuracy: 0.3333 - val_loss: 1.0986
# dla adagrad: accuracy: 0.8367 - loss: 0.5137 - val_accuracy: 0.8095 - val_loss: 0.5717

# dla categorical_crossentropy: 0.9704 - loss: 0.0762 - val_accuracy: 1.0000 - val_loss: 0.0634
# dla mean_squared_error: accuracy: 0.9470 - loss: 0.0213 - val_accuracy: 1.0000 - val_loss: 0.0150
# dla mean_absolute_error: 0.9195 - loss: 0.0501 - val_accuracy: 1.0000 - val_loss: 0.0319

# Rózne optymalizatory i funkcje dają różne wyniki
# prędkośc uczenia można dostowować regulując learning_rate, ale może spowodować to niestabilnośc.

# f) 4:accuracy: 0.9664 - loss: 0.0874 - val_accuracy: 1.0000 - val_loss: 0.0272
#   8:accuracy: 0.9628 - loss: 0.0629 - val_accuracy: 1.0000 - val_loss: 0.0343
#   16: accuracy: 0.9770 - loss: 0.0567 - val_accuracy: 1.0000 - val_loss: 0.0496
# Widac na wykresach, że wraz ze wzrostem rozmiarem partii, zwiększa się stabilność dkoładności, nie ma takich wahań.
# Dokładnośc na zbiorze treningowych i walidacyjnym zaczynają sie pokrywać, a wykres straty jest zbliżony dla zbioru
# treningowego i walidacyjnego, gdzie dla mniejszego rozmiaru się rozjeżdżały

# g) Dla konfiguracji tanh, adam, categorical_crossentropy, batch_size=16, Widać na wykresach, że sieć dobrze się uczy
# - n=rozbieżności pomiędzy zbiorem testowym, a walidacyjnym są znikome.
# najlepzy wynik sieć osiągneła dla epoki 95 - accuracy: 0.9874 - loss: 0.0503 - val_accuracy: 1.0000 - val_loss: 0.0583
# można już zauważyć efekty przeuczenia sieci - coraz bardziej rozbieżna strata

# h)
# 1. Załadowanie irysów
# 2. Podział na dane i wynik
# 3. Skalowanie cech
# 4. onehot na wartosci -1, 0, 1 dla irysów
# 5. Podział na zbiór treningowy i testowy 70, 30 %
# 6. Załadowanie modelu
# 7. Trenowanie modelu na zbiorze treningowym
# 8. Zapis modelu do pliku
# 9. Ewaluacja modelu na grupie testowej i wyświetlenie dokładnośic i straty


