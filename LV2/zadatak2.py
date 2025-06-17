#U direktoriju PSU_LV/LV2/ nalazi se datoteka mtcars.csv koja sadrži različita mjerenja provedena na 32
#automobila (modeli 1973-74). Opis pojedinih varijabli nalazi se u datoteci mtcars_info.txt.
#a) Učitajte datoteku mtcars.csv pomoću:
#data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6),
#delimiter=",", skiprows=1)
#b) Prikažite ovisnost potrošnje automobila (mpg) o konjskim snagama (hp) pomoću naredbe
#matplotlib.pyplot.scatter.
#c) Na istom grafu prikažite i informaciju o težini pojedinog vozila (npr. veličina točkice neka bude u skladu sa
#težinom wt).
#d) Izračunajte minimalne, maksimalne i srednje vrijednosti potrošnje (mpg) automobila.
#e) Ponovite zadatak pod d), ali samo za automobile sa 6 cilindara (cyl).

import numpy as np
import matplotlib.pyplot as plt

try:
    data = np.loadtxt("LV-PSU/LV2/mtcars.csv", delimiter=",", skiprows=1, usecols=(1, 2, 3, 4, 5, 6))
except FileNotFoundError:
    print("Datoteka mtcars.csv nije pronađena.")
    exit()

mpg = data[:, 0]  # Miles per gallon
cyl = data[:, 1]  # Broj cilindara
hp = data[:, 3]   # Konjske snage
wt = data[:, 5]   # Težina vozila

plt.figure(figsize=(8, 6))
plt.scatter(mpg, hp, s=wt * 30, c='purple', alpha=0.7, edgecolors='w')
plt.xlabel("Potrošnja (mpg)")
plt.ylabel("Konjske snage (hp)")
plt.title("Ovisnost potrošnje o konjskim snagama (veličina = težina vozila)")
plt.grid(True)
plt.show()

print("SVE POTROŠNJE (mpg):")
print(f"Min: {np.min(mpg):.2f}")
print(f"Max: {np.max(mpg):.2f}")
print(f"Srednja vrijednost: {np.mean(mpg):.2f}")

mpg_6cyl = mpg[cyl == 6]

print("\nPOTROŠNJE ZA 6-CILINDRIČNE AUTOMOBILE:")
print(f"Min: {np.min(mpg_6cyl):.2f}")
print(f"Max: {np.max(mpg_6cyl):.2f}")
print(f"Srednja vrijednost: {np.mean(mpg_6cyl):.2f}")
