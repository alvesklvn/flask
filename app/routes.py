from app import app
from flask import render_template, url_for

@app.route('/index')
@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/nova')
def novapag():
    return 'outra view'