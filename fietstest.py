import csv
import random
import datetime
import telepot
import pyotp


def telegramRead():
    bot = telepot.Bot("370325529:AAGKGqP-dHRoyKb2FKnPtMyYCdOhcGKLK5Q")
    response = bot.getUpdates()  # pakt het laatst verzonden bericht aan de bot
    response_1 = response[-1]
    UserID = response_1['message']['chat']['id']  # pakt het ID van de verzender
    UserBericht = response_1['message']['text']

    return UserBericht


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

    while len(wachtwoord) <= 6:
        print("Wachtwoord moet ten minste 6 tekens lang zijn.. ")
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

    print("Gebruiker is geregistreerd en heeft fietsnummer: " + str(fietsnummer))


def persoonlijke_informatie_opvragen():

    print("U moet eerst inloggen om deze gegevens te mogen bekijken.")
    response_inloggen = inloggen()

    if response_inloggen != 0:

        gebruiker_gegevens = csvread("gebruikers.csv")
        stalling_gegevens = csvread("gestald.csv")

        for gebruiker_gegeven in gebruiker_gegevens:
            if mail == gebruiker_gegeven["mail"]:
                if gebruiker_gegeven["tussenvoegsel"] == "":
                    print("Uw volledige naam: " + gebruiker_gegeven["voornaam"] + " " + gebruiker_gegeven["achternaam"])
                else:
                    print("Uw volledige naam: " + gebruiker_gegeven["voornaam"] + " " + gebruiker_gegeven["tussenvoegsel"] + " " + gebruiker_gegeven["achternaam"])
                print("Uw unieke fietsnummer is: " + gebruiker_gegeven["fietsnummer"])
                print("Uw e-mail adres is: " + gebruiker_gegeven["mail"])
                print("Uw telefoonnummer is: " + gebruiker_gegeven["telefoonnummer"])

            for fietsdata in stalling_gegevens:
                if gebruiker_gegeven["fietsnummer"] == fietsdata["fietsnummer"]:
                    datum = fietsdata["staldatum"]

        prijs_te_betalen()

    else:
        print("Informatie kan niet worden aangevraagd.")


def algemene_informatie_aanvragen():
    gegevens = csvread("gestald.csv")

    vrije_plekken = 1000 - (len(gegevens) + 1)

    print("Er zijn nog " + str(vrije_plekken) + " van de 1000 plekken over.")
    print("De kosten voor het bergen van uw fiets zijn \u20ac2.5 per dag.")
    print("De eerste dag is gratis.")


def prijs_te_betalen():

    gebruiker_gegevens = csvread("gebruikers.csv")
    stalling_gegevens = csvread("gestald.csv")

    for gebruiker_gegeven in gebruiker_gegevens:
        if mail == gebruiker_gegeven["mail"]:
            for fietsdata in stalling_gegevens:
                if gebruiker_gegeven["fietsnummer"] == fietsdata["fietsnummer"]:
                    datum = fietsdata["staldatum"]

    datum = datum.split("/")
    vandaag = datetime.datetime.today()
    datum_vandaag = datetime.date(int(vandaag.strftime("%Y")), int(vandaag.strftime("%m")), int(vandaag.strftime("%d")))
    datum_gestald = datetime.date(int(datum[2]), int(datum[1]), int(datum[0]))
    aantal_dagen_gestald = datum_vandaag - datum_gestald
    aantal_dagen_gestald = (str(aantal_dagen_gestald)).split(" ")

    if str(aantal_dagen_gestald[0]) == "0:00:00":
        aantal_dagen_gestald = [0]

    if int(aantal_dagen_gestald[0]) <= 1:
        print("Er hoeft niks betaald te worden, de eerste dag is gratis.")
    else:
        prijs = str(int(aantal_dagen_gestald[0])-1 * 2.5)
        print("Er moet \u20ac" + prijs + " worden betaald.")


def inloggen():
    global mail             # voor in de functies informatie opvragen
    gegevens_gebruiker = csvread("gebruikers.csv")
    mail = str(input("Geef je e-mailadres: "))
    wachtwoord = str(input("Geef je wachtwoord: "))
    counter = 3
    global fietsnummer
    fietsnummer = 0

    while counter > 0:
        for item in gegevens_gebruiker:
            if str(item['wachtwoord']) == wachtwoord and str(item['mail']) == mail:
                fietsnummer = str(item['fietsnummer'])
                return (str(item['fietsnummer']))
        else:
            print("Combinatie is niet correct.. " + "Je hebt nog " + str(counter) + "inlogpogingen over..")
            mail = str(input("Geef je e-mailadres: "))
            wachtwoord = str(input("Geef je wachtwoord: "))
            counter -= 1

    print("Inlogpogingen overschreden..")
    return 0


def captcha_check():
    if fietsnummer != 0:
        hotp = pyotp.HOTP('base32secret3232')
        random_seed = random.randint(9999, 99999)
        print(hotp.at(random_seed))

        first_check = telegramRead()

        check_via_input = input("Code ingevuld.")

        counter = 2

        while counter != 0:
            if check_via_input != first_check:
                if hotp.verify(check_via_input, random_seed) == True:
                    print("True")
                    break
                else:
                    print("Foute code, probeer het nog een keer.")
                    check_via_input = input("Wat is de code?")
                    counter -= 1


def stallen_fiets():
    vandaag = datetime.datetime.today()
    datum = vandaag.strftime('%d/%m/%Y')
    gegevens_gestald = csvread('gestald.csv')
    response_inloggen = inloggen()

    if response_inloggen != 0:

        fietsnummer = input("Fietsnummer: ")

        pogingen_fietsnummer = 0
        while str(fietsnummer) != response_inloggen and pogingen_fietsnummer < 5:
            print(str(fietsnummer) + " is niet geregistreerd.. Probeer opnieuw..")
            fietsnummer = input("Fietsnummer: ")
            pogingen_fietsnummer += 1

        fietsnummer_lijst = []
        for gegeven in gegevens_gestald:
            fietsnummer_lijst.append(gegeven['fietsnummer'])

        if fietsnummer in fietsnummer_lijst:
            print("Fiets staat al in stalling..")

        else:
            print("Fiets kan gestald worden..")
            gegevens_stalling = str(fietsnummer) + ";" + datum

            bestand = open('database/gestald.csv', 'a')  # nog in een fucntie zetten?
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
            print("Fiets staat niet in stalling.. ")

        else:
            for fiets in gegevens_stalling:
                if fiets['fietsnummer'] == response_inloggen:
                    gegevens_stalling.remove(fiets)
                    print("Fiets opgehaald.")
                    prijs_te_betalen()

            with open("database/gestald.csv", "w", newline='\n') as WriteMyCsv:
                veldnamen = ["fietsnummer", "staldatum"]
                writer = csv.DictWriter(WriteMyCsv, fieldnames=veldnamen, delimiter=";")
                writer.writeheader()

                for gegeven in gegevens_stalling:
                    writer.writerow((gegeven))

    else:
        print("Fiets kan niet opgehaald worden..")

inloggen()
captcha_check()