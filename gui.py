import tkinter
import sys
import csv
import random
import tkinter.messagebox
import datetime
import pyotp
import telepot


def telegramRead():
    bot = telepot.Bot("370325529:AAGKGqP-dHRoyKb2FKnPtMyYCdOhcGKLK5Q")
    response = bot.getUpdates()  # pakt het laatst verzonden bericht aan de bot
    response_1 = response[-1]
    UserID = response_1['message']['chat']['id']  # pakt het ID van de verzender
    UserBericht = response_1['message']['text']

    return UserBericht


def captcha_check():
    hotp = pyotp.HOTP('base32secret3232')
    random_seed = random.randint(9999, 99999)
    tkinter.messagebox.showinfo("", "Ga naar: http://t.me/BevFietsBot" + "\nen stuur deze code: " + hotp.at(random_seed) + "\nGa na versturen verder.")
    telegram_output = telegramRead()

    if hotp.verify(telegram_output, random_seed) == True:
        return 1
    else:
        tkinter.messagebox.showinfo("", "Inlog gegevens niet correct")
        return 0


def csvread(bestandsnaam):
    with open("database/" + bestandsnaam, "r") as ReadMyCsv:
        reader = csv.DictReader(ReadMyCsv, delimiter=";")

        gegevens = []
        for gegeven in reader:
            gegevens.append(gegeven)

    return gegevens


def registreren():
    """Functie voor het registreren van de gebruiker. Slaat de gegevens op in gebruikers.csv"""
    gegevens_gebruikers = csvread("gebruikers.csv")
    gegevens_status = 0

    mail_lijst = []

    wachtwoord = wachtwoord_entry.get()
    naam = naam_entry.get()
    mail = email_entry.get()
    telefoonnummer = telefoonnummer_entry.get()

    for gegeven in gegevens_gebruikers:
        mail_lijst.append(gegeven['mail'])

    if mail in mail_lijst:
        tkinter.messagebox.showinfo("", "Dit e-mail adress is al geregistreerd.")
    else:
        gegevens_status += 1
        pass

    if len(wachtwoord) <= 6:
        tkinter.messagebox.showinfo("", "Je hebt een te korte wachtwoord ingevoerd.")
    else:
        gegevens_status += 1
        pass

    fietsnummer = int(random.randint(1000, 9999))

    fietsnummer_lijst = []
    for gegeven in gegevens_gebruikers:
        fietsnummer_lijst.append(gegeven['fietsnummer'])

    while str(fietsnummer) in fietsnummer_lijst:
        fietsnummer = int(random.randint(1000, 9999))

    if gegevens_status == 2:
        nieuwe_gegevens = str(fietsnummer) + ';' + naam + ';' + mail + ';' + wachtwoord + ';' + str(telefoonnummer)
        registrerengelukt = tkinter.messagebox.showinfo("","Je bent succesvol geregistreerd.\n"+"Fietsnummer: "+str(fietsnummer))
        bestand = open('database/gebruikers.csv', 'a')
        bestand.write(nieuwe_gegevens + '\n')
        bestand.close()
        if registrerengelukt == "ok":
            return toonHoofdFrame()
    else:
        pass


def inlog_stallen():
    # gegevens voor het stallen
    gegevens_gebruiker = csvread("gebruikers.csv")
    gegevens_gestald = csvread("gestald.csv")

    vandaag = datetime.datetime.today()
    datum = vandaag.strftime('%d/%m/%Y')

    username = inlogNaamStallen_entry.get()
    password = inlogWachtwoordStallen_entry.get()
    fietsnummer = inlogFietsnummerStallen_entry.get()

    status_inloggen = 0
    fietsnummer_lijst = []

    # controleren gegevens gebruiker
    for item in gegevens_gebruiker:
        if str(item['wachtwoord']) == password and str(item['mail']) == username:
            status_inloggen = 1
        else:
            pass
    if status_inloggen == 0:
        tkinter.messagebox.showinfo("", "Inlog gegevens niet correct")
    else:
        pass

    # controleren of fiets al in de stalling staat
    for gegeven in gegevens_gestald:
        fietsnummer_lijst.append(gegeven['fietsnummer'])
    if fietsnummer in fietsnummer_lijst:
        tkinter.messagebox.showinfo("", "Fiets staat al in stalling..")
        status_inloggen = 0
    else:
        pass

    # telegram check voor two-factor authenticatie
    if status_inloggen == 1:
        status_inloggen = captcha_check()
    else:
        pass

    # fiets opslaan in bestand en succes bericht geven aan gebruiker
    if status_inloggen == 1:
        gegevens_stalling = str(fietsnummer) + ";" + datum
        inloggengelukt = tkinter.messagebox.showinfo("", "Je bent succesvol ingelogd.\n" + "Je fiets is gestald")
        bestand = open('database/gestald.csv', 'a')
        bestand.write(gegevens_stalling + '\n')
        bestand.close()
        if inloggengelukt == "ok":
            return toonHoofdFrame()
    else:
        pass


