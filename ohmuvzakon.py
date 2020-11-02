u = float(input("Zadej napětí ve V: "))
i = float(input("Zadej proud v A: "))
r = float(input("zadej odpor v Ohmech: "))

if u == 0 and i == 0 and r ==0:
    print("Zadej 2 čísla, která nejsou 0. ")
elif u == 0 and i == 0 or u == 0 and r == 0 or i == 0 and r == 0:
    print("Zadej ještě jedno číslo. ")
else:
    if u == 0:
        print(r, " Ohm x ", i, " A= ", r*i, " V. ")
    if i == 0:
        print(u, " V : ", r, " Ohm= ", u/r, " A. ")
    if r == 0:
        print(u, " V : ", i, " A= ", u/i, " Ohm. ")
