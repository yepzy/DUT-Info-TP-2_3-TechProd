import sqlite3
import csv
import json

# Récupérer les fichiers activité.csv, equipement.csv et installation.json
# et les mettres dans la base de données


def readCSV():
    # with open('CSV/activités.csv') as csvfile:
    # 	reader = csv.DictReader(csvfile)
    # 	cpt = 0
    # 	for row in reader:
    # 		cpt = cpt + 1
    # 		print(str(cpt)+" | "+row['EquipementId']+" "+row['ActLib'])
    # 		writeTableActivites(row['EquipementId'],row['ActLib'])
    with open('CSV/equipements.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        cpt = 0
        for row in reader:
            cpt = cpt + 1
            print(str(cpt) + " | " + row['EquipementId'] + " " + row['EquNom'])
            writeTableEquipements(row['EquipementId'], row['EquNom'])


def readJSON():
    with open('JSON/installations.json') as data_file:
        data = json.load(data_file)
        for row in data:
            print(row)


def createTableIntallations():
    conn = sqlite3.connect('DB/data.db')
    c = conn.cursor()
    if not c.execute('SELECT * FROM Installations'):
        c.execute('CREATE TABLE Installations (numero INTEGER,nom TEXT,adresse TEXT,code_postal INTEGER,ville TEXT,latitude REAL,longitude REAL)')
    # Sauvegarder les modifications
    conn.commit()
    # Fermer le curseur
    c.close()


def writeTableInstallations(numero, nom, adresse, code_postal, ville, latitude, longitude):
    conn = sqlite3.connect('DB/data.db')
    c = conn.cursor()
    try:
        c.execute('SELECT * FROM installations;')
    except sqlite3.Error as e:
        print(e.args[0])
        createTableIntallations()
    c.execute("INSERT INTO Installations VALUES (?,\"?\",\"?\",?,\"?\",?,?);",
              numero, nom, adresse, code_postal, ville, latitude, longitude)
    # Sauvegarder les modifications
    conn.commit()
    # Fermer le curseur
    c.close()


def createTableActivites():
    conn = sqlite3.connect('DB/data.db')
    c = conn.cursor()
    c.execute('CREATE TABLE Activites (numero INTEGER,nom TEXT);')
    # Sauvegarder les modifications
    conn.commit()
    # Fermer le curseur
    c.close()


def writeTableActivites(numero, nom):
    conn = sqlite3.connect('DB/data.db')
    c = conn.cursor()
    try:
        c.execute('SELECT * FROM Activites;')
    except sqlite3.Error as e:
        createTableActivites()
    c.execute('INSERT INTO Activites VALUES (' + numero + ',\"' + nom + '\");')
    # Sauvegarder les modifications
    conn.commit()
    # Fermer le curseur
    c.close()


def createTableEquipements(	):
    conn = sqlite3.connect('DB/data.db')
    c = conn.cursor()
    c.execute('CREATE TABLE Equipements (numero INTEGER,nom TEXT);')
    # Sauvegarder les modifications
    conn.commit()
    # Fermer le curseur
    c.close()


def writeTableEquipements(numero, nom):
    conn = sqlite3.connect('DB/data.db')
    c = conn.cursor()
    try:
        c.execute('SELECT * FROM Equipements;')
    except sqlite3.Error as e:
        createTableEquipements()
    c.execute('INSERT INTO Equipements VALUES (' + numero + ',\"' + nom + '\");')
    # Sauvegarder les modifications
    conn.commit()
    # Fermer le curseur
    c.close()


readCSV()
