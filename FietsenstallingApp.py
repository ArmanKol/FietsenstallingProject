import tkinter
import os
import sys
import csv
import random
import tkinter.messagebox
import datetime
import pyotp
import telepot
import requests
import xmltodict


def filecheck():
    """Kijkt of benodigde map en bestanden aanwezig zijn bij de .exe variant van het programma."""
    database_folder = os.getcwd() + "\database"
    if not os.path.isdir(database_folder):
        os.makedirs(database_folder)

    gebruikers_bestand = database_folder + "\gebruikers.csv"
    if not os.path.isfile(gebruikers_bestand):
        inhoud_gebruikers_bestand = "fietsnummer;naam;mail;wachtwoord;telefoonnummer\n"
        schrijf_gebruikers_bestand = open(gebruikers_bestand, 'a')
        schrijf_gebruikers_bestand.writelines(inhoud_gebruikers_bestand)

    gestald_bestand = database_folder + "\gestald.csv"
    if not os.path.isfile(gestald_bestand):
        inhoud_gestald_bestand = "fietsnummer;staldatum\n"
        schrijf_gestald_bestand = open(gestald_bestand, 'a')
        schrijf_gestald_bestand.writelines(inhoud_gestald_bestand)


def telegram_read():
    """Telegram bot leest de teruggestuurde code van de gebruiker."""
    bot = telepot.Bot("370325529:AAGKGqP-dHRoyKb2FKnPtMyYCdOhcGKLK5Q")
    response = bot.getUpdates()
    response_1 = response[-1]
    UserBericht = response_1['message']['text']

    return UserBericht


def telegram_check():
    """Genereert een random code en controleert of de juist code wordt toegezonden door de gebruiker."""
    hotp = pyotp.HOTP('base32secret3232')
    random_seed = random.randint(9999, 99999)
    tkinter.messagebox.showinfo("", "Ga naar: http://t.me/BevFietsBot" + "\nen stuur deze code: " + hotp.at(random_seed)
                                + "\nGa na versturen verder.")
    telegram_output = telegram_read()

    if hotp.verify(telegram_output, random_seed):
        return 1
    else:
        tkinter.messagebox.showinfo("", "Inlog gegevens niet correct")
        return 0


def csvread(bestandsnaam):
    """Functie voor het lezen van een CSV bestand."""
    with open("database/" + bestandsnaam, "r") as ReadMyCsv:
        reader = csv.DictReader(ReadMyCsv, delimiter=";")

        gegevens = []
        for gegeven in reader:
            gegevens.append(gegeven)

    return gegevens


def registreren():
    """Functie voor het registreren van de gebruiker. Slaat de gegevens op in gebruikers.csv."""
    gegevens_gebruikers = csvread("gebruikers.csv")
    gegevens_status = 0

    mail_lijst = []

    naam = naam_entry.get()
    mail = email_entry.get().lower()
    wachtwoord = wachtwoord_entry.get()
    telefoonnummer = telefoonnummer_entry.get()

    # controle of mail ingevuld is of mail al geregistreerd is
    for gegeven in gegevens_gebruikers:
        mail_lijst.append(gegeven['mail'])
    if mail in mail_lijst:
        tkinter.messagebox.showinfo("", "Dit e-mail adres is al geregistreerd.")
    elif mail == '' or mail == len(mail) * ' ':
        tkinter.messagebox.showinfo("", "E-mail adres is niet ingevuld.")
    else:
        gegevens_status += 1
        pass

    # controle op lengte wachtwoord
    if len(wachtwoord) <= 6:
        tkinter.messagebox.showinfo("", "Het wachtwoord moet langer dan 6 tekens zijn.")
    else:
        gegevens_status += 1
        pass

    # genereren random fietsnummer
    fietsnummer = int(random.randint(1000, 9999))

    fietsnummer_lijst = []
    for gegeven in gegevens_gebruikers:
        fietsnummer_lijst.append(gegeven['fietsnummer'])

    while str(fietsnummer) in fietsnummer_lijst:
        fietsnummer = int(random.randint(1000, 9999))

    # gegevens opslaan in bestand
    if gegevens_status == 2:
        nieuwe_gegevens = str(fietsnummer) + ';' + naam + ';' + mail + ';' + wachtwoord + ';' + str(telefoonnummer)
        registrerengelukt = tkinter.messagebox.showinfo("", "Je bent succesvol geregistreerd." +
                                                        "\n" + "Fietsnummer: " + str(fietsnummer))
        bestand = open('database/gebruikers.csv', 'a')
        bestand.write(nieuwe_gegevens + '\n')
        bestand.close()

        naam_entry.delete(0, 'end')
        email_entry.delete(0, 'end')
        wachtwoord_entry.delete(0, 'end')
        telefoonnummer_entry.delete(0, 'end')

        if registrerengelukt == "ok":
            return toonHoofdFrame()
    else:
        pass


