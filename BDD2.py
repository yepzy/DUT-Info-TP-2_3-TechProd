import sqlite3
import csv
import json

# Récupérer les fichiers activité.csv, equipement.csv et installation.json
# et les mettres dans la base de données


def readCSV(filepath, tablename, columns):
    # with open('CSV/activités.csv') as csvfile:
    # 	reader = csv.DictReader(csvfile)
    # 	cpt = 0
    # 	for row in reader:
    # 		cpt = cpt + 1
    # 		print(str(cpt)+" | "+row['EquipementId']+" "+row['ActLib'])
    # 		writeTableActivites(row['EquipementId'],row['ActLib'])
    with open(filepath) as csvfile:
        reader = csv.DictReader(csvfile)
        cpt = 0
        allvalues = []
        for row in reader:
            values = []
            cpt = cpt + 1
            for column in columns:
                values.append('\''+row[column]+'\'')
            allvalues.append(values)
            #print(str(cpt) + str(values))
        writeTable(tablename, allvalues)

def readJSON(filepath):
    with open(filepath) as data_file:
        data = json.load(data_file)
        for row in data:
            print(row)

def createTable(tablename, attributes):
    conn = sqlite3.connect('DB/data.db')
    c = conn.cursor()
    if not c.execute('SELECT * FROM '+tablename):
        c.execute('CREATE TABLE '+tablename+' ('+attributes+')')
    # Sauvegarder les modifications
    conn.commit()
    # Fermer le curseur
    c.close()

def writeTable(tablename, values):
    conn = sqlite3.connect('DB/data.db')
    c = conn.cursor()
    try:
        c.execute('SELECT * FROM '+tablename)
    except sqlite3.Error as e:
        print (e.args[0])
    string = "?"
    for _ in range(1, len(values[0])):
        string += ',?'
    str2 = 'INSERT INTO '+tablename+' VALUES ('+string+')'
    print(str2)
    c.executemany(str2, values)
    # Sauvegarder les modifications
    conn.commit()
    # Fermer le curseur
    c.close()

readCSV("CSV/equipements.csv", "equipements", {'EquipementId', 'EquNom'})
