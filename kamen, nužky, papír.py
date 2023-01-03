import random
again = True
oddelovac = 40 * "="
pocitadlo_hrac = 0 
pocitadlo_pocitac = 0

print(f"""
{oddelovac}
Vítej ve hře Kámen, Nůžky, Papír !
{oddelovac}""")

while again:
    moznosti = ["kámen", "nůžky", "papír"]
    pocitac = random.choice(moznosti)
    hrac = input("Napiš svou volbu(kámen,nůžky,papír): ").lower()

    if hrac in moznosti:
        if hrac == pocitac:
            print("počítač dává: " + pocitac.capitalize())
            print(f"""
{oddelovac}
        Je to nerozhodně !
{oddelovac}""")
            
        elif (hrac == "kámen" and pocitac == "nůžky") or (hrac == "nůžky" and pocitac == "papír") or (hrac == "papír" and pocitac == "kámen"):
            print("Počítač dává: " + pocitac.capitalize())
            print(f"""
{oddelovac}
        Jsi vítěz !
{oddelovac}""")
            pocitadlo_hrac += 1
            
        else:
            print("Počítač dává: " + pocitac.capitalize())
            print(f"""
{oddelovac}
Vyhrává počítač !
{oddelovac}""")   
            pocitadlo_pocitac +=1

    else:
        print("Zadej správnou odpověď!")

    play_again = input(f"Chceš hrát znova? Tvé skóre je {pocitadlo_hrac}:{pocitadlo_pocitac} \nNapiš 'yes' pro novou hru: ")
    print(oddelovac)
    if play_again != "yes":
        again = False
        

print("Děkuji za hru, Měj se hezky!")