def inlog_stallen():
    """Functie voor het stallen van de fiets. Slaat gegevens op in gestald.csv."""
    # gegevens voor het stallen
    gegevens_gebruiker = csvread("gebruikers.csv")
    gegevens_gestald = csvread("gestald.csv")

    vandaag = datetime.datetime.today()
    datum = vandaag.strftime('%d/%m/%Y')

    username = inlogNaamStallen_entry.get().lower()
    password = inlogWachtwoordStallen_entry.get()
    fietsnummer = inlogFietsnummerStallen_entry.get()

    status_inloggen = 0
    fietsnummer_lijst = []

    # controleren gegevens gebruiker
    for item in range(0, len(gegevens_gebruiker)):
        if str(gegevens_gebruiker[item]['wachtwoord']) == password \
                and str(gegevens_gebruiker[item]['mail']) == username \
                and str(gegevens_gebruiker[item]['fietsnummer']) == fietsnummer:
            status_inloggen = 1
        else:
            pass
    if status_inloggen == 0:
        tkinter.messagebox.showinfo("", "Inloggegevens niet correct")
    else:
        pass

    # controleren of fiets al in de stalling staat
    if status_inloggen == 1:
        for gegeven in gegevens_gestald:
            fietsnummer_lijst.append(gegeven['fietsnummer'])
        if fietsnummer in fietsnummer_lijst:
            tkinter.messagebox.showinfo("", "Fiets staat al in stalling..")
            status_inloggen = 0
        else:
            pass
    else:
        pass

    # telegram check voor two-factor authenticatie
    if status_inloggen == 1:
        status_inloggen = telegram_check()
    else:
        pass

    # fiets opslaan in bestand en succes bericht geven aan gebruiker
    if status_inloggen == 1:
        gegevens_stalling = str(fietsnummer) + ";" + datum
        inloggengelukt = tkinter.messagebox.showinfo("", "Je bent succesvol ingelogd.\n" + "Je fiets is gestald")
        bestand = open('database/gestald.csv', 'a')
        bestand.write(gegevens_stalling + '\n')
        bestand.close()

        inlogNaamStallen_entry.delete(0, 'end')
        inlogWachtwoordStallen_entry.delete(0, 'end')
        inlogFietsnummerStallen_entry.delete(0, 'end')

        if inloggengelukt == "ok":
            return toonHoofdFrame()
    else:
        pass


def prijs_te_betalen(mail):
    """Functie voor het berekenen van de prijs die de gebruiker moet betalen voor het stallen van zijn fiets."""
    gebruiker_gegevens = csvread("gebruikers.csv")
    stalling_gegevens = csvread("gestald.csv")

    for gebruiker_gegeven in gebruiker_gegevens:
        if mail == gebruiker_gegeven["mail"]:
            for fietsdata in stalling_gegevens:
                if gebruiker_gegeven["fietsnummer"] == fietsdata["fietsnummer"]:
                    datum = fietsdata["staldatum"]

                    datum = datum.split("/")
                    vandaag = datetime.datetime.today()
                    datum_vandaag = datetime.date(int(vandaag.strftime("%Y")), int(vandaag.strftime("%m")),
                                                  int(vandaag.strftime("%d")))
                    datum_gestald = datetime.date(int(datum[2]), int(datum[1]), int(datum[0]))
                    aantal_dagen_gestald = datum_vandaag - datum_gestald
                    aantal_dagen_gestald = (str(aantal_dagen_gestald)).split(" ")

                    if str(aantal_dagen_gestald[0]) == "0:00:00":
                        aantal_dagen_gestald = [0]

                    if int(aantal_dagen_gestald[0]) <= 1:
                        return 0
                    else:
                        return (int(aantal_dagen_gestald[0]) - 1) * 2.5


