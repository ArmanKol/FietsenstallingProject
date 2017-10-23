def inloggen():
    e_mail = str(input("Geef je e-mailadres: "))
    wachtwoord = str(input("Geef je wachtwoord: "))

    bestand = open("database/gebruikers.csv", "r")
    lines = bestand.readlines()
    bestand.close()
    for regels in lines:
        print(regels)

inloggen()