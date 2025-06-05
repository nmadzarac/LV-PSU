#U zasebnoj skripti učitajte mrežu iz drugog zadatka te pokušajte klasificirati sliku nekog prometnog znaka (npr. pronađite
#sliku prometnog znaka na internetu).

import tensorflow as tf
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Učitavanje treniranog modela
model = tf.keras.models.load_model("best_model.h5")

# Učitavanje slike prometnog znaka (putanja do tvoje slike)
img_path = "znak.jpg"  # promijeni u stvarnu putanju
img = cv2.imread(img_path)

# Provjera i priprema slike
img = cv2.resize(img, (48, 48))         # Resize na očekivanu veličinu
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # BGR → RGB ako koristiš OpenCV
img = img.astype("float32") / 255.0     # Normalizacija
img = np.expand_dims(img, axis=0)       # Dodavanje batch dimenzije (1, 48, 48, 3)

# Klasifikacija
pred = model.predict(img)
predicted_class = np.argmax(pred)

# Prikaz slike i predikcije
plt.imshow(img[0])
plt.title(f"Predviđena klasa: {predicted_class}")
plt.axis("off")
plt.show()
