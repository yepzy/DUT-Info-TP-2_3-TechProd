import sqlite3
import csv
import json
#import Test
# Récupérer les fichiers activité.csv, equipement.csv et installation.json
# et les mettres dans la base de données


def importData(dbfilepath):
	""" lance les fonctions vouluent """
	# Création des Tables
	createTable(dbfilepath, "installations", ["id NUMBER PRIMARY KEY", "InsLieuDit TEXT",  "Latitude REAL", "Longitude REAL", "geo TEXT", "InsNumeroInstall NUMBER",  "InsCodePostal NUMBER", "ComLib TEXT", "InsLibelleVoie TEXT"])
	createTable(dbfilepath, "activites", ["id NUMBER PRIMARY KEY", "EquipementId NUMBER", "ActCode NUMBER", "ActLib TEXT", "EquActivitePraticable NUMBER", "EquActivitePratique NUMBER", "EquActiviteSalleSpe NUMBER"])
	createTable(dbfilepath, "equipements", ["id NUMBER PRIMARY KEY", "InsNumeroInstall NUMBER", "EquipementId NUMBER", "EquNom TEXT", "EquNomBatiment TEXT", "EquipementTypeLib TEXT", "EquipementFiche TEXT", "FamilleFicheLib TEXT", "EquGpsX REAL", "EquGpsY REAL", "EquDateMaj TEXT"])

	# Lecture des CSV et du JSON, puis ecriture dans la DB
	readJSON(dbfilepath, "JSON/installations.json", "installations", ["InsLieuDit",  "Latitude", "Longitude",  "geo", "InsNumeroInstall",  "InsCodePostal", "ComLib",  "InsLibelleVoie"])
	readCSV(dbfilepath, 'CSV/equipements.csv', "equipements", ["InsNumeroInstall", "EquipementId", "EquNom", "EquNomBatiment", "EquipementTypeLib", "EquipementFiche", "FamilleFicheLib", "EquGpsX", "EquGpsY", "EquDateMaj"])
	readCSV(dbfilepath, 'CSV/activités.csv', 'activites', ["EquipementId", "ActCode", "ActLib", "EquActivitePraticable", "EquActivitePratique", "EquActiviteSalleSpe"])


def readCSV(dbfilepath, filepath, tablename, columns):
	""" Lecture des données d'un fichier CSV et demande à les écrires dans la DB """
	with open(filepath) as csvfile:
		reader = csv.DictReader(csvfile)
		cpt = 0
		allvalues = []
		for row in reader:
			values = [cpt]
			cpt = cpt + 1
			for column in columns:
				values.append(row[column])
			allvalues.append(values)
		writeTable(dbfilepath, tablename, allvalues)


def readJSON(dbfilepath, filepath, tablename, columns):
	""" Lecture des données d'un fichier JSON et demande à les écrires dans la DB """
	with open(filepath) as data_file:
		data = json.loads(data_file.read())
		data = data["data"]
		cpt = 0
		allvalues = []
		for row in data:
			values = [cpt]
			cpt = cpt + 1
			for column in columns:
				if column == 'geo':
					this = row[column]
					row[column] = this['name']
				if(isinstance(convertOuiNonBool(row[column]), str)):
					values.append(row[column])
				else:
					values.append(convertOuiNonBool(row[column]))
			allvalues.append(values)
		writeTable(dbfilepath, tablename, allvalues)


def createTable(filepath, tablename, attributes):
	""" Création de la table si elle n'existe pas et supprime les données si elle existait dans la DB"""
	conn = sqlite3.connect(filepath)
	c = conn.cursor()
	s = 'CREATE TABLE ' + tablename + \
		' (' + ','.join([str(x) for x in attributes]) + ');'
	try:
		c.execute('DROP TABLE ' + tablename + ';')
		c.execute(s)
	except sqlite3.Error as e:
		c.execute(s)
	# Sauvegarder les modifications
	print(s)
	conn.commit()
	# Fermer le curseur
	c.close()


def writeTable(filepath, tablename, values):
	""" Ecris les données en argument dans la table en argument sur la DB en argument """
	try:
		conn = sqlite3.connect(filepath)
		c = conn.cursor()
		c.execute('SELECT * FROM ' + tablename + ';')
		string = "?"
		for _ in range(1, len(values[0])):
			string += ',?'
			str2 = 'INSERT INTO ' + tablename + ' VALUES (' + string + ');'
		# print(str2)
		c.executemany(str2, values)
		# Sauvegarder les modifications
		conn.commit()
	except sqlite3.Error as e:
		print (e.args[0])
	# Fermer le curseur
	c.close()


def convertOuiNonBool(data):
	""" convertit les Oui et Non respectivement en booléen True False  """
	if(data == "Oui"):
		return True
	if(data == "Non"):
		return False
	return data
