import tkinter

root = tkinter.Tk()
nslogo = tkinter.PhotoImage(file="C:\\Users\\Arman.K\\PycharmProjects\\FietsenstallingProject\\NSLogo.png")

root.title("NS-Fietsenstalling")

achtergrond_label = tkinter.Label(master=root, image=nslogo)
achtergrond_label.pack()

registrerenknop = tkinter.Button(master=root, text="Test")
registrerenknop.pack()

root.mainloop()