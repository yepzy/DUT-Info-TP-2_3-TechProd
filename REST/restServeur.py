from bottle.bottle import run,route,get, post,request,BaseRequest
import json
import sqlite3

dbPath = "../DB/data.db"

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@route('/installations', method='GET')
def installations():
	
	conn = sqlite3.connect(dbPath)
	conn.row_factory = dict_factory
	c = conn.cursor()
	res = c.execute('SELECT * FROM installations WHERE ComLib=\"'+request.query['localisation']+'\" AND InsCodePostal="'+request.query['cp']+'";').fetchall()
	print(res)
	return json.dumps(dict(data=res))

@route('/equipements/:nom/:type/:', method='GET')
def equipements(localisation,cp):
	conn = sqlite3.connect(dbPath)
	conn.row_factory = dict_factory
	c = conn.cursor()
	res = c.execute('SELECT * FROM installations WHERE ComLib=\"'+localisation+'\" AND InsCodePostal="'+cp+'";').fetchall()
	#print(res)
	return json.dumps(dict(data=res))

@route('/activites/:nom/:EqActivitePratiquable/:EqActivitePratique/:EqActiviteSalleSpe', method='GET')
def activites(nom,EqActivitePratiquable,EqActivitePratique,EqActiviteSalleSpe):
	conn = sqlite3.connect(dbPath)
	conn.row_factory = dict_factory
	c = conn.cursor()
	res = c.execute('SELECT * FROM activites WHERE ActLib=\"'+nom+'\" AND EquActivitePraticable=\"'+EqActivitePratiquable+'\" AND EquActivitePratique=\"'+EqActivitePratique+'\" AND EquActiviteSalleSpe=\"'+EqActiviteSalleSpe+'\";').fetchall()
	print(res)
	return json.dumps(dict(data=res))


def main():
	run(host='localhost', port=8080)

# Execution de la fonction main au lancement du script
if __name__ == '__main__':
    main()