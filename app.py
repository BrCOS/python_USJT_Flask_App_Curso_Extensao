from flask import Flask, render_template
app = Flask('projeto')

@app.route('/')
def ola_mundo():
    nome = 'Bruno Costa'
    produtos = [
    {'nome': 'Ração', 'preco': 199.99},
    {'nome': 'Playstation', 'preco': 1999.99}]
    return render_template('alo.html', n=nome, aProdutos = produtos), 200

app.run()