from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
from keras.optimizers import SGD, Adam, RMSprop
from keras.callbacks import ModelCheckpoint
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns
from tensorflow.keras.preprocessing.image import ImageDataGenerator


def define_model(optimizer='SGD', activation='relu', use_dropout=False):
    model = Sequential()

    model.add(Conv2D(32, (3, 3), activation=activation, kernel_initializer='he_uniform', padding='same',
                     input_shape=(200, 200, 3)))
    model.add(MaxPooling2D((2, 2)))

    if use_dropout:
        model.add(Dropout(0.5))

    model.add(Flatten())
    model.add(Dense(128, activation=activation, kernel_initializer='he_uniform'))

    if use_dropout:
        model.add(Dropout(0.5))

    model.add(Dense(1, activation='sigmoid'))  # Binary classification

    if optimizer == 'SGD':
        opt = SGD(learning_rate=0.001, momentum=0.9)
    elif optimizer == 'Adam':
        opt = Adam(learning_rate=0.001)
    elif optimizer == 'RMSprop':
        opt = RMSprop(learning_rate=0.001)

    model.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])

    return model


def summarize_diagnostics(history, model_name):
    plt.subplot(211)
    plt.title('Cross Entropy Loss')
    plt.plot(history.history['loss'], color='blue', label='train')
    plt.plot(history.history['val_loss'], color='orange', label='test')

    plt.subplot(212)
    plt.title('Classification Accuracy')
    plt.plot(history.history['accuracy'], color='blue', label='train')
    plt.plot(history.history['val_accuracy'], color='orange', label='test')

    plt.savefig(f'{model_name}_plot.png')
    plt.close()


def plot_confusion_matrix(y_true, y_pred, model_name):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(6, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False, xticklabels=['Dog', 'Cat'],
                yticklabels=['Dog', 'Cat'])
    plt.title(f'Confusion Matrix for {model_name}')
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.savefig(f'{model_name}_confusion_matrix.png')
    plt.close()


def run_experiment(optimizer, activation, use_dropout):
    model = define_model(optimizer, activation, use_dropout)

    datagen = ImageDataGenerator(rescale=1.0 / 255.0)
    train_it = datagen.flow_from_directory('dataset_dogs_vs_cats/train/', class_mode='binary', batch_size=64,
                                           target_size=(200, 200))
    test_it = datagen.flow_from_directory('dataset_dogs_vs_cats/test/', class_mode='binary', batch_size=64,
                                          target_size=(200, 200))

    model_checkpoint = ModelCheckpoint(f'{optimizer}_{activation}_dropout_{use_dropout}.keras', save_best_only=True)

    history = model.fit(train_it, steps_per_epoch=len(train_it), validation_data=test_it, validation_steps=len(test_it),
                        epochs=20, verbose=0, callbacks=[model_checkpoint])

    _, acc = model.evaluate(test_it, steps=len(test_it), verbose=0)
    print(f'{optimizer} - {activation} - Dropout: {use_dropout} > Accuracy: {acc * 100:.2f}%')

    summarize_diagnostics(history, f'{optimizer}_{activation}_dropout_{use_dropout}')

    y_true = test_it.classes
    y_pred = (model.predict(test_it, steps=len(test_it)) > 0.5).astype(int)

    plot_confusion_matrix(y_true, y_pred, f'{optimizer}_{activation}_dropout_{use_dropout}')


optimizers = ['SGD', 'Adam', 'RMSprop']
activations = ['relu', 'tanh', 'sigmoid']
dropouts = [False, True]

for optimizer in optimizers:
    for activation in activations:
        for use_dropout in dropouts:
            print(f'\nRunning experiment with {optimizer} optimizer, {activation} activation, dropout={use_dropout}')
            run_experiment(optimizer, activation, use_dropout)

# SGD - relu - Dropout: False > Accuracy: 71.92%
# SGD - relu - Dropout: True > Accuracy: 71.14%
# SGD - tanh - Dropout: False > Accuracy: 57.32%
# SGD - tanh - Dropout: True > Accuracy: 50.48%
# SGD - sigmoid - Dropout: False > Accuracy: 59.81%
# SGD - sigmoid - Dropout: True > Accuracy: 54.39%
# Adam - relu - Dropout: False > Accuracy: 66.65%
# Adam - relu - Dropout: True > Accuracy: 49.60%
# Adam - tanh - Dropout: False > Accuracy: 50.42%
