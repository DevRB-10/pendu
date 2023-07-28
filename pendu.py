class App(object):
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title(' Jeu du Pendu ')
        self.root.iconbitmap('potence.ico')
        
        self.base = ("line", 30, 190, 170, 190)
        self.mas = ("line", 70, 190, 70, 10)
        self.haut = ("line", 170, 10, 70, 10)
        self.angle = ("line", 100, 10, 70, 50)
        self.petit_bout = ("line", 170, 10, 170, 40)
        self.tete = ("oval", 155, 40, 185, 70)
        self.corps = ("line", 170, 140, 170, 70)
        self.bras = ("line", 190, 80, 150, 80)
        self.j_gauche = ("line", 170, 140, 150, 160)
        self.j_droite = ("line", 170, 140, 190, 160)
        self.trait = [self.base, self.mas, self.haut, self.angle, 
                      self.petit_bout, self.tete, self.corps, self.bras, 
                      self.j_gauche, self.j_droite]

        self.conf()
        self.new_party()
        self.root.mainloop()

    def conf(self):
        fileObject = open("conf.json", "r")
        jsonContent = fileObject.read()
        obj_python = json.loads(jsonContent)

        self.bg_canevas = obj_python['canevas']

        self.active_letters = obj_python['letters']['active']
        self.used_letters = obj_python['letters']['used']
        self.border_letters = obj_python['letters']['border']

        self.color_line = obj_python['line']['color']
        self.width_line = obj_python['line']['width']
        self.theme = obj_python['theme']

    def new_party(self):
        self.conf()
        self.caneva()
        self.menu()
        self.alphabet()
        self.sql()
        self.mot()
        self.avancement_mot = []
        self.cpt = 0

    def caneva(self):
        self.canevas = Canvas(self.root, width=200, height=200, background=self.bg_canevas)
        self.canevas.grid(row=1, column=1, rowspan=6)

    def menu(self):
        fichier_xml = "menus.xml"
        #fichier_xml = "menus_sauv.xml"
        tree = ET.parse(fichier_xml)
        myroot = tree.getroot()
        menubar = Menu(self.root)

        nb_menu = 0
        for menu in myroot.findall('menu'):
            nb_menu += 1
            truc_menu = Menu(menubar, tearoff=0)
            nb_lien = 0
            for lien in menu.findall('lien'):
                nb_lien += 1
                nb_sous_menu = 0
                for sous_menu in lien.findall('menu'):
                    nb_sous_menu += 1
                    truc_sous_menu = Menu(truc_menu, tearoff=0)
                    nb_sous_lien = 0
                    for sous_lien in sous_menu.findall('lien'):
                        nb_sous_lien += 1
                        #print(str(nb_sous_menu) + menu.attrib['categorie'].capitalize(), " -> ", 
                        # sous_menu.attrib['categorie'].capitalize(), " -> ", str(nb_sous_lien) + 
                        # sous_lien.find('label').text + ": " + sous_lien.find('command').text)
                        self.sous_label = sous_lien.find('label').text
                        sous_command = sous_lien.find('command').text

                        truc_sous_menu.add_command(label=self.sous_label, command= lambda: self.niveau(self.sous_label))

                        """ if nb_sous_menu == 1 and nb_sous_lien == 1:
                            truc_sous_menu.add_command(label=self.sous_label, command= lambda: self.niveau("Developpeur"))
                        if nb_sous_menu == 1 and nb_sous_lien == 2:
                            truc_sous_menu.add_command(label=self.sous_label, command= lambda: self.niveau("Designer")) """

                        #truc_sous_menu.add_command(label=self.sous_label, command=sous_command)
                    sous_label_up = sous_menu.attrib['categorie'].capitalize()
                    truc_menu.add_cascade(label=sous_label_up, menu=truc_sous_menu)
                if nb_sous_menu == 0:
                    #print(str(nb_menu) + menu.attrib['categorie'].capitalize(), " -> ", 
                    # str(nb_lien) + lien.find('label').text + ": " + lien.find('command').text)
                    self.label = lien.find('label').text
                    command = lien.find('command').text

                    if nb_menu == 1 and nb_lien == 1:
                        truc_menu.add_command(label=self.label, command=self.new_party)
                    if nb_menu == 1 and nb_lien == 3:
                        truc_menu.add_command(label=self.label, command=self.apparence)
                    if nb_menu == 1 and nb_lien == 4:
                        truc_menu.add_command(label=self.label, command=self.root.destroy)
                    if nb_menu == 2 and nb_lien == 1:
                        truc_menu.add_command(label=self.label, command=self.edit_mot)
                    if nb_menu == 2 and nb_lien == 2:
                        truc_menu.add_command(label=self.label, command=self.edit_niveau)
                    if nb_menu == 3 and nb_lien == 1:
                        truc_menu.add_command(label=self.label, command=self.propos)

                    #truc_menu.add_command(label=self.label, command=command)
            label_up = menu.attrib['categorie'].capitalize()
            menubar.add_cascade(label=label_up, menu=truc_menu)
        self.root.config(menu=menubar)

    def alphabet(self):
        self.l_Z = Button(self.root, text="Z", width=3, height=1, command=lambda: self.lettre("Z", 4, 6)).\
            grid(row = 4, column=6)
        self.l_Y = Button(self.root, text="Y", width=3, height=1, command=lambda: self.lettre("Y", 4, 5)).\
            grid(row = 4, column=5)
        self.l_X = Button(self.root, text="X", width=3, height=1, command=lambda: self.lettre("X", 4, 4)).\
            grid(row = 4, column=4)
        self.l_W = Button(self.root, text="W", width=3, height=1, command=lambda: self.lettre("W", 4, 3)).\
            grid(row = 4, column=3)
        self.l_V= Button(self.root, text="V", width=3, height=1, command=lambda: self.lettre("V", 4, 2)).\
            grid(row = 4, column=2)

        self.l_U = Button(self.root, text="U", width=3, height=1, command=lambda: self.lettre("U", 3, 8)).\
            grid(row = 3, column=8)
        self.l_T = Button(self.root, text="T", width=3, height=1, command=lambda: self.lettre("T", 3, 7)).\
            grid(row = 3, column=7)
        self.l_S = Button(self.root, text="S", width=3, height=1, command=lambda: self.lettre("S", 3, 6)).\
            grid(row = 3, column=6)
        self.l_R = Button(self.root, text="R", width=3, height=1, command=lambda: self.lettre("R", 3, 5)).\
            grid(row = 3, column=5)
        self.l_Q = Button(self.root, text="Q", width=3, height=1, command=lambda: self.lettre("Q", 3, 4)).\
            grid(row = 3, column=4)
        self.l_P = Button(self.root, text="P", width=3, height=1, command=lambda: self.lettre("P", 3, 3)).\
            grid(row = 3, column=3)
        self.l_O = Button(self.root, text="O", width=3, height=1, command=lambda: self.lettre("O", 3, 2)).\
            grid(row = 3, column=2)

        self.l_N = Button(self.root, text="N", width=3, height=1, command=lambda: self.lettre("N", 2, 8)).\
            grid(row = 2, column=8)
        self.l_M = Button(self.root, text="M", width=3, height=1, command=lambda: self.lettre("M", 2, 7)).\
            grid(row = 2, column=7)
        self.l_L = Button(self.root, text="L", width=3, height=1, command=lambda: self.lettre("L", 2, 6)).\
            grid(row = 2, column=6)
        self.l_K = Button(self.root, text="K", width=3, height=1, command=lambda: self.lettre("K", 2, 5)).\
            grid(row = 2, column=5)
        self.l_J = Button(self.root, text="J", width=3, height=1, command=lambda: self.lettre("J", 2, 4)).\
            grid(row = 2, column=4)
        self.l_I = Button(self.root, text="I", width=3, height=1, command=lambda: self.lettre("I", 2, 3)).\
            grid(row = 2, column=3)
        self.l_H = Button(self.root, text="H", width=3, height=1, command=lambda: self.lettre("H", 2, 2)).\
            grid(row = 2, column=2)

        self.l_G = Button(self.root, text="G", width=3, height=1, command=lambda: self.lettre("G", 1, 8)).\
            grid(row = 1, column=8, padx=3)
        self.l_F = Button(self.root, text="F", width=3, height=1, command=lambda: self.lettre("F", 1, 7)).\
            grid(row = 1, column=7, padx=3)
        self.l_E = Button(self.root, text="E", width=3, height=1, command=lambda: self.lettre("E", 1, 6)).\
            grid(row = 1, column=6, padx=3)
        self.l_D = Button(self.root, text="D", width=3, height=1, command=lambda: self.lettre("D", 1, 5)).\
            grid(row = 1, column=5, padx=3)
        self.l_C = Button(self.root, text="C", width=3, height=1, command=lambda: self.lettre("C", 1, 4)).\
            grid(row = 1, column=4, padx=3)
        self.l_B = Button(self.root, text="B", width=3, height=1, command=lambda: self.lettre("B", 1, 3)).\
            grid(row = 1, column=3, padx=3)
        self.l_A = Button(self.root, text="A", width=3, height=1, command=lambda: self.lettre("A", 1, 2)).\
            grid(row = 1, column=2, padx=3)
    
    def niveau(self, theme):
        print("Theme choisi: " + theme)
        modif_json = {
            "canevas": "yellow",
            "letters": {
                "active": "write",
                "used": "grey",
                "border": "black"
            },
            "line": {
                "color": "black",
                "width": 2
            },
            "theme": theme
        }
        jsonString = json.dumps(modif_json)
        jsonFile = open("conf.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
        self.new_party()
                
    def sql(self):
        self.mydb = sqlite3.connect('bdd.sqlite')
        self.cursor = self.mydb.cursor()
        self.statement = self.cursor.execute('SELECT * FROM mots WHERE theme="'+  self.theme +'"')

    def mot(self):
        self.find_mot = ''
        self.liste_mot = random.choice(self.statement.fetchall())
        self.find_mot = self.liste_mot[1]
        self.cursor.close()
        self.mydb.close()
        print('Le mot est: ' + self.find_mot)
        mot_tire = ''
        for k in range(0, int((23-len(self.find_mot))/2)):
            mot_tire += ' '
        for l in range(0, len(self.find_mot)):
            mot_tire += '_ '
        for k in range(0, int((23-len(self.find_mot))/2)):
            mot_tire += ' '
        Label(self.root, text=(mot_tire)).grid(row=6, column=4, columnspan=3)
        self.find_mot

    def tracer(self):
        self.cpt += 1
        if self.cpt < 11:
            for t in range(0,10): 
                if self.cpt == 6:
                    self.canevas.create_oval(self.trait[self.cpt-1][1], self.trait[self.cpt-1][2], 
                                        self.trait[self.cpt-1][3], self.trait[self.cpt-1][4], 
                                        fill=self.color_line, width=self.width_line)
                else:
                    self.canevas.create_line(self.trait[self.cpt-1][1], self.trait[self.cpt-1][2], 
                                        self.trait[self.cpt-1][3], self.trait[self.cpt-1][4], 
                                        fill=self.color_line, width=self.width_line)
            #print("erreur: " + str(self.cpt)) 
            if self.cpt == 10:
                print("👎🏼 Perdu!")
                image=Image.open('pouce_blanc_bas.gif')
                img=image.resize((128, 128))
                my_img=ImageTk.PhotoImage(img)
                label=self.canevas.create_image(100, 100, image = my_img)
                label.grid(row=1, column=1, rowspan=6)
   
    mot_valide = 0
    def lettre(self, letter, r, c):
        trace = 0
        self.mot_floute = ''
        for a in range(0, len(self.find_mot)):
            if self.find_mot[a] == letter.lower():
                trace += 1
            if len(self.avancement_mot) >= len(self.find_mot):
                if letter.lower() == self.find_mot[a]:
                    self.avancement_mot[a] = self.find_mot[a]
            else:
                if letter.lower() == self.find_mot[a]:
                    self.avancement_mot.insert(a, self.find_mot[a])
                else:
                    self.avancement_mot.insert(a, "_")
            self.mot_floute += self.avancement_mot[a].upper() + " "
        if trace == 0:
            self.tracer()
        print("motfloute: " + self.mot_floute)
        print(" ")
        Button(self.root, text=letter, width=3, height=1, background="grey", 
               activebackground="grey", relief=RIDGE).\
            grid(row = r, column = c)
        Label(self.root, text=(self.mot_floute)).grid(row=6, column=4, columnspan=3)
        
        ### verif gagnant ###
        gagne = 0
        for d in range(0, len(self.mot_floute)): 
            if  self.find_mot[int(d/2)] == self.mot_floute[d].lower():
                gagne += 1
                if gagne >= len(self.find_mot):
                    print("👍🏼 Gagné!")
                    self.caneva()
                    image=Image.open('pouce_blanc_haut.gif')
                    img=image.resize((128, 128))
                    my_img=ImageTk.PhotoImage(img)
                    label=self.canevas.create_image(100, 100, image = my_img)
                    label.grid(row=1, column=1, rowspan=6)

    def apparence(self):
        import tkinter as tk
        fen = tk.Tk()
        fen.title("Apparence")
        fen.geometry("300x100")
        def getEntry():
            color = myEntry.get()
            modif_json = {
                "canevas": color,
                "letters": {
                    "active": "write",
                    "used": "grey",
                    "border": "black"
                },
                "line": {
                    "color": "black",
                    "width": 2
                },
                "theme": self.theme
            }
            jsonString = json.dumps(modif_json)
            jsonFile = open("conf.json", "w")
            jsonFile.write(jsonString)
            jsonFile.close()
            self.new_party()
            fen.destroy()

        texte1 = tk.Label(fen, text="Modifier la couleur du background")
        texte1.pack()
        myEntry = tk.Entry(fen, width=35, justify=CENTER)
        myEntry.pack(pady=10)
        btn1 = tk.Button(fen, height=1, width=10, text="Valider", command=getEntry)
        btn1.pack(side=LEFT, padx=40)
        btn2 = tk.Button(fen, height=1, width=10, text = "Quitter", command=fen.destroy)
        btn2.pack(side=RIGHT, padx=40)

        fen.mainloop()

    def propos(self):
        a_propos.About()

    def edit_mot(self):
        import tkinter as tk
        from tkinter import ttk
        fenetre = tk.Tk()
        fenetre.title("Ajout de mot")
        fenetre.geometry("300x150")
        def getEntry():
            niveau = listeCombo.get()
            new_mot = myEntry.get()
            mydb = sqlite3.connect('bdd.sqlite')
            cursor = mydb.cursor()
            cursor.execute('INSERT INTO mots(mot, theme) VALUES("' + new_mot + '", "' + niveau + '")')
            print(new_mot + " a été ajouté en " + listeCombo.get() + " dans la BDD")
            mydb.commit()
            cursor.close()
            mydb.close()

        texte1 = tk.Label(fenetre, text="Ajouter un mot")
        texte1.pack()
        myEntry = tk.Entry(fenetre, width=35, justify=CENTER)
        myEntry.pack(pady=10)
        self.mydb = sqlite3.connect('bdd.sqlite')
        self.cursor = self.mydb.cursor()
        self.statement = self.cursor.execute('SELECT DISTINCT theme FROM mots')
        listeProduits=[]
        self.liste_theme = self.statement.fetchall()
        for j in range(0, len(self.liste_theme)):
            theme_brut = str(self.liste_theme[j])
            theme_doux = theme_brut[2:len(self.liste_theme)-5]
            listeProduits += [theme_doux]
        self.cursor.close()
        self.mydb.close()
        listeCombo = ttk.Combobox(fenetre, values=listeProduits)
        listeCombo.pack()
        listeCombo.current(0)
        btn1 = tk.Button(fenetre, height=1, width=10, text="Ajouter", command=getEntry)
        btn1.pack(side=LEFT, padx=40)
        btn2 = tk.Button(fenetre, height=1, width=10, text = "Quitter", command=fenetre.destroy)
        btn2.pack(side=RIGHT, padx=40)

        fenetre.mainloop()

    def edit_niveau(self):
        print("Edition des niveaux")

        """ import tkinter as tk
        from tkinter import ttk
        fenetre = tk.Tk()
        fenetre.title("Ajout de theme")
        fenetre.geometry("300x160")
        def getEntry():
            theme = myEntry.get()
            mot = myEntry2.get() """
        """ mydb = sqlite3.connect('bdd.sqlite')
            cursor = mydb.cursor()
            cursor.execute('INSERT INTO mots(mot, theme) VALUES("' + mot + '", "' + theme + '")')
            print(mot + " a été ajouté en " + theme + " dans la BDD")
            mydb.commit()
            cursor.close()
            mydb.close() """

            #modif xml
            
        """ fichier_xml = "menus.xml"
            tree = ET.parse(fichier_xml)
            myroot = tree.getroot()

            for menu in myroot.findall('menu'):
                for lien in menu.findall('lien'):
                    for sous_menu in lien.findall('menu'):
                        if sous_menu.attrib['categorie'] == "Niveaux":
                            print("menu niveau")
                        nb_souslien = 0
                        for sous_lien in sous_menu.findall('lien'):
                            nb_souslien += 1
                            self.sous_label = sous_lien.find('label').text
                            print(self.sous_label)
                        if sous_menu.attrib['categorie'] == "Niveaux":
                            print(nb_souslien)
                            new_lien = ET.SubElement(lien, 'lien')
                            new_label = ET.SubElement(new_lien, 'label')
                            new_command = ET.SubElement(new_label, 'command')

            self.new_party()

        texte1 = tk.Label(fenetre, text="Ajouter un theme")
        texte1.pack()
        myEntry = tk.Entry(fenetre, width=35, justify=CENTER)
        myEntry.pack(pady=10)

        texte2 = tk.Label(fenetre, text="Ajouter un mot")
        texte2.pack()
        myEntry2 = tk.Entry(fenetre, width=35, justify=CENTER)
        myEntry2.pack(pady=10)
        
        btn1 = tk.Button(fenetre, height=1, width=10, text="Ajouter", command=getEntry)
        btn1.pack(side=LEFT, padx=40)
        btn2 = tk.Button(fenetre, height=1, width=10, text = "Quitter", command=fenetre.destroy)
        btn2.pack(side=RIGHT, padx=40)

        fenetre.mainloop() """


if __name__ == '__main__': 
    from tkinter import *
    import sqlite3 	
    import random
    import json
    import xml.etree.ElementTree as ET
    from PIL import Image, ImageTk

    import a_propos

    f = App()	
