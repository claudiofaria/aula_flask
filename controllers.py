from aplicacao import app
from flask import render_template

@app.route('/home')
def home():
    return '<h1>Olá mundo na rota Home</h1>'

@app.route('/')
def ola():
    return render_template('index.html')

@app.route('/funcao')
def pagina_funcao():
    return '<h1>Funcao | Hello World</h1>'

app.run(debug=True)