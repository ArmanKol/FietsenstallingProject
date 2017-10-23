import tkinter
import sys
import os

def toonHoofdFrame():
    RegistermenuFrame.pack_forget()
    informatiemenuFrame.pack_forget()
    algemeneInformatiemenuFrame.pack_forget()
    stallenmenuFrame.pack_forget()
    ophalenmenuFrame.pack_forget()
    hoofdmenuFrame.pack()

def toonRegisterFrame():
    hoofdmenuFrame.pack_forget()
    RegistermenuFrame.pack()

def toonStallenFrame():
    hoofdmenuFrame.pack_forget()
    stallenmenuFrame.pack()

def toonOphalenFrame():
    hoofdmenuFrame.pack_forget()
    ophalenmenuFrame.pack()

def toonInformatieFrame():
    hoofdmenuFrame.pack_forget()
    algemeneInformatiemenuFrame.pack_forget()
    informatiemenuFrame.pack()

def toonAlgemeneInformatieFrame():
    informatiemenuFrame.pack_forget()
    algemeneInformatiemenuFrame.pack()

root = tkinter.Tk()
root.title("NS-Fietsenstalling")
root.resizable(False, False)
root.configure(background="yellow")

#Hoofdmenu
hoofdmenuFrame = tkinter.Frame(root)
hoofdmenuFrame.configure(background="yellow")
hoofdmenuFrame.pack()

titel_label = tkinter.Label(master=hoofdmenuFrame, text="NS-Fietsstalling", background="yellow")
titel_label.grid(row=0, column=0)

registrerenknop = tkinter.Button(master=hoofdmenuFrame, text="Fiets registreren", width=25, command=toonRegisterFrame)
registrerenknop.grid(row=1, column=0)

stallenKnop = tkinter.Button(master=hoofdmenuFrame, text="Fiets stallen", width=25, command=toonStallenFrame)
stallenKnop.grid(row=2, column=0)

ophalenKnop = tkinter.Button(master=hoofdmenuFrame, text="Fiets ophalen", width=25, command=toonOphalenFrame)
ophalenKnop.grid(row=3, column=0)


informatieOpvragenKnop = tkinter.Button(master=hoofdmenuFrame, text="Informatie opvragen", width=25, command=toonInformatieFrame)
informatieOpvragenKnop.grid(row=4, column=0)

#Registreren
RegistermenuFrame = tkinter.Frame(root)
RegistermenuFrame.configure(background="yellow")
RegistermenuFrame.pack()

naam_label = tkinter.Label(master=RegistermenuFrame, text="Voer hier je naam in: ", background="yellow")
naam_label.grid(row=0, column=0)

naam_entry = tkinter.Entry(RegistermenuFrame)
naam_entry.grid(row=0, column=1)

wachtwoord_label = tkinter.Label(master=RegistermenuFrame, text="Voer hier je wachtwoord in: ", background="yellow")
wachtwoord_label.grid(row=1, column=0)

wachtwoord_entry = tkinter.Entry(RegistermenuFrame)
wachtwoord_entry.grid(row=1, column=1)

telefoonnummer_label = tkinter.Label(master=RegistermenuFrame, text="Voer hier je telefoonnummer in: ", background="yellow")
telefoonnummer_label.grid(row=2, column=0)

telefoonnummer_entry = tkinter.Entry(RegistermenuFrame)
telefoonnummer_entry.grid(row=2, column=1)

email_label = tkinter.Label(master=RegistermenuFrame, text="Voer hier je e-mail in: ", background="yellow")
email_label.grid(row=3, column=0)

email_entry = tkinter.Entry(RegistermenuFrame)
email_entry.grid(row=3, column=1)

knopregistreer = tkinter.Button(master=RegistermenuFrame, text="Registreer")
knopregistreer.grid(row=4, column=1)

knopterugRegistreren = tkinter.Button(master=RegistermenuFrame, text="Terug", command=toonHoofdFrame)
knopterugRegistreren.grid(row=4, column=0)

#Stallen
stallenmenuFrame = tkinter.Frame(root)
stallenmenuFrame.configure(background="yellow")
stallenmenuFrame.pack()

knopterugStallen = tkinter.Button(master=stallenmenuFrame, text="Terug", command=toonHoofdFrame)
knopterugStallen.pack()
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

persoonlijkeInformatieKnop = tkinter.Button(master=informatiemenuFrame, text="Persoonlijke informatie")
persoonlijkeInformatieKnop.grid(row=0, column=1)

knopterugInformatieOpvragen = tkinter.Button(master=informatiemenuFrame, text="Terug", command=toonHoofdFrame)
knopterugInformatieOpvragen.grid(row=1, column=1)

#informatie opvragen/algemene informatie
algemeneInformatiemenuFrame = tkinter.Frame(root)
algemeneInformatiemenuFrame.configure(background="yellow")
algemeneInformatiemenuFrame.pack()

aantalplekken = tkinter.Label(master=algemeneInformatiemenuFrame, text="Er zijn nog x plekken vrij", background="yellow")
aantalplekken.pack()

knopterugAlgemenInformatie = tkinter.Button(master=algemeneInformatiemenuFrame, text="Terug", command=toonInformatieFrame)
knopterugAlgemenInformatie.pack()

#informatie opvragen/persoonlijke informatie


toonHoofdFrame()

root.mainloop()