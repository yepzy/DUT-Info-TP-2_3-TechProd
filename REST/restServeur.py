# -*- coding: utf-8 -*-
from bottle.bottle import run, route, request, error
import json
import sqlite3

dbPath = "../DB/data.db"



def dict_factory(cursor, row):
	""" Permet de créer un tableau associatif avec les résultat de la requête SQL """
	d = {}
	for idx, col in enumerate(cursor.description):
		d[col[0]] = row[idx]
	return d

def replaceSpecialChar(s):
	return s.replace('[ÀÂÄÈÉÊËÎÏÔŒÙÛÜŸàâäèéêëîïôœùûüÿÇç«»€]','_',s)


@route('/installations', method='GET')
def installations():

	conn = sqlite3.connect(dbPath)
	conn.row_factory = dict_factory
	c = conn.cursor()
	try:
		localisation = request.query['localisation']
		print(localisation)
	except KeyError:
		print('no localisation')
		localisation = -1
	try:
		code_postal = request.query['cp']
	except KeyError:
		print('no cp')
		code_postal = -1

	try:
		recherche = request.query['recherche']
	except KeyError:
		print('no recherche')
		recherche = -1
	if localisation == -1 and code_postal == -1 and recherche == -1:
		req = 'SELECT * FROM installations ;'
	else:
		req = 'SELECT * FROM installations WHERE '
		argWhere = []
		if localisation != -1:
			localisation = localisation.lower().title()
			argWhere.append('ComLib like "%' + replaceSpecialChar(localisation) + '%"')
		if code_postal != -1:
			argWhere.append('InsCodePostal="' + code_postal + '"')
		req += (' AND '.join(argWhere)) + ';'
	print(req)
	res = c.execute(req).fetchall()
	print(res)
	return json.dumps(dict(data=res), ensure_ascii=False).encode('utf-8')


@route('/equipements', method='GET')
def equipements():
	conn = sqlite3.connect(dbPath)
	conn.row_factory = dict_factory
	c = conn.cursor()
	res = c.execute('SELECT * FROM installations WHERE ComLib=\"' +
					localisation + '\" AND InsCodePostal="' + cp + '";').fetchall()
	# print(res)
	return json.dumps(dict(data=res)).encode('utf-8')


@route('/activites', method='GET')
def activites():
	conn = sqlite3.connect(dbPath)
	conn.row_factory = dict_factory
	c = conn.cursor()
	try:
		nom = request.query['nom']
	except KeyError:
		nom = -1
	try:
		ActivitePraticable = request.query['ActivitePraticable']
	except KeyError:
		ActivitePraticable = -1
	try:
		ActivitePratique = request.query['ActivitePratique']
	except KeyError:
		ActivitePratique = -1
	try:
		ActiviteSalleSpe = request.query['ActiviteSalleSpe']
	except KeyError:
		ActiviteSalleSpe = -1

	if nom == -1 and ActivitePraticable == -1 and ActivitePratique == -1 and ActiviteSalleSpe == -1:
		res = c.execute('SELECT EquipementId,ActLib,EquActivitePraticable,EquActivitePratique,EquActiviteSalleSpe FROM activites;').fetchall()
	else:
		argWhere = []
		req  = 'SELECT EquipementId,ActLib,EquActivitePraticable,EquActivitePratique,EquActiviteSalleSpe FROM activites WHERE '
		if nom != -1:
			argWhere.append(' ActLib Like \"%'+nom+'%\"')
		if ActivitePraticable != -1:
			argWhere.append(' EquActivitePraticable=\"Oui\"')
		else:
			argWhere.append(' EquActivitePraticable=\"Non\"')
		if ActivitePratique != -1:
			argWhere.append(' EquActivitePratique=\"Oui\"')
		else:
			argWhere.append(' EquActivitePratique=\"Non\"')
		if ActiviteSalleSpe != -1:
			argWhere.append(' EquActiviteSalleSpe=\"Oui\"')
		else:
			argWhere.append(' EquActiviteSalleSpe=\"Non\"')
		req += (' AND '.join(argWhere)) +';'
		print(req)
		res = c.execute(req).fetchall()
	print(res)
	return json.dumps(dict(data=res), ensure_ascii=False).encode('utf-8')


@error(404)
def error404(error):
	return '{ \"Error\" : 404}'


def main():
	run(host='localhost', port=8080)

# Execution de la fonction main au lancement du script
if __name__ == '__main__':
	main()
