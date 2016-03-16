import bottle
import bottle_sqlite

app = bottle.Bottle()
plugin = bottle.ext.sqlite.Plugin(dbfile='../DATA/data.db')
app.install(plugin)

@app.route('/test')
def index():
    return '<b>Hello World</b>!'


@app.route('/')
def show(db):
    row = db.execute('SELECT * from equipements').fetchone()
    if row:
        return template('showitem', page=row)
    return HTTPError(404, "Page not found")

run(host='localhost', port=80)