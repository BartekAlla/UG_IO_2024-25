from keras.applications import ResNet50
from keras.models import Model
from keras.layers import Dense, Flatten, Dropout, MaxPooling2D, GlobalAveragePooling2D
from keras.optimizers import SGD
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import sys


def define_resnet_model():
    base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(200, 200, 3))
    for layer in base_model.layers:
        layer.trainable = False
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(128, activation='relu')(x)
    predictions = Dense(1, activation='sigmoid')(x)
    model = Model(inputs=base_model.input, outputs=predictions)
    opt = SGD(learning_rate=0.001, momentum=0.9)
    model.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])
    return model


def summarize_diagnostics(history):
    plt.subplot(211)
    plt.title('Cross Entropy Loss')
    plt.plot(history.history['loss'], color='blue', label='train')
    plt.plot(history.history['val_loss'], color='orange', label='test')
    plt.legend()
    plt.subplot(212)
    plt.title('Classification Accuracy')
    plt.plot(history.history['accuracy'], color='blue', label='train')
    plt.plot(history.history['val_accuracy'], color='orange', label='test')
    plt.legend()
    filename = sys.argv[0].split('/')[-1]
    plt.savefig(filename + '_resnet_plot.png')
    plt.show()


def run_test_harness():
    model = define_resnet_model()
    datagen = ImageDataGenerator(rescale=1.0 / 255.0)
    train_it = datagen.flow_from_directory('dataset_dogs_vs_cats/train/',
                                           class_mode='binary', batch_size=64, target_size=(200, 200))
    test_it = datagen.flow_from_directory('dataset_dogs_vs_cats/test/',
                                          class_mode='binary', batch_size=64, target_size=(200, 200))
    history = model.fit(train_it, steps_per_epoch=len(train_it),
                        validation_data=test_it, validation_steps=len(test_it),
                        epochs=10, verbose=1)
    _, acc = model.evaluate(test_it, steps=len(test_it), verbose=0)
    print('Accuracy with ResNet50: %.3f' % (acc * 100.0))
    summarize_diagnostics(history)


run_test_harness()

#Wybrano ResNet50
# Dodano GlobalAveragePooling2D - Zmniejsza wymiar danych wyjściowych.
# Warstwa ukryta Dense(128, activation='relu').
# Dense(1, activation='sigmoid') - Warstwa wyjściowa dla klasyfikacji binarnej.
# Accuracy with ResNet50: 57.877
# Dla sieci konwolucyjnej osiągnieto :
# SGD - relu - Dropout: False > Accuracy: 71.92% co wskazuej, że ResNet poradził sobie zdecydowanie gorzej


