mesta = [
    "Praha", "Vídeň", "Olomouc",
    "Svitavy", "Zlín", "Ostrava"
]
domeny = ("gmail.com", "seznam.cz", "email.cz")
slevy = ("Olomouc", "Svitavy", "Ostrava")
ceny = (150, 200, 120, 120, 100, 180)
dvojita_cara = "=" * 35
cara = "-" * 35
nabidka = \
"""
1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180"""

print(dvojita_cara)
print("Vítej v aplikaci Destinatio!")
print(dvojita_cara)

print(nabidka)
print(cara)


destinace = int(input("Vyber si destinaci: "))
if destinace >= 1 and destinace <= 6:
    upravena_destinace = mesta[destinace - 1]
    print(f"Destinace {upravena_destinace}")
else:
    print(f"Číslo {destinace} NEEXISTUJE! Ukončuji ...")
    quit()
print(cara)

    
if upravena_destinace == slevy[1] or upravena_destinace == slevy[0] or upravena_destinace == slevy[2]:  #upravena_cena in slevy:    - lepší zápis
    cena_po_sleve = ceny[destinace-1]*0.75
    print(f"Získáváte slevu 25%, Cena po selvě je: {cena_po_sleve}Kč")
    print(cara)
else:
    print(f"Vaše cena je: {ceny[destinace-1]}Kč.")
    print(cara)

jmeno = input("Jméno:")
prijmeni = input("Příjmení:")
print(cara)

if jmeno.isalpha() and prijmeni.isalpha():
    print(jmeno + " " + prijmeni)
    
else: 
    print(f"Zadané jméno: {jmeno} nebo příjmení: {prijmeni} je zadáno chybně! Ukončuji program ...")
    quit()

print(cara)

email = input("Email:")
email_domena = email.split("@")   # if @ in email and email.split("@")[1] in domeny:
if "@" in email:
    if email_domena[1] in domeny:
        print(f"Na váš email: {email} vám příjde jízdenka.")
    else:
        print("Vaše doména není podporována, Ukončuji program ...")
        quit()
else:
    print("Zadali jste špatně Váš E-mail. Ukončuji program ...")
    quit
print(dvojita_cara)

print(f'''Rekapitulace
Vaše jmnéno: {jmeno + " " + prijmeni},
Vašel destinace: {upravena_destinace}, 
Na Váš email: {email} vám bude poslán lístek.''')