import sqlite3
import csv
import json

# Récupérer les fichiers activité.csv, equipement.csv et installation.json
# et les mettres dans la base de données


def readCSV(filepath, tablename, columns):
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
        writeTable(filepath, tablename, allvalues)

def readJSON(filepath, tablename, columns):
    with open(filepath, encoding="utf-8") as data_file:
        data = json.loads(data_file.read())
        cpt = 0
        allvalues = []
        for row in data:
            values = []
            cpt = cpt + 1
            for column in columns:
                if(isinstance(convertOuiNonBool(row[column]), str)):
                    values.append('\''+row[column]+'\'')
                else:
                    values.append(convertOuiNonBool(row[column]))
            allvalues.append(values)
        writeTable(filepath, tablename, allvalues)

def createTable(filepath, tablename, attributes):
    conn = sqlite3.connect(filepath)
    c = conn.cursor()
    if not c.execute('SELECT * FROM '+tablename):
        c.execute('CREATE TABLE '+tablename+' ('+attributes+')')
    # Sauvegarder les modifications
    conn.commit()
    # Fermer le curseur
    c.close()

def writeTable(filepath, tablename, values):
    conn = sqlite3.connect(filepath)
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

def convertOuiNonBool(data):
    if(data == "Oui"):
        return True
    if(data == "Non"):
        return False
    return data

#readCSV("CSV/equipements.csv", "equipements", {'EquipementId', 'EquNom'})
readJSON("JSON/installations.json", "installations", {'EquipementId', 'EquActiviteSalleSpe', 'EquActivitePratique', 'EquActivitePraticable', 'ComLib', 'ActCode', 'ActNivLib', 'ComInsee', 'ActLib', 'EquNbEquIdentique'})
