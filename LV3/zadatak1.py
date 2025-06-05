#Za mtcars skup podataka napišite programski kod koji će odgovoriti na sljedeća pitanja:
#1. Kojih 5 automobila ima najveću potrošnju? (koristite funkciju sort)
#2. Koja tri automobila s 8 cilindara imaju najmanju potrošnju?
#3. Kolika je srednja potrošnja automobila sa 6 cilindara?
#4. Kolika je srednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs?
#5. Koliko je automobila s ručnim, a koliko s automatskim mjenjačem u ovom skupu podataka?
#6. Koliko je automobila s automatskim mjenjačem i snagom preko 100 konjskih snaga?
#7. Kolika je masa svakog automobila u kilogramima?


import pandas as pd
import numpy as np

mtcars = pd.read_csv('C:\\Users\\student\\Desktop\\LV3\\mtcars.csv.csv')

print(mtcars.sort_values(by='mpg').head(5))
print(mtcars[mtcars.cyl == 8].sort_values(by='mpg').tail(3))

cyl6 = mtcars[mtcars.cyl == 6]
cyl6 = cyl6.iloc[:, 1:2]
print(cyl6.mean())

car1 = mtcars[(mtcars.cyl == 4) & (mtcars.wt > 2.000) & (mtcars.wt < 2.200)]
car1 = car1.iloc[:, 1:2]
print(car1.mean())

manual = 0
automatik = 0
vrsta = mtcars.sort_values(by='am')
for car in vrsta.am:
    if car == 0:
        manual += 1
    elif car == 1:
        automatik += 1

print('automatika ima', automatik, 'manualaca ima', manual)

car6 = mtcars[(mtcars.am == 1) & (mtcars.hp > 100)]
print('ima ih', len(car6))

car_kg = mtcars.wt * 1000 / 2.20462262
print(car_kg)
