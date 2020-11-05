from flask import Flask, request, redirect, url_for
from jinja2 import Template, Environment, FileSystemLoader
import json

environment="development"

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

app = Flask(__name__, static_url_path='/static')
with open('data.json') as json_file:
    my_json = json.load(json_file)

def mensaje():
    mensaje='Hola desde el método'
    return "alert('"+ mensaje + "')"

# mystring=request.form['form.html']
# reverse = (mystring[::-1])
# len = (len(mystring))
# upper = (mystring.upper())
# lower = (mystring.lower())

@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        _codigo = request.form['codigo']
        # _tipo = request.form['tipo']
        # _nombre = request.form['nombre']
        # _pasillo = request.form['pasillo']
        # _thumbnail = request.form['thumbnail']
        # my_json['data'].append({"codigo":_codigo, "tipo":_tipo, "nombre":_nombre, "pasillo":_pasillo, "thumbnail":_thumbnail})
        # print('Insertados:',_codigo, _tipo, _nombre, _pasillo)
        ##print(my_json)
        return redirect(url_for('index'))
    
    if request.method == 'GET': 
        template = env.get_template('lista.html')
        return template.render()
    else:
        template = env.get_template('lista.html')
        return template.render()
@app.route('/', methods=['GET', 'POST'])
def index():
    template = env.get_template('form.html')
    return template.render(my_data=my_json['data'], headers=my_json['headers'])

if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    print("Local change")
    app.run(host="0.0.0.0")


