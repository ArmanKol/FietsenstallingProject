import csv
import random


def csvread(bestandsnaam):
    with open("database/" + bestandsnaam, "r") as ReadMyCsv:
        reader = csv.DictReader(ReadMyCsv, delimiter=";")

        gegevens = []
        for gegeven in reader:
            gegevens.append(gegeven)

    return gegevens


def registreren():
    """Functie voor het registreren van de gebruiker. Slaat de gegevens op in gebruikers.csv"""
    gegevens = csvread("gebruikers.csv")

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
    fietsnummer = int(random.randint(1000, 9999))

    fietsnummer_lijst = []
    for gegeven in gegevens:
        fietsnummer_lijst.append(gegeven['fietsnummer'])

    while str(fietsnummer) in fietsnummer_lijst:
        fietsnummer = int(random.randint(1000, 9999))

    nieuwe_gegevens = str(fietsnummer) + ';' + naam + ';' + tussenvoegsel + ';' + achternaam + ';' + mail + ';' + wachtwoord + ';' + str(telefoonnummer)

    bestand = open('database/gebruikers.csv', 'a') #nog in een fucntie zetten?
    bestand.write(nieuwe_gegevens + '\n')
    bestand.close()


def persoonlijke_informatie_opvragen():
    print("U moet eerst inloggen om deze gegevens te mogen bekijken.")
    correctLogin = 0

    while correctLogin == 0:
        correctLogin = inloggen()

    gegevens = csvread("gebruikers.csv")
    stalling_gegevens = csvread("gestald.csv")

    for gegeven in gegevens:
        if mail == gegeven["mail"]:
            if gegeven["tussenvoegsel"] == "":
                print("Uw volledige naam: " + gegeven["voornaam"] + " " + gegeven["achternaam"])
            else:
                print("Uw volledige naam: " + gegeven["voornaam"] + " " + gegeven["tussenvoegsel"] + " " + gegeven[
                    "achternaam"])
            print("Uw unieke fietsnummer is: " + gegeven["fietsnummer"])
            print("Uw e-mail adres is: " + gegeven["mail"])
            print("Uw telefoonnummer is: " + gegeven["telefoonnummer"])

        for fietsdata in stalling_gegevens:
            if gegeven["fietsnummer"] == fietsdata["fietsnummer"]:
                data = fietsdata["staldata"]

    print("En dan nog iets doen met -> " + data)


def algemene_informatie_aanvragen():
    gegevens = csvread("gestald.csv")

    vrije_plekken = 1000 - (len(gegevens) + 1)

    print("Er zijn nog " + str(vrije_plekken) + " van de 1000 plekken over.")
    print("De kosten voor het bergen van uw fiets zijn 0.10 euro per uur.")


def inloggen():
    correctLogin = 0
    pogingen = 5
    gegevens = csvread("gebruikers.csv")

    while correctLogin != 1:
        if pogingen == 0:
            break
        global mail
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
                if lengte_lijst == len(gegevens):
                    print("Het e-mailadres is niet gevonden.")
                lengte_lijst += 1
                pass

    if pogingen == 0:
        print("Uw heeft te vaak geprobeert in te loggen.")

registreren()