def inlog_ophalen():
    """Functie voor het ophalen van de fiets. Bewerkt en slaat gegevens op in gestald.csv."""
    # gegevens voor het ophalen van de fiets
    gegevens_gebruiker = csvread("gebruikers.csv")
    gegevens_gestald = csvread("gestald.csv")

    username = inlogNaamOphalen_entry.get().lower()
    password = inlogWachtwoordOphalen_entry.get()
    fietsnummer = inlogFietsnummerOphalen_entry.get()

    status_inloggen = 0
    fietsnummer_lijst = []

    # controleren gegevens gebruiker
    for item in range(0, len(gegevens_gebruiker)):
        if str(gegevens_gebruiker[item]['wachtwoord']) == password \
                and str(gegevens_gebruiker[item]['mail']) == username \
                and str(gegevens_gebruiker[item]['fietsnummer']) == fietsnummer:
            status_inloggen = 1
        else:
            pass
    if status_inloggen == 0:
        tkinter.messagebox.showinfo("", "Inloggegevens niet correct")
    else:
        pass

    # controleren of fiets in de stalling staat
    if status_inloggen == 1:
        for gegeven in gegevens_gestald:
            fietsnummer_lijst.append(gegeven['fietsnummer'])
        if fietsnummer not in fietsnummer_lijst:
            tkinter.messagebox.showinfo("", "Fiets staat niet in stalling..")
            status_inloggen = 0
        else:
            pass
    else:
        pass

    # telegram check voor two-factor authenticatie
    if status_inloggen == 1:
        status_inloggen = telegram_check()
    else:
        pass

    # Gebruiker informeren dat inloggen succesvol is en gestalde fiets uit bestand verwijderen
    if status_inloggen == 1:
        inloggengelukt = tkinter.messagebox.showinfo("", "Je bent succesvol ingelogd." +
                                                     "\nJe kan je fiets ophalen" +
                                                     "\nDe kosten zijn: \u20ac" + str(prijs_te_betalen(username)))

        for fiets in gegevens_gestald:
            if fiets['fietsnummer'] == fietsnummer:
                gegevens_gestald.remove(fiets)

        with open("database/gestald.csv", "w", newline='\n') as WriteMyCsv:
            veldnamen = ["fietsnummer", "staldatum"]
            writer = csv.DictWriter(WriteMyCsv, fieldnames=veldnamen, delimiter=";")
            writer.writeheader()

            for gegeven in gegevens_gestald:
                writer.writerow(gegeven)

        inlogNaamOphalen_entry.delete(0, 'end')
        inlogWachtwoordOphalen_entry.delete(0, 'end')
        inlogFietsnummerOphalen_entry.delete(0, 'end')

        if inloggengelukt == "ok":
            return toonHoofdFrame()
    else:
        pass


def algemene_informatie_aanvragen():
    """Functie voor het berekenen van het aantal beschikbare plekken in de stalling."""
    # gegevens voor algemene informatie
    gegevens = csvread("gestald.csv")

    vrije_plekken = 1000 - len(gegevens)

    return vrije_plekken


def persoonlijke_informatie_aanvragen():
    """Functie voor het opvragen van de persoonlijke informatie."""
    # gegevens voor persoonlijke informatie
    gegevens_gebruiker = csvread("gebruikers.csv")
    gegevens_gestald = csvread("gestald.csv")

    username = inlogNaamPersoonlijk_entry.get().lower()
    password = inlogWachtwoordPersoonlijk_entry.get()

    stal_datum = "Niet in stalling"
    prijs_betalen = 0
    fietsnummer = ''
    naam = ''
    telefoonnummer = ''

    status_inloggen = 0

    # controleren gegevens gebruiker
    for item in range(0, len(gegevens_gebruiker)):
        if str(gegevens_gebruiker[item]['wachtwoord']) == password \
                and str(gegevens_gebruiker[item]['mail']) == username:
            fietsnummer = str(gegevens_gebruiker[item]['fietsnummer'])
            status_inloggen = 1
        else:
            pass
    if status_inloggen == 0:
        tkinter.messagebox.showinfo("", "Inloggegevens niet correct")
    else:
        pass

    # telegram check voor two-factor authenticatie
    if status_inloggen == 1:
        status_inloggen = telegram_check()
    else:
        pass

    # gegevens ophalen voor persoonlijke informatie en controle of fiets in stalling staat
    if status_inloggen == 1:
        for gebruiker_gegeven in gegevens_gebruiker:
            if username == gebruiker_gegeven['mail']:
                naam = gebruiker_gegeven['naam']
                fietsnummer = gebruiker_gegeven['fietsnummer']
                telefoonnummer = gebruiker_gegeven['telefoonnummer']

                for stal_gegeven in gegevens_gestald:
                    if gebruiker_gegeven['fietsnummer'] == stal_gegeven['fietsnummer']:
                        stal_datum = stal_gegeven['staldatum']
                        prijs_betalen = prijs_te_betalen(username)

    # weergeven van informatie aan gebruiker
        persoonlijkeInformatie_label = tkinter.Label(master=persoonlijkeInformatieFrame, text=(
            "Uw unieke fietsnummer: " + str(fietsnummer) +
            "\nUw naam: " + naam +
            "\nUw telefoonnummer: " + telefoonnummer +
            "\nUw e-mail adres: " + username +
            "\nUw fiets staat gestald sinds: " + str(stal_datum) +
            "\nDe kosten op dit moment: \u20ac" + str(prijs_betalen)), background="yellow")
        persoonlijkeInformatie_label.grid(row=0, column=0)

        persoonlijkeInformatie_knop = tkinter.Button(master=persoonlijkeInformatieFrame, text="Terug",
                                                     command=toonHoofdFrame)
        persoonlijkeInformatie_knop.grid(row=1, column=0)

        inlogNaamPersoonlijk_entry.delete(0, 'end')
        inlogWachtwoordPersoonlijk_entry.delete(0, 'end')

        toonPersoonlijkeInformatieFrame()
        return persoonlijkeInformatie_label


