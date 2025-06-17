#Primijenite scikit-learn kmeans metodu za kvantizaciju boje na slici. Proučite kod 6.2. iz priloga vježbe te ga primijenite
#za kvantizaciju boje na slici example_grayscale.png koja dolazi kao prilog ovoj vježbi. Mijenjajte broj klastera.
#Što primjećujete? Izračunajte kolika se kompresija ove slike može postići ako se koristi 10 klastera.
#Pomoću sljedećeg koda možete učitati sliku:
#import matplotlib.image as mpimg
#imageNew = mpimg.imread('example_grayscale.png')

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.cluster import KMeans

imageNew = mpimg.imread('C:/Users/student/Desktop/LV6/example_grayscale.png')

if len(imageNew.shape) == 2:
    imageNew = np.stack([imageNew] * 3, axis=-1)

pikseli = imageNew.reshape((-1, 3))

broj_klastera = 10
model = KMeans(n_clusters=broj_klastera, n_init=1, random_state=42)
model.fit(pikseli)

centri = model.cluster_centers_.astype(int)
etikete = model.labels_
kvantizirana_slika = centri[etikete].reshape(imageNew.shape)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(imageNew)
plt.title("Izvorna slika")

plt.subplot(1, 2, 2)
plt.imshow(kvantizirana_slika)
plt.title(f"Kvantizirana slika (k={broj_klastera})")

plt.show()

velicina_originala = imageNew.size * imageNew.itemsize
velicina_kvantizirane = broj_klastera * pikseli.shape[0] * pikseli.itemsize
kompresija = velicina_originala / velicina_kvantizirane

print(f"Kompresijski omjer za {broj_klastera} klastera: {kompresija:.2f}x")
