#Napišite programski kod koji će iscrtati sljedeće slike za mtcars skup podataka:
#1. Pomoću barplot-a prikažite na istoj slici potrošnju automobila s 4, 6 i 8 cilindara.
#2. Pomoću boxplot-a prikažite na istoj slici distribuciju težine automobila s 4, 6 i 8 cilindara.
#3. Pomoću odgovarajućeg grafa pokušajte odgovoriti na pitanje imaju li automobili s ručnim mjenjačem veću
#potrošnju od automobila s automatskim mjenjačem?
#4. Prikažite na istoj slici odnos ubrzanja i snage automobila za automobile s ručnim odnosno automatskim
#mjenjačem.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

mtcars = pd.read_csv('C:\\Users\\student\\Desktop\\LV3\\mtcars.csv.csv')

plt.figure(figsize=(8,5))
sns.barplot(x='cyl', y='mpg', data=mtcars, ci=None)
plt.title('Potrošnja automobila po broju cilindara')
plt.xlabel('Broj cilindara')
plt.ylabel('Potrošnja (mpg)')
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x='cyl', y='wt', data=mtcars)
plt.title('Distribucija težine automobila po broju cilindara')
plt.xlabel('Broj cilindara')
plt.ylabel('Težina (1000 lbs)')
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x='am', y='mpg', data=mtcars)
plt.title('Potrošnja automobila po tipu mjenjača')
plt.xlabel('Tip mjenjača (0 = automatik, 1 = ručni)')
plt.ylabel('Potrošnja (mpg)')
plt.show()

plt.figure(figsize=(8,5))
for tip in [0, 1]:
    podskup = mtcars[mtcars.am == tip]
    plt.scatter(podskup.hp, podskup.qsec, label=f"Am = {tip}")
plt.title('Odnos snage i ubrzanja po tipu mjenjača')
plt.xlabel('Snaga (hp)')
plt.ylabel('Ubrzanje (qsec)')
plt.legend()
plt.show()
