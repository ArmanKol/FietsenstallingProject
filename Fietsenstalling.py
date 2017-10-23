import csv

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

inloggen()