import sqlite3
import json
import os
with open("config.json") as config:
    dataConfig = json.loads(config.read())

dbPath = dataConfig['dbPath']

def getDbAllDataFrom(tablename,value="*"):
	try:
		conn = sqlite3.connect(dbPath)
		c = conn.cursor()
		s = 'SELECT ? FROM ? ;'
		tab = [value,tablename]
		return c.execute(s,[value,tablename]).fetchall()
	except sqlite3.Error as e:
		print (e.args[0])

 #def getDbSpeDataFrom(tablename,value="*",):
