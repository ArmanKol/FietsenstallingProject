import tkinter
import sys
import os

def toonHoofdFrame():
    RegistermenuFrame.pack_forget()
    hoofdmenuFrame.pack()

def toonRegisterFrame():
    hoofdmenuFrame.pack_forget()
    RegistermenuFrame.pack()

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

ophalenKnop = tkinter.Button(master=hoofdmenuFrame, text="Fiets ophalen", width=25)
ophalenKnop.grid(row=2, column=0)

stallenKnop = tkinter.Button(master=hoofdmenuFrame, text="Fiets stallen", width=25)
stallenKnop.grid(row=3, column=0)

informatieOpvragenKnop = tkinter.Button(master=hoofdmenuFrame, text="Informatie opvragen", width=25)
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

knopterug = tkinter.Button(master=RegistermenuFrame, text="Terug", command=toonHoofdFrame)
knopterug.grid(row=4, column=0)


toonHoofdFrame()

root.mainloop()