#Napišite Python skriptu koja će učitati tekstualnu datoteku naziva song.txt. Potrebno je napraviti rječnik koji kao
#ključeve koristi sve različite riječi koje se pojavljuju u datoteci, dok su vrijednosti jednake broju puta koliko se svaka
#riječ (ključ) pojavljuje u datoteci. Koliko je riječi koje se pojavljuju samo jednom u datoteci? Ispišite ih.

import string

brojac_jedinstvenih = 0
statistika_rijeci = {}

try:
    with open("C:\\Users\\student\\Desktop\\song.txt", 'r', encoding='utf-8') as datoteka:
        for red in datoteka:
            # Ukloni interpunkciju i pretvori u mala slova
            red = red.translate(str.maketrans('', '', string.punctuation)).lower()
            rijeci = red.split()
            
            for rijec in rijeci:
                if rijec in statistika_rijeci:
                    statistika_rijeci[rijec] += 1
                else:
                    statistika_rijeci[rijec] = 1

except FileNotFoundError:
    print("Greška: Datoteka ne postoji.")
    exit()

# Izdvajanje riječi koje se pojavljuju samo jednom
jedinstvene_rijeci = [r for r, broj in statistika_rijeci.items() if broj == 1]
brojac_jedinstvenih = len(jedinstvene_rijeci)

# Ispis rezultata
print("Rječnik svih riječi i njihovih ponavljanja:\n", statistika_rijeci)
print("\nBroj riječi koje se pojavljuju samo jednom:", brojac_jedinstvenih)
print("Te riječi su:\n", jedinstvene_rijeci)