def trein_tijden():
    """Functie voor het ophalen van de meest actuele vertrektijd, aan de hand van begin en eindstation"""
    try:
        beginstation = treinTijdenBeginstation_entry.get()
        eindstation = treinTijdenEindstation_entry.get()

        translater = str.maketrans(" ", "+")
        eindstation = eindstation.translate(translater)

        api_auth = ('ik_ben_liam@hotmail.com', 'KGCZ67pwlCPtrE2OGj_zVNy3ULYqHKlt0pd91MdxUatUGoGnUJGEgw')
        api_url = 'http://webservices.ns.nl/ns-api-treinplanner?fromStation=' + beginstation + "&toStation=" + \
                  eindstation

        api_request = requests.get(api_url, auth=api_auth)

        request = xmltodict.parse(api_request.text)

        treindata = request['ReisMogelijkheden']['ReisMogelijkheid'][0]
        datum_en_tijd = str(treindata['ActueleVertrekTijd'])
        datum_en_tijd = datum_en_tijd.split("T")
        tijd = datum_en_tijd[1].split(":")
        uren = int(tijd[0]) + 2
        if uren > 23:
            uren -= 24

        tkinter.messagebox.showinfo("", "U moet " + treindata['AantalOverstappen'] + " overstappen." +
                                    "\nDe geplande reistijd is: " + treindata['GeplandeReisTijd'] +
                                    "\nActuele vertrektijd: " + str(uren) + ":" + str(tijd[1]))

        treinTijdenBeginstation_entry.delete(0, "end")
        treinTijdenEindstation_entry.delete(0, "end")

        toonHoofdFrame()

    except:
        tkinter.messagebox.showinfo("", "Dit station is niet gevonden of het is fout getyped.")


# toonHoofdFrame() zorgt ervoor dat alle andere frames worden weggehaald en alleen het hoofdmenuframe laat zien.
def toonHoofdFrame():
    registermenuFrame.pack_forget()
    informatiemenuFrame.pack_forget()
    algemeneInformatiemenuFrame.pack_forget()
    stallenmenuFrame.pack_forget()
    ophalenmenuFrame.pack_forget()
    persoonlijkeInlogFrame.pack_forget()
    persoonlijkeInformatieFrame.pack_forget()
    treinTijdenFrame.pack_forget()
    hoofdmenuFrame.pack(padx=50, pady=10)


# Als je van hoofdmenu naar "Fiets registreren" gaat dan wordt het hoofdmenu weggehaald en vervolgens wordt
# het registerFrame opgeroepen.
def toonRegisterFrame():
    hoofdmenuFrame.pack_forget()
    registermenuFrame.pack(padx=10, pady=10)


# Algemene_informatie_aanvragen geeft het aantal plaatsen terug die nog vrij zijn.
# Bij meer dan 0 plaatsen wordt het hoofdmenu weggehaald en kom je in het "Fiets stallen" menu terecht.
# Als er geen plekken beschikbaar zijn dan krijg je een popup met de tekst "Er zijn geen plekken beschikbaar."
def toonStallenFrame():
    if algemene_informatie_aanvragen() > 0:
        hoofdmenuFrame.pack_forget()
        informatiemenuFrame.pack_forget()
        stallenmenuFrame.pack(padx=10, pady=10)
    else:
        tkinter.messagebox.showinfo("", "Er zijn geen plekken beschikbaar")


# Als je op de knop "Fiets ophalen" klikt dan wordt het hoofdmenu weggehaald en
# kom je in het "Fiets ophalen" menu terecht.
def toonOphalenFrame():
    hoofdmenuFrame.pack_forget()
    ophalenmenuFrame.pack(padx=10, pady=10)


# Bij het klikken op het "Informatie aanvragen" knop wordt het hoofdmenuFrame weggehaald en
# wordt het informatiemenuFrame gepackt die dan vervolgens op je beelscherm te zien is.
# In de functie staan ook andere Frames die worden weggehaald.
# Als we dat niet doen dan komen er verschillende frames op een venster.
def toonInformatieFrame():
    hoofdmenuFrame.pack_forget()
    algemeneInformatiemenuFrame.pack_forget()
    persoonlijkeInlogFrame.pack_forget()
    treinTijdenFrame.pack_forget()
    informatiemenuFrame.pack(padx=50, pady=10)


# Als er op "Informatie opvragen" wordt geklikt en je gaat vervolgens naar "Algemene informatie".
# Dan zorgt dit ervoor dat de informatiemenuFrame wordt weggehaald en
# vervolgens de "Algemene informatie" menu laat zien.
def toonAlgemeneInformatieFrame():
    informatiemenuFrame.pack_forget()
    algemeneInformatiemenuFrame.pack(padx=10, pady=10)


