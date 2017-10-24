import tkinter
import sys

def toonHoofdFrame():
    registermenuFrame.pack_forget()
    informatiemenuFrame.pack_forget()
    algemeneInformatiemenuFrame.pack_forget()
    stallenmenuFrame.pack_forget()
    ophalenmenuFrame.pack_forget()
    persoonlijkeInformatieFrame.pack_forget()
    hoofdmenuFrame.pack()

def toonRegisterFrame():
    hoofdmenuFrame.pack_forget()
    registermenuFrame.pack()

def toonStallenFrame():
    hoofdmenuFrame.pack_forget()
    informatiemenuFrame.pack_forget()
    stallenmenuFrame.pack()

def toonOphalenFrame():
    hoofdmenuFrame.pack_forget()
    ophalenmenuFrame.pack()

def toonInformatieFrame():
    hoofdmenuFrame.pack_forget()
    algemeneInformatiemenuFrame.pack_forget()
    persoonlijkeInformatieFrame.pack_forget()
    informatiemenuFrame.pack()

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
#root.geometry("280x170")
root.configure(background="yellow")

#Hoofdmenu
hoofdmenuFrame = tkinter.Frame(root)
hoofdmenuFrame.configure(background="yellow")
hoofdmenuFrame.pack()

titel_label = tkinter.Label(master=hoofdmenuFrame, text="NS-Fietsstalling", background="yellow", font=20)
titel_label.grid(row=0, column=0)

registrerenknop = tkinter.Button(master=hoofdmenuFrame, text="Fiets registreren", width=25, command=toonRegisterFrame)
registrerenknop.grid(row=1, column=0)

stallenKnop = tkinter.Button(master=hoofdmenuFrame, text="Fiets stallen", width=25, command=toonStallenFrame)
stallenKnop.grid(row=2, column=0)

ophalenKnop = tkinter.Button(master=hoofdmenuFrame, text="Fiets ophalen", width=25, command=toonOphalenFrame)
ophalenKnop.grid(row=3, column=0)


informatieOpvragenKnop = tkinter.Button(master=hoofdmenuFrame, text="Informatie opvragen", width=25, command=toonInformatieFrame)
informatieOpvragenKnop.grid(row=4, column=0)

knopAfsluiten = tkinter.Button(master=hoofdmenuFrame, text="Afsluiten", width=25, command=sys.exit  )
knopAfsluiten.grid(row=5, column=0)

#Registreren
registermenuFrame = tkinter.Frame(root)
registermenuFrame.configure(background="yellow")
registermenuFrame.pack()

naam_label = tkinter.Label(master=registermenuFrame, text="Voer hier je naam in: ", background="yellow")
naam_label.grid(row=0, column=0)

naam_entry = tkinter.Entry(registermenuFrame)
naam_entry.grid(row=0, column=1)

wachtwoord_label = tkinter.Label(master=registermenuFrame, text="Voer hier je wachtwoord in: ", background="yellow")
wachtwoord_label.grid(row=1, column=0)

wachtwoord_entry = tkinter.Entry(registermenuFrame)
wachtwoord_entry.grid(row=1, column=1)

telefoonnummer_label = tkinter.Label(master=registermenuFrame, text="Voer hier je telefoonnummer in: ", background="yellow")
telefoonnummer_label.grid(row=2, column=0)

telefoonnummer_entry = tkinter.Entry(registermenuFrame)
telefoonnummer_entry.grid(row=2, column=1)

email_label = tkinter.Label(master=registermenuFrame, text="Voer hier je e-mail in: ", background="yellow")
email_label.grid(row=3, column=0)

email_entry = tkinter.Entry(registermenuFrame)
email_entry.grid(row=3, column=1)

knopregistreer = tkinter.Button(master=registermenuFrame, text="Registreer")
knopregistreer.grid(row=4, column=1)

knopterugRegistreren = tkinter.Button(master=registermenuFrame, text="Terug", command=toonHoofdFrame)
knopterugRegistreren.grid(row=4, column=0)

#Stallen
stallenmenuFrame = tkinter.Frame(root)
stallenmenuFrame.configure(background="yellow")
stallenmenuFrame.pack()

inlogNaamStallen_label = tkinter.Label(master=stallenmenuFrame, text="Voer hier je naam/e-mailadres in: ", background="yellow")
inlogNaamStallen_label.grid(row=0, column=0, pady=5)

inlogNaamStallen_entry = tkinter.Entry(master=stallenmenuFrame)
inlogNaamStallen_entry.grid(row=0, column=1, padx=10)

inlogWachtwoordStallen_label = tkinter.Label(master=stallenmenuFrame, text="Voer hier je wachtwoord in: ", background="yellow")
inlogWachtwoordStallen_label.grid(row=1, column=0)

inlogWachtwoordStallen_entry = tkinter.Entry(master=stallenmenuFrame, show="*")
inlogWachtwoordStallen_entry.grid(row=1, column=1)

inlogKnopStallen_button = tkinter.Button(master=stallenmenuFrame, text="Log in")
inlogKnopStallen_button.grid(row=2, column=1)

knopterugStallen = tkinter.Button(master=stallenmenuFrame, text="Terug", command=toonHoofdFrame)
knopterugStallen.grid(row=2, column=0)

#Ophalen
ophalenmenuFrame = tkinter.Frame(root)
ophalenmenuFrame.configure(background="yellow")
ophalenmenuFrame.pack()



knopterugOphalen = tkinter.Button(master=ophalenmenuFrame, text="Terug", command=toonHoofdFrame)
knopterugOphalen.pack()

#Informatie opvragen
informatiemenuFrame = tkinter.Frame(root)
informatiemenuFrame.configure(background="yellow")
informatiemenuFrame.pack()

algemeneInformatieKnop = tkinter.Button(master=informatiemenuFrame, text="Algemene informatie", command=toonAlgemeneInformatieFrame)
algemeneInformatieKnop.grid(row=0, column=0)

persoonlijkeInformatieKnop = tkinter.Button(master=informatiemenuFrame, text="Persoonlijke informatie", command=toonPersoonlijkeInformatieFrame)
persoonlijkeInformatieKnop.grid(row=0, column=1)

knopterugInformatieOpvragen = tkinter.Button(master=informatiemenuFrame, text="Terug", command=toonHoofdFrame)
knopterugInformatieOpvragen.grid(row=1, column=1)

#informatie opvragen/algemene informatie
algemeneInformatiemenuFrame = tkinter.Frame(root)
algemeneInformatiemenuFrame.configure(background="yellow")
algemeneInformatiemenuFrame.pack()

aantalplekken_label = tkinter.Label(master=algemeneInformatiemenuFrame, text="Er zijn nog x plekken vrij", background="yellow")
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
knopterugPersoonlijkeInformatie.grid(row=2, column=0)



toonHoofdFrame()

root.mainloop()