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
            values = [cpt]
            cpt = cpt + 1
            for column in columns:
                values.append('\''+row[column]+'\'')
            allvalues.append(values)
            #print(str(cpt) + str(values))
        writeTable("BD/data.db", tablename, allvalues)

def readJSON(filepath, tablename, columns):
    with open(filepath, encoding="utf-8") as data_file:
        data = json.loads(data_file.read())
        data = data["data"]
        cpt = 0
        allvalues = []
        for row in data:
            values = [cpt]
            cpt = cpt + 1
            for column in columns:
                if(isinstance(convertOuiNonBool(row[column]), str)):
                    values.append('\''+row[column]+'\'')
                else:
                    values.append(convertOuiNonBool(row[column]))
            allvalues.append(values)
        writeTable("DB/data.db", tablename, allvalues)

def createTable(filepath, tablename, attributes):
    conn = sqlite3.connect(filepath)
    c = conn.cursor()
    s = 'CREATE TABLE '+tablename+' ('+','.join([str(x) for x in attributes])+');'
    try:
        c.execute('DROP TABLE '+tablename+';')
        c.execute(s)
    except sqlite3.Error as e:
        c.execute(s)
    # Sauvegarder les modifications
    print(s)
    conn.commit()
    # Fermer le curseur
    c.close()

def writeTable(filepath, tablename, values):
    conn = sqlite3.connect(filepath)
    c = conn.cursor()
    try:
        c.execute('SELECT * FROM '+tablename+';')
    except sqlite3.Error as e:
        print (e.args[0])
    string = "?"
    for _ in range(1, len(values[0])):
        string += ',?'
    str2 = 'INSERT INTO '+tablename+' VALUES ('+string+');'
    print(str2)
    c.executemany(str2, values)
    # Sauvegarder les modifications
    conn.commit()
    # Fermer le curseur
    c.close()

#readCSV("CSV/equipements.csv", "equipements", {'EquipementId', 'EquNom'})
createTable("DB/data.db", "installations",
    {
		"InsLieuDit TEXT",
		"Latitude REAL",
        "Longitude REAL",
		"geo BLOB",
		"InsNumeroInstall NUMBER",
		"InsCodePostal NUMBER",
		"ComLib TEXT",
		"InsLibelleVoie TEXT"		
    })

createTable("DB/data.db","activites",
    {
    "ComInsee NUMBER",
    "ComLib TEXT",
    "EquipementId NUMBER",
    "EquNbEquIdentique NUMBER",
    "ActCode NUMBER",
    "ActLib TEXT",
    "EquActivitePraticable NUMBER",
    "EquActivitePratique NUMBER",
    "EquActiviteSalleSpe NUMBER",
    "ActNivLib TEXT"
    })

createTable("DB/data.db","equipements",
{
    "InsNumeroInstall NUMBER",
    "EquipementId NUMBER",
    "EquNom TEXT",
    "EquNomBatiment TEXT",
    "EquipementTypeLib TEXT",
    "EquipementFiche TEXT",
    "FamilleFicheLib TEXT",
    "EquGpsX NUMBER",
    "EquGpsY NUMBER",
    "EquDateMa TEXT"
})


readJSON("JSON/installations.json", "installations", {'EquipementId', 'EquActiviteSalleSpe', 'EquActivitePratique', 'EquActivitePraticable', 'ComLib', 'ActCode', 'ActNivLib', 'ComInsee', 'ActLib', 'EquNbEquIdentique'})
readCSV('CSV/equipements.csv')