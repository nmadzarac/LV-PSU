#Napišite program koji od korisnika zahtijeva unos brojeva u beskonačnoj petlji sve dok korisnik ne upiše „Done“ (bez
#navodnika). Pri tome brojeve spremajte u listu. Nakon toga potrebno je ispisati koliko brojeva je korisnik unio, njihovu
#srednju, minimalnu i maksimalnu vrijednost. Sortirajte listu i ispišite je na ekran.
#Dodatno: osigurajte program od pogrešnog unosa (npr. slovo umjesto brojke) na način da program zanemari taj unos i
#ispiše odgovarajuću poruku.

lista = []

while True:
    unos = input("Unesite broj (ili 'Done' za kraj): ")
    
    if unos.lower() == 'done':  
        break
    
    try:
        broj = float(unos) 
        lista.append(broj)  
    except ValueError:
        print("Pogrešan unos! Molimo unesite broj.")  

if lista:
    print("\nBroj unesenih brojeva:", len(lista))
    print("Srednja vrijednost brojeva:", sum(lista) / len(lista))
    print("Minimalna vrijednost:", min(lista))
    print("Maksimalna vrijednost:", max(lista))

    lista.sort()  
    print("\nSortirana lista:", lista)
else:
    print("\nNiste unijeli niti jedan broj.")



    

    




