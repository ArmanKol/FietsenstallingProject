import csv
import random


def csvread():
    with open("database/gebruikers.csv", "r") as ReadMyCsv:
        reader = csv.DictReader(ReadMyCsv, delimiter=";")

        gegevens = []
        for gegeven in reader:
            gegevens.append(gegeven)

    return gegevens


def inloggen():
    correctLogin = 0
    pogingen = 5
    gegevens = csvread()
    while correctLogin != 1:
        if pogingen == 0:
            break
        mail = str(input("Geef je e-mailadres: "))
        wachtwoord = str(input("Geef je wachtwoord: "))
        lengte_lijst = 0
        for gegeven in gegevens:
            if mail == gegeven["mail"]:
                if wachtwoord == "":
                    print("Er is geen wachtwoord ingevoerd.")
                    break
                if wachtwoord == gegeven["wachtwoord"]:
                    print("Combinatie klopt.")
                    correctLogin = 1
                    break
                else:
                    print("De combinatie is niet goed.")
                    pogingen -= 1
                    if pogingen != 0:
                        print("U heeft nog " + str(pogingen) + " pogingen over.")
            else:
                if lengte_lijst == (len(gegevens)-1):
                    print("Het e-mailadres is niet gevonden.")
                lengte_lijst += 1
                pass
    if pogingen == 0:
        print("Uw heeft te vaak geprobeert in te loggen.")


def registreren():
    """Functie voor het registreren van de gebruiker. Slaat de gegevens op in gebruikers.csv"""
    gegevens = csvread()

    mail = input("E-mail adres: ")

    for gegeven in gegevens:
        if mail != gegeven['mail']:
            pass
        else:
            print("Dit e-mail adres is al in gebruik.. ")
            mail = input("E-mail adres: ")

    naam = input("Voornaam: ")
    tussenvoegsel = input("Tussenvoegsel: ")
    achternaam = input("Achternaam: ")
    telefoonnummer = str(input("Telefoon nummer: "))

    #for nummer in telefoonnummer:
    #    if nummer not in '0123456789':
    #        print("Telefoonnummer niet correct..")
    #        telefoonnummer = input("Telefoon nummer: ")

    wachtwoord = input("Wachtwoord: ")
    fietsnummer = int(random.randint(0, 10))

    #while True:
    #    for gegeven in gegevens:
    #        if str(fietsnummer) != gegeven['fietsnummer']:
    #            print("aangemaakt")
    #            break
    #        else:
    #            print("aangepast")
    #            fietsnummer = int(random.randint(0, 10))

    nieuwe_gegevens = str(fietsnummer) + ';' + naam + ';' + tussenvoegsel + ';' + achternaam + ';' + mail + ';' + wachtwoord + ';' + str(telefoonnummer)

    bestand = open('database/gebruikers.csv', 'a')
    bestand.write(nieuwe_gegevens + '\n')
    bestand.close()

registreren()