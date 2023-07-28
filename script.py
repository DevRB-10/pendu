""" import sqlite3

mydb = sqlite3.connect('bdd.sqlite')

cursor = mydb.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS mots(id INTEGER PRIMARY KEY, mot TEXT, theme INT)')
# theme 1: developpeur
cursor.execute('INSERT INTO mots(mot, theme) VALUES("logiciel", "Developpeur"), ("application", "Developpeur"), ' 
               '("algorithme", "Developpeur"),("balise", "Developpeur"), ("cookie", "Developpeur"), '
               '("lien", "Developpeur"), ("linux", "Developpeur"), ("login", "Developpeur"), ("redirection", "Developpeur"), '
               '("referencement", "Developpeur"), ("requete", "Developpeur"), ("refonte", "Developpeur"), '
               '("serveur", "Developpeur"), ("github", "Developpeur")')
# theme 2: designer
cursor.execute('INSERT INTO mots(mot, theme) VALUES("maquette", "Designer"), ("affordance", "Designer"), '
               '("arborescence", "Designer"), ("detourage", "Designer"), ("ergonomie", "Designer"), '
               '("template", "Designer"), ("interface", "Designer"), ("prototype", "Designer"), '
               '("typographie", "Designer"), ("wireframe", "Designer"), ("zoning", "Designer"), ("couleur", "Designer")')

#statement = cursor.execute('SELECT * FROM mots')
#print(statement.fetchall())

# 14 mots dans developpeur
# 12 mots dans designer
mydb.commit()
cursor.close()
mydb.close() """

import sqlite3

mydb = sqlite3.connect('bdd.sqlite')

cursor = mydb.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS mots(id INTEGER PRIMARY KEY, mot TEXT, theme INT)')
# theme 1: developpeur
cursor.execute('INSERT INTO mots(mot, theme) VALUES("logiciel", "Developpeur"), ("application", "Developpeur"), ' 
               '("algorithme", "Developpeur"),("balise", "Developpeur"), ("cookie", "Developpeur"), '
               '("lien", "Developpeur"), ("linux", "Developpeur"), ("login", "Developpeur"), ("redirection", "Developpeur"), '
               '("referencement", "Developpeur"), ("requete", "Developpeur"), ("refonte", "Developpeur"), '
               '("serveur", "Developpeur"), ("github", "Developpeur")')
# theme 2: designer
cursor.execute('INSERT INTO mots(mot, theme) VALUES("maquette", "Designer"), ("affordance", "Designer"), '
               '("arborescence", "Designer"), ("detourage", "Designer"), ("ergonomie", "Designer"), '
               '("template", "Designer"), ("interface", "Designer"), ("prototype", "Designer"), '
               '("typographie", "Designer"), ("wireframe", "Designer"), ("zoning", "Designer")')

#statement = cursor.execute('SELECT * FROM mots')
#print(statement.fetchall())

mydb.commit()
cursor.close()
mydb.close()