import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

# Loading MNIST dataset
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# pixel values to be between 0 and 1
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

# Building a simple neural network model
model = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compiling the mosel
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Training the model
model.fit(x_train, y_train, epochs=5, batch_size=32, validation_split=0.1)

# Model use on test data
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)

print(f'Test accuracy: {test_acc}')