def inlog_ophalen():
    # gegevens voor het ophalen van de fiets
    gegevens_gebruiker = csvread("gebruikers.csv")
    gegevens_gestald = csvread("gestald.csv")

    username = inlogNaamOphalen_entry.get()
    password = inlogWachtwoordOphalen_entry.get()
    fietsnummer = inlogFietsnummerOphalen_entry.get()

    status_inloggen = 0
    fietsnummer_lijst = []


    # controleren gegevens gebruiker
    for item in gegevens_gebruiker:
        if str(item['wachtwoord']) == password and str(item['mail']) == username:
            status_inloggen = 1
        else:
            pass
    if status_inloggen == 0:
        tkinter.messagebox.showinfo("", "Inlog gegevens niet correct")
    else:
        pass

    # controleren of fiets in de stalling staat
    for gegeven in gegevens_gestald:
        fietsnummer_lijst.append(gegeven['fietsnummer'])
    if fietsnummer not in fietsnummer_lijst:
        tkinter.messagebox.showinfo("", "Fiets staat niet in stalling..")
        status_inloggen = 0
    else:
        pass

    # telegram check voor two-factor authenticatie
    if status_inloggen == 1:
        status_inloggen = captcha_check()
    else:
        pass

    if status_inloggen == 1:
        inloggengelukt = tkinter.messagebox.showinfo("", "Je bent succesvol ingelogd.\n" + "Je kan je fiets ophalen")

        for fiets in gegevens_gestald:
            if fiets['fietsnummer'] == fietsnummer:
                gegevens_gestald.remove(fiets)

        with open("database/gestald.csv", "w", newline='\n') as WriteMyCsv:
            veldnamen = ["fietsnummer", "staldatum"]
            writer = csv.DictWriter(WriteMyCsv, fieldnames=veldnamen, delimiter=";")
            writer.writeheader()

            for gegeven in gegevens_gestald:
                writer.writerow((gegeven))

        if inloggengelukt == "ok":
            return toonHoofdFrame()
    else:
        pass


def algemene_informatie_aanvragen():
    gegevens = csvread("gestald.csv")

    vrije_plekken = 1000 - (len(gegevens) + 1)

    return vrije_plekken
    #print("Er zijn nog " + str(vrije_plekken) + " van de 1000 plekken over.")
    #print("De kosten voor het bergen van uw fiets zijn \u20ac2.5 per dag.")
    #print("De eerste dag is gratis.")


def toonHoofdFrame():
    registermenuFrame.pack_forget()
    informatiemenuFrame.pack_forget()
    algemeneInformatiemenuFrame.pack_forget()
    stallenmenuFrame.pack_forget()
    ophalenmenuFrame.pack_forget()
    persoonlijkeInformatieFrame.pack_forget()
    hoofdmenuFrame.pack(padx=50, pady=10)


def toonRegisterFrame():
    hoofdmenuFrame.pack_forget()
    registermenuFrame.pack(padx=10, pady=10)


def toonStallenFrame():
    if algemene_informatie_aanvragen() > 0:
        hoofdmenuFrame.pack_forget()
        informatiemenuFrame.pack_forget()
        stallenmenuFrame.pack(padx=10, pady=10)
    else:
        tkinter.messagebox.showinfo("", "Er zijn geen plekke beschikbaar")


def toonOphalenFrame():
    hoofdmenuFrame.pack_forget()
    ophalenmenuFrame.pack(padx=10, pady=10)


def toonInformatieFrame():
    hoofdmenuFrame.pack_forget()
    algemeneInformatiemenuFrame.pack_forget()
    persoonlijkeInformatieFrame.pack_forget()
    informatiemenuFrame.pack(padx=50, pady=10)


def toonAlgemeneInformatieFrame():
    informatiemenuFrame.pack_forget()
    algemeneInformatiemenuFrame.pack()


def toonPersoonlijkeInformatieFrame():
    hoofdmenuFrame.pack_forget()
    informatiemenuFrame.pack_forget()
    persoonlijkeInformatieFrame.pack()


root = tkinter.Tk()
root.title("NS-Fietsenstalling")
root.resizable(False, False)
root.configure(background="yellow")

#nslogo = tkinter.PhotoImage("C:\\Users\\Arman.K\\PycharmProjects\\FietsenstallingProject\\nslogo.png")

#Hoofdmenu
hoofdmenuFrame = tkinter.Frame(root)
hoofdmenuFrame.configure(background="yellow")
hoofdmenuFrame.pack()

