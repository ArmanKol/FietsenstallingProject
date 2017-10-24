import tkinter
import sys
import random
import csv

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

    mail = email_entry.get()
    mail_lijst = []
    for gegeven in gegevens:
        mail_lijst.append(gegeven['mail'])

    while mail in mail_lijst:
        print("Dit e-mail adress is al geregistreerd")
        mail = email_entry.get()

    naam = naam_entry.get()

    while True:
        try:
            telefoonnummer = telefoonnummer_entry.get()
            break
        except:
            print("Telefoonnummer klopt niet..")

    wachtwoord = wachtwoord_entry.get()

    while len(wachtwoord) <= 6:
        wachtwoord = wachtwoord_entry.get()

    fietsnummer = int(random.randint(1000, 9999))

    fietsnummer_lijst = []
    for gegeven in gegevens:
        fietsnummer_lijst.append(gegeven['fietsnummer'])

    while str(fietsnummer) in fietsnummer_lijst:
        fietsnummer = int(random.randint(1000, 9999))

    nieuwe_gegevens = str(fietsnummer) + ';' + naam + ';' + mail + ';' + wachtwoord + ';' + str(telefoonnummer)

    bestand = open('database/gebruikers.csv', 'a')
    bestand.write(nieuwe_gegevens + '\n')
    bestand.close()

def toonHoofdFrame():
    registermenuFrame.pack_forget()
    hoofdmenuFrame.pack(padx=50, pady=10)

def toonRegisterFrame():
    hoofdmenuFrame.pack_forget()
    registermenuFrame.pack(padx=10, pady=10)


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

stallenKnop = tkinter.Button(master=hoofdmenuFrame, text="Fiets stallen", width=25)
stallenKnop.grid(row=2, column=0, pady=5)

ophalenKnop = tkinter.Button(master=hoofdmenuFrame, text="Fiets ophalen", width=25)
ophalenKnop.grid(row=3, column=0, pady=5)


informatieOpvragenKnop = tkinter.Button(master=hoofdmenuFrame, text="Informatie opvragen", width=25)
informatieOpvragenKnop.grid(row=4, column=0, pady=5)

knopAfsluiten = tkinter.Button(master=hoofdmenuFrame, text="Afsluiten", width=25, command=sys.exit)
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

toonHoofdFrame()
root.mainloop()