# Als er op "Informatie aanvragen" wordt geklikt en je gaat vervolgens door naar "Persoonlijke informatie".
# Dan zorgt dit ervoor dat je het hoofd menu en de informatie menu vergeet.
# Bij het klikken op "Persoonlijke informatie" wordt een inlog menu geopend met persoonlijkeInlogFrame.
def toonPersoonlijkeInlogFrame():
    hoofdmenuFrame.pack_forget()
    informatiemenuFrame.pack_forget()
    persoonlijkeInlogFrame.pack()


# Als er op "Log in" wordt geklikt in het inlogscherm van "persoonlijke informatie", dan zorgt dit ervoor dat het
# inlogscherm wordt vergeten en vervolgens een menu opent met je persoonlijke informatie.
def toonPersoonlijkeInformatieFrame():
    persoonlijkeInlogFrame.pack_forget()
    persoonlijkeInformatieFrame.pack(padx=10, pady=10)


# Als er op "Informatie aanvragen" wordt geklikt en daar op "Trein tijden".
# Dan zorgt dit ervoor dat we de "Invormatie aanvragen" frame weghalen en de treintijden frame laten zien.
def toonTreinTijdenFrame():
    informatiemenuFrame.pack_forget()
    treinTijdenFrame.pack(padx=10, pady=10)


filecheck()

# Root van de gui. Dit zorgt ervoor dat je een venster maakt. root.resizable is dat je het venster niet kunt vergroten.
# Daarna hebben we configure die in dit geval ervoor zorgt dat we een gele achtergrond krijgen.
root = tkinter.Tk()
root.title("NS-Fietsenstalling")
root.resizable(False, False)
root.configure(background="yellow")

# Hoofdmenu. Dit maakt een frame aan.
hoofdmenuFrame = tkinter.Frame(root)
hoofdmenuFrame.configure(background="yellow")
hoofdmenuFrame.pack()

# Hier wordt een stuk tekst aangemaakt die vervolgens in de gui geplaats kan worden.
# In dit geval in het hoofdmenu frame.
titel_label = tkinter.Label(master=hoofdmenuFrame, text="NS-Fietsstalling", background="yellow", font=20)
titel_label.grid(row=0, column=0, pady=5)

# Hier worden knoppen gemaakt die je in het hoofdmenu frame terug ziet komen.
registrerenknop = tkinter.Button(master=hoofdmenuFrame, text="Fiets registreren", width=25, command=toonRegisterFrame)
registrerenknop.grid(row=1, column=0, pady=5)

stallenKnop = tkinter.Button(master=hoofdmenuFrame, text="Fiets stallen", width=25, command=toonStallenFrame)
stallenKnop.grid(row=2, column=0, pady=5)

ophalenKnop = tkinter.Button(master=hoofdmenuFrame, text="Fiets ophalen", width=25, command=toonOphalenFrame)
ophalenKnop.grid(row=3, column=0, pady=5)

informatieOpvragenKnop = tkinter.Button(master=hoofdmenuFrame, text="Informatie opvragen", width=25,
                                        command=toonInformatieFrame)
informatieOpvragenKnop.grid(row=4, column=0, pady=5)

knopAfsluiten = tkinter.Button(master=hoofdmenuFrame, text="Afsluiten", width=25, command=sys.exit)
knopAfsluiten.grid(row=5, column=0, pady=5)

# Registreren. Hier wordt een frame aangemaakt voor het menu "Fiets registreren".
registermenuFrame = tkinter.Frame(root)
registermenuFrame.configure(background="yellow")
registermenuFrame.pack()

# Hier wordt een stuk tekst aangemaakt die vervolgens in de gui geplaats kan worden.
# In dit geval in het register menu frame.
naam_label = tkinter.Label(master=registermenuFrame, text="Voer hier je naam in: ", background="yellow")
naam_label.grid(row=0, column=0, pady=5)

# Hier wordt een entry aangemaakt. In een entry kun je tekst typen.
# Deze entry kun je terug zien in het register menu frame
naam_entry = tkinter.Entry(registermenuFrame)
naam_entry.grid(row=0, column=1)
naam_entry.delete(0, "end")

# Hier wordt een stuk tekst aangemaakt die vervolgens in de gui geplaats kan worden.
# In dit geval in het register menu frame.
wachtwoord_label = tkinter.Label(master=registermenuFrame, text="Voer hier je wachtwoord in: ", background="yellow")
wachtwoord_label.grid(row=1, column=0)

# Hier wordt een entry aangemaakt. In een entry kun je tekst typen.
# Deze entry kun je terug zien in het register menu frame
wachtwoord_entry = tkinter.Entry(registermenuFrame)
wachtwoord_entry.grid(row=1, column=1)

