import csv
import datetime


def csvread(bestandsnaam):
    with open("database/" + bestandsnaam, "r") as ReadMyCsv:
        reader = csv.DictReader(ReadMyCsv, delimiter=";")

        gegevens = []
        for gegeven in reader:
            gegevens.append(gegeven)

    return gegevens


def inloggen():
    global mail             # voor in de functies informatie opvragen
    gegevens_gebruiker = csvread("gebruikers.csv")
    mail = str(input("Geef je e-mailadres: "))
    wachtwoord = str(input("Geef je wachtwoord: "))
    counter = 3

    while counter > 0:
        for item in gegevens_gebruiker:
            if str(item['wachtwoord']) == wachtwoord and str(item['mail']) == mail:
                return (str(item['fietsnummer']))
        else:
            print("Combinatie is niet correct.. " + "Je hebt nog " + str(counter) + " inlogpogingen over..")
            mail = str(input("Geef je e-mailadres: "))
            wachtwoord = str(input("Geef je wachtwoord: "))
            counter -= 1

    print("Inlogpogingen overschreden..")
    return 0


def stallen_fiets():
    vandaag = datetime.datetime.today()
    datum = vandaag.strftime('%d/%m/%Y')
    gegevens_stalling = csvread('gestald.csv')
    response_inloggen = inloggen()

    if response_inloggen != 0:

        fietsnummer = input("Fietsnummer: ")

        pogingen_fietsnummer = 0
        while str(fietsnummer) != response_inloggen and pogingen_fietsnummer < 5:
            print(str(fietsnummer) + " is niet geregistreerd.. Probeer opnieuw..")
            fietsnummer = input("Fietsnummer: ")
            pogingen_fietsnummer += 1

        fietsnummer_lijst = []
        for gegeven in gegevens_stalling:
            fietsnummer_lijst.append(gegeven['fietsnummer'])

        if fietsnummer in fietsnummer_lijst:
            print("Fiets staat al in stalling..")

        else:
            print("Fiets kan gestald worden..")
            gegevens_stalling = str(fietsnummer) + ";" + datum

            bestand = open('database/gestald.csv', 'a')
            bestand.write(gegevens_stalling + '\n')
            bestand.close()

    else:
        print("Fiets kan niet gestald worden..")


def ophalen_fiets():
    gegevens_stalling = csvread('gestald.csv')
    response_inloggen = inloggen()

    if response_inloggen != 0:

        fietsnummer = input("Fietsnummer: ")

        pogingen_fietsnummer = 0
        while str(fietsnummer) != response_inloggen and pogingen_fietsnummer < 5:
            print(str(fietsnummer) + " is niet geregistreerd.. Probeer opnieuw..")
            fietsnummer = input("Fietsnummer: ")
            pogingen_fietsnummer += 1

        fietsnummer_lijst = []
        for gegeven in gegevens_stalling:
            fietsnummer_lijst.append(gegeven['fietsnummer'])

        if fietsnummer not in fietsnummer_lijst:
            print("Fiets staat niet in stalling..")

        else:

            #bestand = open('database/gestald.csv', 'w')

            #for gegeven in gegevens_stalling:
            #    gegevens_stalling.write(gegeven)
            #bestand.close()

    else:
        print("Fiets kan niet opgehaald worden..")


ophalen_fiets()