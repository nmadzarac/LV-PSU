#Izradite konvolucijsku mrežu sa slike 9.2. (mreža ima ukupno 1 358 155 parametara). Prilikom treniranja mreže koristite
#20% primjera za validaciju te odabir najboljeg modela pomoću ModelCheckpoint callbacka. Koristite Tensorboard
#callback za nadzor treniranja mreže. Na kraju evaluirajte mrežu na testnom skupu: ispišite točnost klasifikacije na testnim
#podacima te dobivenu matricu zabune.


import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense
from tensorflow.keras.callbacks import ModelCheckpoint, TensorBoard
from sklearn.metrics import confusion_matrix, classification_report
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Pretpostavimo da su X_train, y_train, X_test, y_test već učitani i pripremljeni
# One-hot kodiranje labela ako nije već napravljeno:
# y_train = tf.keras.utils.to_categorical(y_train, num_classes=43)
# y_test = tf.keras.utils.to_categorical(y_test, num_classes=43)

# Model arhitektura
model = Sequential()

for filters in [32, 64, 128]:
    model.add(Conv2D(filters=filters, kernel_size=(3, 3), padding='same', activation='relu', input_shape=(48, 48, 3) if filters == 32 else None))
    model.add(Conv2D(filters=filters, kernel_size=(3, 3), padding='valid', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=2))
    model.add(Dropout(0.2))

model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(43, activation='softmax'))

# Kompilacija modela
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Callback funkcije
checkpoint = ModelCheckpoint("best_model.h5", save_best_only=True, monitor="val_accuracy", mode="max")
tensorboard = TensorBoard(log_dir="./logs")
callbacks = [checkpoint, tensorboard]

# Treniranje modela
history = model.fit(
    X_train, y_train,
    epochs=20,
    batch_size=64,
    validation_split=0.2,
    callbacks=callbacks
)

# Učitavanje najboljeg modela
model.load_weights("best_model.h5")

# Evaluacija na testnom skupu
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Testna točnost: {accuracy:.4f}")

# Predikcije i matrica zabune
y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)
y_true = np.argmax(y_test, axis=1)

conf_mat = confusion_matrix(y_true, y_pred_classes)
print("Matrica zabune:\n", conf_mat)
print("\nKlasifikacijski izvještaj:\n", classification_report(y_true, y_pred_classes))

# Prikaz matrice zabune kao heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(conf_mat, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Matrica zabune')
plt.show()