#backgroundFrame = tkinter.Label(master=hoofdmenuFrame, image=nslogo)
#backgroundFrame.grid(row=0)

titel_label = tkinter.Label(master=hoofdmenuFrame, text="NS-Fietsstalling", background="yellow", font=20)
titel_label.grid(row=0, column=0, pady=5)

registrerenknop = tkinter.Button(master=hoofdmenuFrame, text="Fiets registreren", width=25, command=toonRegisterFrame)
registrerenknop.grid(row=1, column=0, pady=5)

stallenKnop = tkinter.Button(master=hoofdmenuFrame, text="Fiets stallen", width=25, command=toonStallenFrame)
stallenKnop.grid(row=2, column=0, pady=5)

ophalenKnop = tkinter.Button(master=hoofdmenuFrame, text="Fiets ophalen", width=25, command=toonOphalenFrame)
ophalenKnop.grid(row=3, column=0, pady=5)


informatieOpvragenKnop = tkinter.Button(master=hoofdmenuFrame, text="Informatie opvragen", width=25, command=toonInformatieFrame)
informatieOpvragenKnop.grid(row=4, column=0, pady=5)

knopAfsluiten = tkinter.Button(master=hoofdmenuFrame, text="Afsluiten", width=25, command=sys.exit  )
knopAfsluiten.grid(row=5, column=0, pady=5)

#Registreren
registermenuFrame = tkinter.Frame(root)
registermenuFrame.configure(background="yellow")
registermenuFrame.pack()

naam_label = tkinter.Label(master=registermenuFrame, text="Voer hier je naam in: ", background="yellow")
naam_label.grid(row=0, column=0, pady=5)

naam_entry = tkinter.Entry(registermenuFrame)
naam_entry.grid(row=0, column=1)

wachtwoord_label = tkinter.Label(master=registermenuFrame, text="Voer hier je wachtwoord in: ", background="yellow")
wachtwoord_label.grid(row=1, column=0)

wachtwoord_entry = tkinter.Entry(registermenuFrame)
wachtwoord_entry.grid(row=1, column=1)

telefoonnummer_label = tkinter.Label(master=registermenuFrame, text="Voer hier je telefoonnummer in: ", background="yellow")
telefoonnummer_label.grid(row=2, column=0, pady=5)

telefoonnummer_entry = tkinter.Entry(registermenuFrame)
telefoonnummer_entry.grid(row=2, column=1)

email_label = tkinter.Label(master=registermenuFrame, text="Voer hier je e-mail in: ", background="yellow")
email_label.grid(row=3, column=0)

email_entry = tkinter.Entry(registermenuFrame)
email_entry.grid(row=3, column=1)

knopregistreer = tkinter.Button(master=registermenuFrame, text="Registreer", command=registreren)
knopregistreer.grid(row=4, column=1, pady=5)

knopterugRegistreren = tkinter.Button(master=registermenuFrame, text="Terug", command=toonHoofdFrame)
knopterugRegistreren.grid(row=4, column=0, pady=5)

#Stallen
stallenmenuFrame = tkinter.Frame(root)
stallenmenuFrame.configure(background="yellow")
stallenmenuFrame.pack()

inlogNaamStallen_label = tkinter.Label(master=stallenmenuFrame, text="Voer hier je e-mailadres in: ", background="yellow")
inlogNaamStallen_label.grid(row=0, column=0, pady=5)

inlogNaamStallen_entry = tkinter.Entry(master=stallenmenuFrame)
inlogNaamStallen_entry.grid(row=0, column=1)

inlogWachtwoordStallen_label = tkinter.Label(master=stallenmenuFrame, text="Voer hier je wachtwoord in: ", background="yellow")
inlogWachtwoordStallen_label.grid(row=1, column=0)

inlogWachtwoordStallen_entry = tkinter.Entry(master=stallenmenuFrame, show="*")
inlogWachtwoordStallen_entry.grid(row=1, column=1)

inlogFietsnummerStallen_label = tkinter.Label(master=stallenmenuFrame, text="Voer hier je fietsnummer in: ", background="yellow")
inlogFietsnummerStallen_label.grid(row=2, column=0, pady=5)

inlogFietsnummerStallen_entry = tkinter.Entry(master=stallenmenuFrame)
inlogFietsnummerStallen_entry.grid(row=2, column=1)

inlogKnopStallen = tkinter.Button(master=stallenmenuFrame, text="Log in", command=inlog_stallen)
inlogKnopStallen.grid(row=3, column=1, pady=5)

knopterugStallen = tkinter.Button(master=stallenmenuFrame, text="Terug", command=toonHoofdFrame)
knopterugStallen.grid(row=3, column=0, pady=5)

#Ophalen
ophalenmenuFrame = tkinter.Frame(root)
ophalenmenuFrame.configure(background="yellow")
ophalenmenuFrame.pack()

