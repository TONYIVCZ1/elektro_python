#Zadání hodnot. Za neznámou dosaď 0. 
p = float(input("Zadej Výkon ve W: "))
u = float(input("Zadej napětí ve V: "))
i = float(input("Zadej proud v A: "))
#Zjištění neznámé
if p == 0 and u == 0 and i == 0: 
    print("Prosím, zadej 2 čísla jejich hodnota není 0. ")
elif p == 0 and u == 0 or u == 0 and i == 0 or p == 0 and i == 0:
    print("Zadej ještě jedno číslo. ")
else:
    if p == 0:
        print(u, " V x ", i, " A= ", u*i, " W. ")
    if u == 0:
        print(p, " W : ", i, " A= ", p/i, " V. ")
    if i == 0:
        print(p, " W : ", u, " V= ", p/u, " A. ")
