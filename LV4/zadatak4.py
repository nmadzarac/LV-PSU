#Primjer 4.3. učitava skup podataka koji se nalazi u datoteci car_processed.csv u dataframe. Ova datoteka sadrži
#podatke koji su prikupljeni s online platforme cardekho.com koja se bavi prodajom vozila u Indiji. Za svaki automobil na
#raspolaganju je:
#name: ime automobila
#year: godina proizvodnje automobila
#selling_price: cijena po kojoj se automobil prodaje (logaritam cijene u indijskim rupijima)
#km_driven: prijeđeni broj kilometara
#fuel: tip motora (Diesel, Petrol, CNG, LPG)
#seller_type: prodavač (individual/dealer)
#transmission: tip mjenjača (automatic/manual)
#owner: broj prethodnih vlasnika
#mileage: potrošnja automobila
#engine: zapremnina motora u cm3
#max_power: maksimalna snaga motora (bhp)
#seats broj sjedala
#Skripta crta određene grafove kako bi se dobio uvid u dataset. Proučite dobivene grafove te odgovorite na sljedeća pitanja
#1. Koliko mjerenja (automobila) je dostupno u datasetu?
#2. Kakav je tip pojedinog stupca u dataframeu?
#3. Koji automobil ima najveću cijenu, a koji najmanju?
#4. Koliko automobila je proizvedeno 2012. godine?
#5. Koji automobil je prešao najviše kilometara, a koji najmanje?
#6. Koliko najčešće automobili imaju sjedala?
#7. Kolika je prosječna prijeđena kilometraža za automobile s dizel motorom, a koliko za automobile s benzinskim
#motorom?


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('cars_processed.csv')
print(df.info())

cf=df.sort_values("selling_price")

print(cf.head(1)) 
print(cf.tail(1))

print(cf["year"].value_counts().get(2012,0))

gg=cf[["km_driven","fuel"]]
suma_diesel=0
brojac_diesel=0
suma_ben=0
brojac_ben=0
brojac=0

for brojac in range (0,len(gg)):

    if(gg["fuel"].get(brojac)=="Diesel"):
        suma_diesel+=gg["km_driven"].get(brojac)
        brojac_diesel+=1

    elif(gg["fuel"].get(brojac)=="Petrol"):
        suma_ben+=gg["km_driven"].get(brojac)
        brojac_ben+=1
      
print(suma_ben/brojac_ben)
print(suma_diesel/brojac_diesel)


sns.pairplot(df, hue='fuel')

sns.relplot(data=df, x='km_driven', y='selling_price', hue='fuel')
df = df.drop(['name','mileage'], axis=1)

obj_cols = df.select_dtypes(object).columns.values.tolist()
num_cols = df.select_dtypes(np.number).columns.values.tolist()

fig = plt.figure(figsize=[15,8])
for col in range(len(obj_cols)):
    plt.subplot(2,2,col+1)
    sns.countplot(x=obj_cols[col], data=df)

df.boxplot(by ='fuel', column =['selling_price'], grid = False)

df.hist(['selling_price'], grid = False)

plt.show()