inlogNaamOphalen_label = tkinter.Label(master=ophalenmenuFrame, text="Voer hier je e-mailadres in: ", background="yellow")
inlogNaamOphalen_label.grid(row=0, column=0, pady=5)

inlogNaamOphalen_entry = tkinter.Entry(master=ophalenmenuFrame)
inlogNaamOphalen_entry.grid(row=0, column=1)

inlogWachtwoordOphalen_label = tkinter.Label(master=ophalenmenuFrame, text="Voer hier je wachtwoord in: ", background="yellow")
inlogWachtwoordOphalen_label.grid(row=1, column=0)

inlogWachtwoordOphalen_entry = tkinter.Entry(master=ophalenmenuFrame, show="*")
inlogWachtwoordOphalen_entry.grid(row=1, column=1)

inlogFietsnummerOphalen_label = tkinter.Label(master=ophalenmenuFrame, text="Voer hier je fietsnummer in: ", background="yellow")
inlogFietsnummerOphalen_label.grid(row=2, column=0, pady=5)

inlogFietsnummerOphalen_entry = tkinter.Entry(master=ophalenmenuFrame)
inlogFietsnummerOphalen_entry.grid(row=2, column=1)

knopterugOphalen = tkinter.Button(master=ophalenmenuFrame, text="Terug", command=toonHoofdFrame)
knopterugOphalen.grid(row=3, column=0, pady=5)

inlogKnopOphalen = tkinter.Button(master=ophalenmenuFrame, text="Log in", command=inlog_ophalen)
inlogKnopOphalen.grid(row=3, column=1)

#Informatie opvragen
informatiemenuFrame = tkinter.Frame(root)
informatiemenuFrame.configure(background="yellow")
informatiemenuFrame.pack()

algemeneInformatieKnop = tkinter.Button(master=informatiemenuFrame, text="Algemene informatie", width=25, command=toonAlgemeneInformatieFrame)
algemeneInformatieKnop.grid(row=0, column=0, pady=5)

persoonlijkeInformatieKnop = tkinter.Button(master=informatiemenuFrame, text="Persoonlijke informatie", width=25, command=toonPersoonlijkeInformatieFrame)
persoonlijkeInformatieKnop.grid(row=1, column=0, pady=5)

knopterugInformatieOpvragen = tkinter.Button(master=informatiemenuFrame, text="Terug", width=25, command=toonHoofdFrame)
knopterugInformatieOpvragen.grid(row=2, column=0, pady=5)

#informatie opvragen/algemene informatie
algemeneInformatiemenuFrame = tkinter.Frame(root)
algemeneInformatiemenuFrame.configure(background="yellow")
algemeneInformatiemenuFrame.pack()

aantalplekken_label = tkinter.Label(master=algemeneInformatiemenuFrame, text="Er zijn nog "+str(algemene_informatie_aanvragen())+" van de 1000 plekken over.", background="yellow")
aantalplekken_label.pack()

knopterugAlgemenInformatie = tkinter.Button(master=algemeneInformatiemenuFrame, text="Terug", command=toonInformatieFrame)
knopterugAlgemenInformatie.pack()

#informatie opvragen/persoonlijke informatie
persoonlijkeInformatieFrame = tkinter.Frame(root)
persoonlijkeInformatieFrame.configure(background="yellow")
persoonlijkeInformatieFrame.pack()

inlogNaamPersoonlijk_label = tkinter.Label(master=persoonlijkeInformatieFrame, text="Voer hier je naam/e-mailadres in: ", background="yellow")
inlogNaamPersoonlijk_label.grid(row=0, column=0, pady=5)

inlogNaamPersoonlijk_entry = tkinter.Entry(master=persoonlijkeInformatieFrame)
inlogNaamPersoonlijk_entry.grid(row=0, column=1, padx=10)

inlogWachtwoordPersoonlijk_label = tkinter.Label(master=persoonlijkeInformatieFrame, text="Voer hier je wachtwoord in: ", background="yellow")
inlogWachtwoordPersoonlijk_label.grid(row=1, column=0)

inlogWachtwoordPersoonlijk_entry = tkinter.Entry(master=persoonlijkeInformatieFrame, show="*")
inlogWachtwoordPersoonlijk_entry.grid(row=1, column=1)

inlogKnopPersoonlijk_button = tkinter.Button(master=persoonlijkeInformatieFrame, text="Log in")
inlogKnopPersoonlijk_button.grid(row=2, column=1)

knopterugPersoonlijkeInformatie = tkinter.Button(master= persoonlijkeInformatieFrame, text="Terug", command=toonInformatieFrame)
knopterugPersoonlijkeInformatie.grid(row=2, column=0, pady=5)


toonHoofdFrame()

root.mainloop()