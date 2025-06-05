brojevi = []
brojac = 0

while True:
    unos_korisnika = input("Unesite broj (ili 'Done' za završetak): ")
    
    if unos_korisnika == "Done":
        break

    try:
        broj = int(unos_korisnika)
        brojevi.append(broj)
        brojac += 1
    except ValueError:
        print("Greška: molimo unesite ispravan broj!")

if brojevi:
    srednja_vr = sum(brojevi) / len(brojevi)
    najmanji = min(brojevi)
    najveci = max(brojevi)
    
    brojevi.sort()
    
    print("\nStatistika:")
    print(f"Ukupan broj unosa: {brojac}")
    print(f"Srednja vrijednost: {srednja_vr}")
    print(f"Minimalna vrijednost: {najmanji}")
    print(f"Maksimalna vrijednost: {najveci}")
    print(f"Sortirana lista: {brojevi}")
else:
    print("Niste unijeli nijedan broj.")
