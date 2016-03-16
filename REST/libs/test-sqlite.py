import bottle
from bottle.ext import sqlite

app = bottle.Bottle()
plugin = sqlite.Plugin(dbfile='../DB/data.db')
app.install(plugin)

@app.route('/show/:item')
def show(item, db):
    row = db.execute('SELECT * from equipements').fetchone()
    if row:
        return template('showitem', page=row)
    return HTTPError(404, "Page not found")

bottle.run(host='localhost', port=80)