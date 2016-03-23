from bottle import run,route
import json
import sqlite3

dbPath = "../DB/data.db"

@route('/installation/:localisation/:cp', method='GET')
def installation(localisation,cp):
	print(localisation+" "+cp)
	conn = sqlite3.connect(dbPath)
	c = conn.cursor()
	res = c.execute('SELECT * FROM installations WHERE ComLib=\"'+localisation+'\" AND InsCodePostal="'+cp+'";').fetchall()
	print(res)
	return json.dumps(res)


def main():
	run(host='localhost', port=8080)

# Execution de la fonction main au lancement du script
if __name__ == '__main__':
    main()