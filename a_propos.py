from tkinter import *

class About(object):
    def __init__(self) -> None:
        print("A propos du pendu... bah il est mort ! ")
        print("Application Sous Licence GPL3")

        self.fenetre = Tk()
        self.fenetre.title("A propos")
        self.fenetre.geometry("250x100")

        texte2 = Label(self.fenetre, text = "Application Sous Licence GPL3")
        texte2.pack(pady=10)
        bouton1 = Button(self.fenetre, text = "Quitter", command=self.fenetre.destroy)
        bouton1.pack(side=BOTTOM, pady=10)

        self.fenetre.mainloop()
