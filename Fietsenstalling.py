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
    mail_lijst = []
    for gegeven in gegevens:
        mail_lijst.append(gegeven['mail'])

    while mail in mail_lijst:
        print("Dit e-mail adress is al geregistreerd")
        mail = input("E-mail adres: ")

    naam = input("Voornaam: ")
    tussenvoegsel = input("Tussenvoegsel: ")
    achternaam = input("Achternaam: ")

    while True:
        try:
            telefoonnummer = int(input("Telefoon nummer: "))
            break
        except:
            print("Telefoonnummer klopt niet..")

    wachtwoord = input("Wachtwoord: ")
    fietsnummer = int(random.randint(1000, 10000))

    fietsnummer_lijst = []
    for gegeven in gegevens:
        fietsnummer_lijst.append(gegeven['fietsnummer'])

    while str(fietsnummer) in fietsnummer_lijst:
        fietsnummer = int(random.randint(1000, 10000))

    nieuwe_gegevens = str(fietsnummer) + ';' + naam + ';' + tussenvoegsel + ';' + achternaam + ';' + mail + ';' + wachtwoord + ';' + str(telefoonnummer)

    bestand = open('database/gebruikers.csv', 'a')
    bestand.write(nieuwe_gegevens + '\n')
    bestand.close()

