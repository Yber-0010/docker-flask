from flask import Flask, render_template, request, url_for, redirect
from datetime import datetime
app = Flask(__name__)

""" @app.route('/')
def hello_geek():
    return '<h1>Ejercicios python en FLASK WEB 2</h1>' """

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return 'hola {0}!'.format(nombre)

@app.route('/datos')
def datos():
    """ print(request.args) """
    """ en la ruta se ingresa http://127.0.0.1:5000/datos?val1=ACA EL VALOR OPTENIDO """
    val1 = request.args.get('val1')
    """ obtiene un request desde la ruta con los lavores en variables """
    return 'estos son los datos: {0}'.format(val1)

@app.route('/eje1', methods=['GET','POST'])
def eje1():
    data={
        'titulo': 'index',
        'encabezado': 'Bienbenid@'
    }
    if request.method == "POST":
        """ print(request.form['a']) """
        a=request.form['a']
        a = int(a)
        b=request.form['b']
        b = int(b)
        z=a+b
        return 'LA SUMA ES: {0}'.format(z)
    else:
        return render_template('eje1.html',data=data)

@app.route('/eje2', methods=['GET','POST'])
def eje2():
    data={
        'titulo': 'index',
        'encabezado': 'Bienbenid@'
    }
    if request.method == "POST":
        """ print(request.form['a']) """
        a=request.form['a']
        a = int(a)
        b=request.form['b']
        b = int(b)
        z=a-b
        return 'LA RESTA ES: {0}'.format(z)
    else:
        return render_template('eje2.html',data=data)

@app.route('/eje3', methods=['GET','POST'])
def eje3():
    multiplicacion = ''
    divicion = ''
    data={
            'titulo': 'index',
            'encabezado': 'Bienbenid@',
            'multiplicacion': multiplicacion,
            'divicion': divicion
    }
    if request.method == "POST":
        """ print(request.form['a']) """
        a=request.form['a']
        a = int(a)
        b=request.form['b']
        b = int(b)
        t=request.form['t']
        if t == '2':
            multiplicacion=a*b
        if t == '1':
            divicion=a/b
        data={
            'a': a,
            'b': b,
            'titulo': 'index',
            'encabezado': 'Bienbenid@',
            'multiplicacion': multiplicacion,
            'divicion': divicion
        }
        return render_template('eje3.html',data=data)
        """ return 'resultado ES: {0}'.format(z) """
    else:
        return render_template('eje3.html',data=data)

@app.route('/eje4', methods=['GET','POST'])
def eje4():
    data={
        'titulo': 'index',
        'encabezado': 'Bienbenid@',
        'nombre': ''
    }
    if request.method == "POST":
        nombre = request.form['nombre']
        print(nombre)
        data={
            'titulo': 'index',
            'encabezado': 'Bienbenid@',
            'nombre': nombre
        }
        return render_template('eje4.html',data=data)
        """ return 'resultado ES: {0}'.format(z) """
    else:
        return render_template('eje4.html',data=data)

@app.route('/eje5', methods=['GET','POST'])
def eje5():
    respuesta = ''
    data={
            'titulo': 'index',
            'encabezado': 'Bienbenid@',
    }
    if request.method == "POST":
        """ print(request.form['a']) """
        a=request.form['a']
        a = int(a)
        b=request.form['b']
        b = int(b)
        if a == b:
            respuesta = True
        else:
            respuesta = False
        data={
            'a': a,
            'b': b,
            'respuesta': respuesta,
        }
        return render_template('eje5.html',data=data)
        """ return 'resultado ES: {0}'.format(z) """
    else:
        return render_template('eje5.html',data=data)

@app.route('/eje6', methods=['GET','POST'])
def eje6():
    respuesta = ''
    """ fecha_string = "2022-11-10"
    fecha = datetime.strptime(fecha_string, "%Y-%m-%d")
    fecha_string2 = "2023-11-10"
    fecha2 = datetime.strptime(fecha_string2, "%Y-%m-%d") """
    data={
            'titulo': 'index',
            'encabezado': 'Bienbenid@',
    }
    if request.method == "POST":
        """ print(request.form['a']) """
        a=request.form['a']
        """ a = int(a) """
        b=request.form['b']
        """ b = int(b) """
        z=''
        if a == b:
            respuesta = True
        else:
            fecha_string = a
            fecha = datetime.strptime(fecha_string, "%Y-%m-%d")
            fecha_string2 = b
            fecha2 = datetime.strptime(fecha_string2, "%Y-%m-%d")
            z = fecha2 - fecha
            respuesta = False

        data={
            'a': a,
            'b': b,
            'respuesta': respuesta,
            'z': z
        }
        return render_template('eje6.html',data=data)
        """ return 'resultado ES: {0}'.format(z) """
    else:
        return render_template('eje6.html',data=data)

@app.route('/eje7', methods=['GET','POST'])
def eje7():
    data={
        'titulo': 'index',
        'encabezado': 'Bienbenid@',
        'nombre': 0
    }
    if request.method == "POST":
        nombre = request.form['nombre']
        nombre = int(nombre)
        if nombre%4==0:
            b=True
        else:
            b=False
        print(b)
        data={
            'titulo': 'index',
            'encabezado': 'Bienbenid@',
            'nombre': nombre,
            'b':b
        }
        return render_template('eje7.html',data=data)
        """ return 'resultado ES: {0}'.format(z) """
    else:
        return render_template('eje7.html',data=data)

@app.route('/')
def index():
    data={
        'titulo': 'index',
        'encabezado': 'Bienbenid@ desde el contenedor'
    }
    return render_template('index.html',data=data)

if __name__ == "__main__":
    app.add_url_rule('/', view_func=index)
    app.run(debug=True)