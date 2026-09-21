import random
cislo = random.randint(1, 69)
while True:
    uzivatelcislo = int(input("uhádni číslo 1-69:"))
    if uzivatelcislo > cislo:
        print("Moc vysoké")
    elif uzivatelcislo < cislo:
        print("Moc nízké")
    else:
        print("Správně!")
        break
