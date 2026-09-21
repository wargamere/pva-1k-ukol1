import random
pokusy = 0
cislo = random.randint(1, 69)
while True:
    uzivatelcislo = int(input("uhádni číslo 1-100:"))
    if uzivatelcislo > cislo:
        print("Moc vysoké")
        pokusy = pokusy + 1
    elif uzivatelcislo < cislo:
        print("Moc nízké")
        pokusy = pokusy + 1
    else:
        print("Správně!")
        break
print(pokusy)
