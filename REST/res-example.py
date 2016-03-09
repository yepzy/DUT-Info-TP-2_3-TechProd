from libs.bottle import route, template, run


@route('/')
def index():
    return '<b>Hello World</b>!'

# @route('/<name>')
# def index(name):
#     return template('<b>Hello {{name}}</b>!', name=name)


run(host='localhost', port=8080)