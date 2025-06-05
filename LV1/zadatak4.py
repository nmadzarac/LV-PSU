#Napišite program koji od korisnika zahtijeva unos imena tekstualne datoteke. Program nakon toga treba tražiti linije
#oblika:

#X-DSPAM-Confidence: <neki_broj>
#koje predstavljaju pouzdanost korištenog spam filtra. Potrebno je izračunati srednju vrijednost pouzdanosti. Koristite
#datoteke mbox.txt i mbox-short.txt
#Primjer
#Ime datoteke: mbox.txt
#Average X-DSPAM-Confidence: 0.894128046745
#Ime datoteke: mbox-short.txt
#Average X-DSPAM-Confidence: 0.750718518519


broj_linija = 0
ukupna_pouzdanost = 0.0

ime_datoteke = input("Unesite ime tekstualne datoteke (bez .txt): ")
putanja = 'C:\\Users\\student\\Desktop\\' + ime_datoteke + '.txt'

try:
    with open(putanja, 'r') as datoteka:
        for linija in datoteka:
            linija = linija.strip()
            if linija.startswith("X-DSPAM-Confidence:"):
                try:
                    vrijednost = float(linija.split(":")[1].strip())
                    ukupna_pouzdanost += vrijednost
                    broj_linija += 1
                except ValueError:
                    print("Upozorenje: nepravilna vrijednost u liniji:", linija)
except FileNotFoundError:
    print("Greška: Datoteka ne postoji.")
    exit()

if broj_linija > 0:
    prosjek = ukupna_pouzdanost / broj_linija
    print(f"Prosječna X-DSPAM-Confidence vrijednost: {prosjek}")
else:
    print("Nema pronađenih X-DSPAM-Confidence linija.")