# Hier wordt een stuk tekst aangemaakt die vervolgens in de gui geplaats kan worden.
# In dit geval in het register menu frame.
telefoonnummer_label = tkinter.Label(master=registermenuFrame, text="Voer hier je telefoonnummer in: ",
                                     background="yellow")
telefoonnummer_label.grid(row=2, column=0, pady=5)

# Hier wordt een entry aangemaakt. In een entry kun je tekst typen.
# Deze entry kun je terug zien in het register menu frame
telefoonnummer_entry = tkinter.Entry(registermenuFrame)
telefoonnummer_entry.grid(row=2, column=1)

# Hier wordt een stuk tekst aangemaakt die vervolgens in de gui geplaats kan worden.
# In dit geval in het register menu frame.
email_label = tkinter.Label(master=registermenuFrame, text="Voer hier je e-mail in: ", background="yellow")
email_label.grid(row=3, column=0)

# Hier wordt een entry aangemaakt. In een entry kun je tekst typen.
# Deze entry kun je terug zien in het register menu frame
email_entry = tkinter.Entry(registermenuFrame)
email_entry.grid(row=3, column=1)

# Hier worden verschillende knoppen aangemaakt die vervolgens in het register frame te zien zijn.
knopregistreer = tkinter.Button(master=registermenuFrame, text="Registreer", command=registreren)
knopregistreer.grid(row=4, column=1, pady=5)

knopterugRegistreren = tkinter.Button(master=registermenuFrame, text="Terug", command=toonHoofdFrame)
knopterugRegistreren.grid(row=4, column=0, pady=5)

# Stallen. Hier wordt een frame aangemaakt voor het menu "Fiets stallen".
stallenmenuFrame = tkinter.Frame(root)
stallenmenuFrame.configure(background="yellow")
stallenmenuFrame.pack()

# Hier wordt een stuk tekst aangemaakt die vervolgens in de gui geplaats kan worden.
# In dit geval in het stallen menu frame.
inlogNaamStallen_label = tkinter.Label(master=stallenmenuFrame, text="Voer hier je e-mailadres in: ",
                                       background="yellow")
inlogNaamStallen_label.grid(row=0, column=0, pady=5)

# Hier wordt een entry aangemaakt. In een entry kun je tekst typen.
inlogNaamStallen_entry = tkinter.Entry(master=stallenmenuFrame)
inlogNaamStallen_entry.grid(row=0, column=1)

# Hier wordt een stuk tekst aangemaakt die vervolgens in de gui geplaats kan worden.
# In dit geval in het stallen menu frame.
inlogWachtwoordStallen_label = tkinter.Label(master=stallenmenuFrame, text="Voer hier je wachtwoord in: ",
                                             background="yellow")
inlogWachtwoordStallen_label.grid(row=1, column=0)

# Hier wordt een entry aangemaakt. In een entry kun je tekst typen.
# Deze entry kun je terug zien in het stallen menu frame
inlogWachtwoordStallen_entry = tkinter.Entry(master=stallenmenuFrame, show="*")
inlogWachtwoordStallen_entry.grid(row=1, column=1)

# Hier wordt een stuk tekst aangemaakt die vervolgens in de gui geplaats kan worden.
# In dit geval in het stallen menu frame.
inlogFietsnummerStallen_label = tkinter.Label(master=stallenmenuFrame, text="Voer hier je fietsnummer in: ",
                                              background="yellow")
inlogFietsnummerStallen_label.grid(row=2, column=0, pady=5)

# Hier wordt een entry aangemaakt. In een entry kun je tekst typen.
# Deze entry kun je terug zien in het stallen menu frame
inlogFietsnummerStallen_entry = tkinter.Entry(master=stallenmenuFrame)
inlogFietsnummerStallen_entry.grid(row=2, column=1)

# Hier worden verschillende knoppen aangemaakt die vervolgens in het stallen frame te zien zijn.
inlogKnopStallen = tkinter.Button(master=stallenmenuFrame, text="Log in", command=inlog_stallen)
inlogKnopStallen.grid(row=3, column=1, pady=5)

knopterugStallen = tkinter.Button(master=stallenmenuFrame, text="Terug", command=toonHoofdFrame)
knopterugStallen.grid(row=3, column=0, pady=5)

# Ophalen. Hier wordt een frame aangemaakt voor het menu "Fiets ophalen".
ophalenmenuFrame = tkinter.Frame(root)
ophalenmenuFrame.configure(background="yellow")
ophalenmenuFrame.pack()

# Hier wordt een stuk tekst aangemaakt die vervolgens in de gui geplaats kan worden.
# In dit geval in het ophalen menu frame.
inlogNaamOphalen_label = tkinter.Label(master=ophalenmenuFrame, text="Voer hier je e-mailadres in: ",
                                       background="yellow")
inlogNaamOphalen_label.grid(row=0, column=0, pady=5)

