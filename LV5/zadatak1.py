#Skripta 5.1. učitava skup podataka koji se nalazi u csv datoteci occupancy_processed.csv. Ova datoteka sadrži
#podatke koji su prikupljeni u prostoriji veličine 6m x 4.6m tijekom 4 dana [1]. Zbog jednostavnosti skup sadrži samo dva
#atributa: mjerenja dobivena sa senzora temperature i mjerenja sa senzora CO2. Izlazna (ciljna) veličina je zauzetost
#prostorije (0 – prazna prostorija, 1 – u prostoriji se nalazi barem jedna osoba). Cilj je izgraditi klasifikator koji će na
#temelju trenutnih mjerenja dobivenih sa senzora temperature i sa senzora CO2 procijeniti zauzetost prostorije.
#a) Pokrenite skriptu i pogledajte dobiveni dijagram raspršenja. Što primjećujete?
#b) Koliko podatkovnih primjera sadrži učitani skup podataka?
#c) Kakva je razdioba podatkovnih primjera po klasama?

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('occupancy_processed.csv')
print(len(df))

features = ['S3_Temp', 'S5_CO2']
target = 'Room_Occupancy_Count'
labels = ['Slobodna', 'Zauzeta']

X = df[features].values
y = df[target].values

plt.figure()
for cls in np.unique(y):
    idx = y == cls
    plt.scatter(X[idx, 0], X[idx, 1], label=labels[cls])

plt.xlabel('S3_Temp')
plt.ylabel('S5_CO2')
plt.title('Zauzetost prostorije')
plt.legend()
plt.show()
