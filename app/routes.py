from app import app
from flask import render_template, url_for

@app.route('/home')
@app.route('/')
def homepage():
    usuario = 'Kelvin'
    return render_template("index.html", usuario=usuario)

@app.route('/nova')
def novapag():
    return 'outra view'