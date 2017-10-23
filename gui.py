import tkinter

root = tkinter.Tk()
#nslogo = tkinter.PhotoImage(file="C:\\Users\\Arman.K\\PycharmProjects\\FietsenstallingProject\\NSLogo.png", width=40, height=40)

root.title("NS-Fietsenstalling")

#achtergrond_label = tkinter.Label(master=root, image=nslogo)
#achtergrond_label.pack()

registrerenknop = tkinter.Button(master=root, text="Fiets registreren")
registrerenknop.pack()



ophalenKnop = tkinter.Button(master=root, text="Fiets ophalen")
ophalenKnop.pack()

stallenKnop = tkinter.Button(master=root, text="Fiets stallen")
stallenKnop.pack()

informatieOpvragenKnop = tkinter.Button(master=root, text="Informatie opvragen")
informatieOpvragenKnop.pack()

root.mainloop()