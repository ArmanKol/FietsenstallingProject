import tkinter
import sys
import os

def hoofdmenu():
    raster = tkinter.Frame(root, height=400, width=200)
    raster.configure(background="yellow")
    raster.pack()
    return raster

def registreren():
    raster1 = tkinter.Frame(root, height=400, width=200)
    raster1.configure(background="yellow")
    raster1.pack()
    raster.destroy()

    naam_label= tkinter.Label(master=raster1, text="Voer hier je naam in: ", background="yellow")
    naam_label.grid(row=0, column=0)

    naam_entry=tkinter.Entry(raster1)
    naam_entry.grid(row=0, column=1)

    wachtwoord_label= tkinter.Label(master=raster1, text="Voer hier je wachtwoord in: ", background="yellow")
    wachtwoord_label.grid(row=1, column=0)

    wachtwoord_entry= tkinter.Entry(raster1)
    wachtwoord_entry.grid(row=1, column=1)

    telefoonnummer_label= tkinter.Label(master=raster1, text="Voer hier je telefoonnummer in: ", background="yellow")
    telefoonnummer_label.grid(row=2, column=0)

    telefoonnummer_entry= tkinter.Entry(raster1)
    telefoonnummer_entry.grid(row=2, column=1)

    email_label= tkinter.Label(master=raster1, text="Voer hier je e-mail in: ", background="yellow")
    email_label.grid(row=3, column=0)

    email_entry= tkinter.Entry(raster1)
    email_entry.grid(row=3, column=1)

    knopregistreer= tkinter.Button(master=raster1, text="Registreer")
    knopregistreer.grid(row=4, column=1)

    knopterug= tkinter.Button(master=raster1, text="Terug", command=hoofdmenu)
    knopterug.grid(row=4, column=0)


root = tkinter.Tk()
root.title("NS-Fietsenstalling")
root.resizable(False, False)
root.configure(background="yellow")

raster = tkinter.Frame(root, height=100,width=100)
raster.configure(background="yellow")
raster.pack()

#nslogo = tkinter.PhotoImage(file="C:\\Users\\Arman.K\\PycharmProjects\\FietsenstallingProject\\NSLogo.png")

#achtergrond_label = tkinter.Label(master=raster, image=nslogo)
#achtergrond_label.grid(row=0, column=0)

titel_label = tkinter.Label(master=raster,text="NS-Fietsstalling", background="yellow")
titel_label.grid(row=0, column=0)

registrerenknop = tkinter.Button(master=raster, text="Fiets registreren", width=25, command=registreren)
registrerenknop.grid(row=1,column=0)

ophalenKnop = tkinter.Button(master=raster, text="Fiets ophalen", width=25)
ophalenKnop.grid(row=2,column=0)

stallenKnop = tkinter.Button(master=raster, text="Fiets stallen", width=25)
stallenKnop.grid(row=3,column=0)

informatieOpvragenKnop = tkinter.Button(master=raster, text="Informatie opvragen", width=25)
informatieOpvragenKnop.grid(row=4,column=0)

root.mainloop()