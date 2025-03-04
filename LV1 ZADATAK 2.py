#Napišite program koji od korisnika zahtijeva upis jednog broja koji predstavlja nekakvu ocjenu i nalazi se između 0.0 i
#1.0. Ispišite kojoj kategoriji pripada ocjena na temelju sljedećih uvjeta:
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#Ako korisnik nije utipkao broj, ispišite na ekran poruku o grešci (koristite try i except naredbe). Također, ako je
#broj izvan intervala [0.0 i 1.0] potrebno je ispisati odgovarajuću poruku.

print('Unesite broj u intervalu [0.0, 1.0]')
try:
    a = float(input())
except:
    print('Nije unesen broj.')
if a < 0.0 or a > 1.0:
    print('Nije unesen broj u intervalu. [0.0, 1.0]')

while a < 0.0 or a > 1.0:
    try:
        a = float(input())
    except:
        print('Nije unesen broj.')
    if a < 0.0 or a > 1.0:
        print('Nije unesen broj u intervalu. [0.0, 1.0]')


if a >= 0.9:
    print('Ocjena A')
if a >= 0.8 and a < 0.9:
    print('Ocijena B')
if a >= 0.7 and a < 0.8:
    print('Ocjena C')
if a >= 0.6 and a < 0.7:
    print('Ocjena D')
if a < 0.6:
    print('Ocjena F')
