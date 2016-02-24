import json
import sqlite3


def readJSON(jsonFile, dbFile, className, argDB, typesDB):
    with open('JSON/' + jsonFile, encoding='utf-8') as data_file:
        fileJson = json.loads(data_file.read())
        data = fileJson['data']
        for row in data:
            row['EquActiviteSalleSpe'] = convertOuiNonBool(
                row['EquActiviteSalleSpe'])
            row['EquActivitePratique'] = convertOuiNonBool(
                row['EquActivitePratique'])
            row['EquActivitePraticable'] = convertOuiNonBool(
                row['EquActivitePraticable'])
            writeJSON(dbFile, className, argDB, typesDB,
                      [row['EquipementId'], row["EquActiviteSalleSpe"], row["EquActivitePratique"], row["EquActivitePraticable"], row["ComLib"], row["ActCode"], row["ActNivLib"], row["ComInsee"], row["ActLib"], row["EquNbEquIdentique"]])


def writeJSON(dbFile, className, argDB, typesDB, valuesDB):
    conn = sqlite3.connect('DB/' + dbFile)
    c = conn.cursor()
    try:
        c.execute('SELECT * FROM ' + className + ';')
    except Exception as e:
        createTable(dbFile, className, argDB, typesDB)
    print(','.join([str(x) for x in valuesDB]))
    c.execute('INSERT INTO ' + className + ' VALUES (' +
              ','.join([str(x) for x in valuesDB]) + ');')


def createTable(dbFile, className, argDB, typesDB):
    conn = sqlite3.connect('DB/' + dbFile)
    c = conn.cursor()
    i = 0
    tabArgs = []
    for arguments in argDB:
        tabArgs.append(str(arguments + " " + typesDB[i]))
        ++i
    c.execute('CREATE TABLE ' + className +
              ' (' + ','.join([str(x) for x in tabArgs]) + ');')
    c.close()


def convertOuiNonBool(data):
    if(data == "Oui"):
        return True
    else:
        return False


readJSON('installations.json', 'data.db', 'Installation', ['EquipementId', "EquActiviteSalleSpe", "EquActivitePratique", "EquActivitePraticable", "ComLib",
                                                           "ActCode", "ActNivLib", "ComInsee", "ActLib", "EquNbEquIdentique"], ['NUMBER', 'NUMBER', 'NUMBER', 'NUMBER', 'TEXT', 'NUMBER', 'TEXT', 'NUMBER', 'TEXT', 'NUMBER'])
