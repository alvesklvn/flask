from app import app
from flask import render_template, url_for

idade = 17
usuario = 'Marlucia'
context = {'idade': idade, 'usuario': usuario}

@app.route('/home')
@app.route('/')
def homepage():
    return render_template("index.html", context=context)

@app.route('/nova')
def novapag():
    return 'outra view'