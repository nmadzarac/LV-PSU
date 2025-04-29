
#Potrebno je izgraditi potpuno konvolucijsku neuronsku mrežu na temelju MNIST skupa podataka te izvršiti njenu
#evaluaciju. U prilogu vježbe nalazi se skripta 8.1. koja učitava MNIST skup podataka. Dopunite skriptu na odgovarajućim
#mjestima:
#1) Izgradite konvolucijsku neuronsku mreže pomoću Keras API. Struktura mreže je dana slikom 8.1. Prilikom
#treniranja neuronske mreže trebate koristiti 10% podatkovnih primjera za validaciju mreže.
#2) Dodajte callback kojim ćete pratiti točnost klasifikacije na skupu za učenje i skupu za validaciju u Tensoboardu.
#3) Dodajte callback za pohranjivanje najboljeg modela na temelju točnosti klasifikacije na validacijskom skupu.
#4) Pokrenite proces treniranja mreže te pratite tijek treniranja u Tensorboard-u. Provjerite je li pohranjen na disk
#najbolji model.
#5) Izračunajte točnost najboljeg modela (mreže) na skupu podataka za učenje i skupu podataka za testiranje.
#6) Prikažite matricu zabune na skupu podataka za učenje i na skupu podataka za testiranje. Komentirajte dobivene
#rezultate.


import tensorflow as tf
from tensorflow.keras import layers, models, callbacks
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, accuracy_score
import datetime
import os

# 1. Učitavanje i priprema podataka
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalizacija i reshaping (dodajemo kanal)
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)

# Kategorizacija (one-hot encoding)
y_train_cat = to_categorical(y_train, 10)
y_test_cat = to_categorical(y_test, 10)

# 2. Izgradnja modela (Fully Convolutional Network)
model = models.Sequential([
    layers.Conv2D(32, kernel_size=(3,3), activation='relu', input_shape=(28,28,1)),
    layers.Conv2D(64, kernel_size=(3,3), activation='relu'),
    layers.MaxPooling2D(pool_size=(2,2)),
    layers.Dropout(0.25),
    
    layers.Conv2D(128, kernel_size=(3,3), activation='relu'),
    layers.GlobalAveragePooling2D(),
    layers.Dropout(0.5),
    layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

# 3. Callback-ovi za TensorBoard i čuvanje modela
log_dir = "logs/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_cb = callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

checkpoint_cb = callbacks.ModelCheckpoint(
    'best_model.h5',
    monitor='val_accuracy',
    save_best_only=True,
    mode='max',
    verbose=1
)

# 4. Treniranje modela s 10% podataka za validaciju
history = model.fit(
    x_train, y_train_cat,
    validation_split=0.1,
    epochs=10,
    batch_size=128,
    callbacks=[tensorboard_cb, checkpoint_cb]
)

# 5. Učitavanje najboljeg modela i evaluacija
best_model = tf.keras.models.load_model('best_model.h5')

train_pred = best_model.predict(x_train)
test_pred = best_model.predict(x_test)

train_labels = np.argmax(train_pred, axis=1)
test_labels = np.argmax(test_pred, axis=1)

train_acc = accuracy_score(y_train, train_labels)
test_acc = accuracy_score(y_test, test_labels)

print(f"\nTočnost na SKUPU ZA UČENJE: {train_acc:.4f}")
print(f"Točnost na TESTNOM SKUPU: {test_acc:.4f}")

# 6. Matrice zabune
def plot_confusion_matrix(y_true, y_pred, title):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8,6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.xlabel("Predviđeno")
    plt.ylabel("Stvarno")
    plt.title(title)
    plt.show()

plot_confusion_matrix(y_train, train_labels, "Matrica zabune - Skup za učenje")
plot_confusion_matrix(y_test, test_labels, "Matrica zabune - Testni skup")
