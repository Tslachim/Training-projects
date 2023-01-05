# Nákupní košík, přidávání zboží do košíku a ubíraní ve skladovych zásobách + výpočet ceny.

# Zadané hodnoty
kosik = dict()
oddelovac = "=" * 40
potraviny = {
    "mleko": [30, 5],  # index '0'-> cena, index '1' -> pocet
    "maso": [100, 1],
    "banan": [30, 10],
    "jogurt": [10, 5],
    "chleb": [20, 5],
    "jablko": [10, 10],
    "pomeranc": [15, 10]
}
nabidka = """
+-----------+----------+
| POTRAVINA |   CENA   |
+-----------+----------+
| mleko     |    30,-  |
| maso      |   100,-  |
| banan     |    30,-  |
| jogurt    |    10,-  |
| chleb     |    20,-  |
| jablko    |    10,-  |
| pomenrac  |    15,-  |
+-----------+----------+
"""
print(f"""Vitejte u našeho nakupního košíku!
{oddelovac}
{nabidka}""")

while zbozi := input("Zadávej zboží(pokud chceš ukončit napiš 'q'): "):
    if zbozi == "q":
        break
    elif zbozi not in potraviny.keys():
        print(f"Zboží {zbozi} není v nabídce.")
        continue
    elif zbozi not in kosik:
        kosik[zbozi] = (potraviny[zbozi][0]), (1)
        potraviny[zbozi] = (potraviny[zbozi][0]), int(potraviny[zbozi][1]) - 1
    elif zbozi in kosik:
        if potraviny[zbozi][1] == 0:
            print("Zboží není skladem.")
            continue
        kosik[zbozi] = (kosik[zbozi][0]), int(kosik[zbozi][1]) + 1
        potraviny[zbozi] = (potraviny[zbozi][0]), int(potraviny[zbozi][1]) - 1

print(f"""{oddelovac}
V košíku máš: {kosik}
{oddelovac}""")