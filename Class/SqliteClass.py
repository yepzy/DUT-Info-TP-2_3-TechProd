import sqlite3
import json
import os

class SqliteConn:

    db = ''
    conn = ''

    # the constructor
    def __init__(filepath="*"):
        if filepath=="*":
            with open("config.json") as config:
            dataConfig = json.loads(config.read())

            db = dataConfig['dbPath']
        else :
            db = filepath
        try:
    		conn = sqlite3.connect(db)
        except sqlite3.Error as e:
    		print (e.args[0])

    def query(_from, _select="*", _where="1==1"):
        try:
            c = conn.cursor()
            req = 'SELECT ? FROM ? WHERE ?'
            args = [_select, _from, _where]
            return c.execute(req, args).fetchAll();
        except sqlite3.Error as e:
    		print (e.args[0])

    def insert(_in, _values):
        try:
            c = conn.cursor()
            req = 'INSERT INTO ? VALUES ?'
            args = [_in, _values]
            return c.execute(req, args).fetchAll();
        except sqlite3.Error as e:
    		print (e.args[0])


    #def getDbSpeDataFrom(tablename,value="*",):
