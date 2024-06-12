from flask import Flask, render_template

app = Flask(__name__)

lista_produtos = [
    {"nome": "coca-cola", "descrição": "veneno"},
    {"nome": "doritos", "descrição": "veveno ao quadrado"},
    {"nome": "agua", "descrição": "legal"}
]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contato")
def contato():
    return "<a style='color: black; text-decoration: none;' href='/'><h1>Contato</h1></a>"

@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos = lista_produtos)

@app.route("/produtos/<nome>")
def produto(nome):
    for produto in lista_produtos:
        if produto['nome'] == nome:
            return render_template("produto.html", produto = produto)
    return "Achei não"

app.run()