# Hier wordt een entry aangemaakt. In een entry kun je tekst typen.
# Deze entry kun je terug zien in het ophalen menu frame
inlogNaamOphalen_entry = tkinter.Entry(master=ophalenmenuFrame)
inlogNaamOphalen_entry.grid(row=0, column=1)

# Hier wordt een stuk tekst aangemaakt die vervolgens in de gui geplaats kan worden.
# In dit geval in het ophalen menu frame.
inlogWachtwoordOphalen_label = tkinter.Label(master=ophalenmenuFrame, text="Voer hier je wachtwoord in: ",
                                             background="yellow")
inlogWachtwoordOphalen_label.grid(row=1, column=0)

# Hier wordt een entry aangemaakt. In een entry kun je tekst typen.
# Deze entry kun je terug zien in het ophalen menu frame.
inlogWachtwoordOphalen_entry = tkinter.Entry(master=ophalenmenuFrame, show="*")
inlogWachtwoordOphalen_entry.grid(row=1, column=1)

# Hier wordt een stuk tekst aangemaakt die vervolgens in de gui geplaats kan worden.
# In dit geval in het ophalen menu frame.
inlogFietsnummerOphalen_label = tkinter.Label(master=ophalenmenuFrame, text="Voer hier je fietsnummer in: ",
                                              background="yellow")
inlogFietsnummerOphalen_label.grid(row=2, column=0, pady=5)

# Hier wordt een entry aangemaakt. In een entry kun je tekst typen.
# Deze entry kun je terug zien in het ophalen menu frame.
inlogFietsnummerOphalen_entry = tkinter.Entry(master=ophalenmenuFrame)
inlogFietsnummerOphalen_entry.grid(row=2, column=1)

# Hier worden verschillende knoppen aangemaakt die vervolgens in het ophalen frame te zien zijn.
knopterugOphalen = tkinter.Button(master=ophalenmenuFrame, text="Terug", command=toonHoofdFrame)
knopterugOphalen.grid(row=3, column=0, pady=5)

inlogKnopOphalen = tkinter.Button(master=ophalenmenuFrame, text="Log in", command=inlog_ophalen)
inlogKnopOphalen.grid(row=3, column=1)

# Informatie opvragen. Hier wordt een frame aangemaakt voor het menu "Informatie aanvragen".
informatiemenuFrame = tkinter.Frame(root)
informatiemenuFrame.configure(background="yellow")
informatiemenuFrame.pack()

# Hier worden verschillende knoppen aangemaakt die vervolgens in het ophalen frame te zien zijn.
algemeneInformatieKnop = tkinter.Button(master=informatiemenuFrame, text="Algemene informatie", width=25,
                                        command=toonAlgemeneInformatieFrame)
algemeneInformatieKnop.grid(row=0, column=0, pady=5)

persoonlijkeInformatieKnop = tkinter.Button(master=informatiemenuFrame, text="Persoonlijke informatie", width=25,
                                            command=toonPersoonlijkeInlogFrame)
persoonlijkeInformatieKnop.grid(row=1, column=0, pady=5)

treinTijdenKnop = tkinter.Button(master=informatiemenuFrame, text="Trein tijden", width=25,
                                 command=toonTreinTijdenFrame)
treinTijdenKnop.grid(row=2, column=0, pady=5)

knopterugInformatieOpvragen = tkinter.Button(master=informatiemenuFrame, text="Terug", width=25, command=toonHoofdFrame)
knopterugInformatieOpvragen.grid(row=3, column=0, pady=5)

# informatie opvragen/algemene informatie. Hier wordt een frame aangemaakt voor het menu "algemene informatie".
algemeneInformatiemenuFrame = tkinter.Frame(root)
algemeneInformatiemenuFrame.configure(background="yellow")
algemeneInformatiemenuFrame.pack()

# Hier worden regels aangemaakt waar je tekst in kwijt kunt en vervolgens in de gui geplaats kan worden.
# In dit geval in het algemene informatie menu frame.
aantalplekken_label = tkinter.Label(master=algemeneInformatiemenuFrame, text="Er zijn nog " + str(
    algemene_informatie_aanvragen()) + " van de 1000 plekken over.", background="yellow")
aantalplekken_label.pack()

kostenperdag_label = tkinter.Label(master=algemeneInformatiemenuFrame,
                                   text="De kosten voor het bergen van uw fiets zijn \u20ac2.50 per dag.",
                                   background="yellow")
kostenperdag_label.pack()

eerstedaggratis_label = tkinter.Label(master=algemeneInformatiemenuFrame, text="De eerste dag is gratis.",
                                      background="yellow")
eerstedaggratis_label.pack()

# Hier wordt een knop aangemaakt. Die ervoor zorgt dat je terug kunt keren naar de vorige menu.
knopterugAlgemenInformatie = tkinter.Button(master=algemeneInformatiemenuFrame, text="Terug",
                                            command=toonInformatieFrame)
knopterugAlgemenInformatie.pack()

