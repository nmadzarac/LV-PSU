#Napišite Python skriptu koja će učitati tekstualnu datoteku naziva SMSSpamCollection.txt [1]. Ova datoteka
#sadrži 425 SMS poruka pri čemu su neke označene kao spam, a neke kao ham. Primjer dijela datoteke:
#ham Go until jurong point, crazy.. Available only in bugis n great world la e buffet... Cine there got amore wat...
#ham Ok lar... Joking wif u oni...
#spam Did you hear about the new "Divorce Barbie"? It comes with all of Ken's stuff!
#ham Yup next stop.
#a) Izračunajte koliki je prosječan broj riječi u SMS porukama koje su tipa ham, a koliko je prosječan broj riječi u
#porukama koje su tipa spam.
#b) Koliko SMS poruka koje su tipa spam završava uskličnikom ?


ham_broj_rijeci = 0
spam_broj_rijeci = 0
ham_broj_poruka = 0
spam_broj_poruka = 0
spam_sa_usklicnikom = 0

try:
    with open("C:\\Users\\student\\Desktop\\SMSSpamCollection.txt", 'r', encoding='utf-8') as datoteka:
        for linija in datoteka:
            linija = linija.strip()
            if not linija:
                continue

            dijelovi = linija.split()
            oznaka = dijelovi[0]
            poruka_rijeci = dijelovi[1:]  # Sve osim oznake

            if oznaka == "ham":
                ham_broj_poruka += 1
                ham_broj_rijeci += len(poruka_rijeci)
            elif oznaka == "spam":
                spam_broj_poruka += 1
                spam_broj_rijeci += len(poruka_rijeci)
                if poruka_rijeci and poruka_rijeci[-1].endswith("!"):
                    spam_sa_usklicnikom += 1

except FileNotFoundError:
    print("Greška: Datoteka ne postoji.")
    exit()

# Ispis rezultata
if ham_broj_poruka > 0:
    prosjek_ham = ham_broj_rijeci / ham_broj_poruka
else:
    prosjek_ham = 0

if spam_broj_poruka > 0:
    prosjek_spam = spam_broj_rijeci / spam_broj_poruka
else:
    prosjek_spam = 0

print(f"Prosječan broj riječi u HAM porukama: {prosjek_ham:.2f}")
print(f"Prosječan broj riječi u SPAM porukama: {prosjek_spam:.2f}")
print(f"Broj SPAM poruka koje završavaju uskličnikom: {spam_sa_usklicnikom}")
