#U prilogu vježbe nalazi se skripta 8.2. koja učitava izgrađenu mrežu i sliku test.png sa diska. Dodajte u skriptu kod
#kojim ćete klasificirati sliku pomoću mreže. Promijenite sliku pomoću nekog grafičkog alata (npr. nacrtajte znamenku 2
#u Paintu) i ponovo pokrenite skriptu. Pokušajte sa svim znamenkama. Kako položaj ili rotacija znamenke utječe na rezultat
#klasifikacije?

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.transform import resize
from skimage import color
from tensorflow.keras import models
import numpy as np

putanja_slike = 'test.png'

slika_ucitana = mpimg.imread(putanja_slike)
siva_slika = color.rgb2gray(slika_ucitana)
smanjena_slika = resize(siva_slika, (28, 28))

plt.imshow(smanjena_slika, cmap=plt.get_cmap('gray'))
plt.axis('off')
plt.show()

ulaz = smanjena_slika.reshape(1, 28, 28, 1)
ulaz = ulaz.astype('float32')

mreza = models.load_model('best_model.h5')

rezultat = mreza.predict(ulaz)
predikcija = np.argmax(rezultat)

print(f'Predikcija: {predikcija}')
