import tkinter

def toonHoofdFrame():
    treinTijdenFrame.pack_forget()


def toonInformatieFrame():
    treinTijdenFrame.pack_forget()


def toonAlgemeneInformatieFrame():
    algemeneInformatiemenuFrame.pack(padx=10, pady=10)


def toonPersoonlijkeInformatieFrame():
    hoofdmenuFrame.pack_forget()
    informatiemenuFrame.pack_forget()
    persoonlijkeInformatieFrame.pack(padx=10, pady=10)


def toonTreinTijdenFrame():
    informatiemenuFrame.pack_forget()
    treinTijdenFrame.pack(padx=10, pady=10)

#Informatie opvragen
treinTijdenKnop = tkinter.Button(master=treinTijdenFrame, text="Trein tijden", width=25)
treinTijdenKnop.grid(row=3, column=0, pady=5)



#Informatie opvragen/trein tijden
treinTijdenFrame = tkinter.Frame(root)
treinTijdenFrame.configure(background="yellow")
treinTijdenFrame.pack()

treinTijden_label = tkinter.Label(master=treinTijdenFrame, text="Vul hier je huidige station in: ",background="yellow")
treinTijden_label.grid(row=0, column=0)

treinTijden_entry = tkinter.Entry(master=treinTijdenFrame)
treinTijden_entry.grid(row=0, column=1)