# informatie opvragen/persoonlijke informatie/inlog. Hier wordt een frame aangemaakt voor
# het menu "persoonlijke informatie/inloggen". Dit is het inlogmenu frame voor "persoonlijke informatie".
persoonlijkeInlogFrame = tkinter.Frame(root)
persoonlijkeInlogFrame.configure(background="yellow")
persoonlijkeInlogFrame.pack()

# Hier wordt een stuk tekst aangemaakt die vervolgens in de gui geplaats kan worden.
# In dit geval in het persoonlijke informatie inlog menu frame.
inlogNaamPersoonlijk_label = tkinter.Label(master=persoonlijkeInlogFrame, text="Voer hier je e-mailadres in: ",
                                           background="yellow")
inlogNaamPersoonlijk_label.grid(row=0, column=0, pady=5)

inlogNaamPersoonlijk_entry = tkinter.Entry(master=persoonlijkeInlogFrame)
inlogNaamPersoonlijk_entry.grid(row=0, column=1, padx=10)

# Hier wordt een stuk tekst aangemaakt die vervolgens in de gui geplaats kan worden.
# In dit geval in het persoonlijke informatie inlog menu frame.
inlogWachtwoordPersoonlijk_label = tkinter.Label(master=persoonlijkeInlogFrame, text="Voer hier je wachtwoord in: ",
                                                 background="yellow")
inlogWachtwoordPersoonlijk_label.grid(row=1, column=0)

# Hier wordt een entry aangemaakt. In een entry kun je tekst typen.
# Deze entry kun je terug zien in het persoonlijke informatie inlog menu frame.
inlogWachtwoordPersoonlijk_entry = tkinter.Entry(master=persoonlijkeInlogFrame, show="*")
inlogWachtwoordPersoonlijk_entry.grid(row=1, column=1)

# Hier worden verschillende knoppen aangemaakt die vervolgens in het persoonlijke informatie inlog frame te zien zijn.
inlogKnopPersoonlijk_button = tkinter.Button(master=persoonlijkeInlogFrame, text="Log in",
                                             command=persoonlijke_informatie_aanvragen)
inlogKnopPersoonlijk_button.grid(row=2, column=1)

knopterugPersoonlijkeInformatie = tkinter.Button(master=persoonlijkeInlogFrame, text="Terug",
                                                 command=toonInformatieFrame)
knopterugPersoonlijkeInformatie.grid(row=2, column=0, pady=5)

# informatie opvragen/persoonlijke informatie/inlog/informatie.
# Hier wordt een frame aangemaakt voor na het inloggen bij "persoonlijke informatie".
persoonlijkeInformatieFrame = tkinter.Frame(root)
persoonlijkeInformatieFrame.configure(background="yellow")
persoonlijkeInformatieFrame.pack()

# Informatie opvragen/trein tijden. Hier wordt een frame aangemaakt voor het menu "Trein tijden".
treinTijdenFrame = tkinter.Frame(root)
treinTijdenFrame.configure(background="yellow")
treinTijdenFrame.pack()

# Hier wordt een stuk tekst aangemaakt die vervolgens in de gui geplaats kan worden.
# In dit geval in het treintijden menu frame.
treinTijdenBeginstation_label = tkinter.Label(master=treinTijdenFrame, text="Beginstation: ", background="yellow")
treinTijdenBeginstation_label.grid(row=0, column=0, pady=5)

# Hier wordt een entry aangemaakt. In een entry kun je tekst typen.
# Deze entry kun je terug zien in het treintijden menu frame.
treinTijdenBeginstation_entry = tkinter.Entry(master=treinTijdenFrame)
treinTijdenBeginstation_entry.grid(row=0, column=1)

# Hier wordt een stuk tekst aangemaakt die vervolgens in de gui geplaats kan worden.
# In dit geval in het treintijden menu frame.
treinTijdenEindstation_label = tkinter.Label(master=treinTijdenFrame, text="Eindstation: ", background="yellow")
treinTijdenEindstation_label.grid(row=1, column=0, pady=5)

# Hier wordt een entry aangemaakt. In een entry kun je tekst typen.
# Deze entry kun je terug zien in het treintijden menu frame.
treinTijdenEindstation_entry = tkinter.Entry(master=treinTijdenFrame)
treinTijdenEindstation_entry.grid(row=1, column=1)

# Hier worden verschillende knoppen aangemaakt die vervolgens in het treintijden frame te zien zijn.
knopverderTreinTijden = tkinter.Button(master=treinTijdenFrame, text="Verder", command=trein_tijden)
knopverderTreinTijden.grid(row=2, column=1, pady=5)

knopterugTreinTijden = tkinter.Button(master=treinTijdenFrame, text="Terug", command=toonInformatieFrame)
knopterugTreinTijden.grid(row=2, column=0)

toonHoofdFrame()

root.mainloop()
