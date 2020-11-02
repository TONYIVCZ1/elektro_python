usource = float(input("Zadejte napětí zdroje ve V: "))
udiode = float(input("Zadejte napětí LED ve V: "))
idiodem = float(input("Zadejte odebíraný proud v mA: "))

if usource == 0 or udiode == 0 or idiodem == 0:
    print("Zadejte všechny čísla, jejiž hodnota není 0. ")
else:
    idiode = idiodem/1000 #Převede mA na A
    uresistor = usource-udiode #Vypočítá napětí na předřadném odporu
    print("Odpor předřadného rezistoru pro led je: ", uresistor/idiode, " Ohm. ") #Vypočítá hodnotu odporu předřadného rezistoru
    print("Výkon odporu je: ", uresistor*idiode, " W. ") #Vypočítá výkon předřadného rezistoru
