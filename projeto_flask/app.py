from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

lista_produtos = [
    {"nome": "coca-cola", "descrição": "veneno", "preco": 1.0, "imagem": ""},
    {"nome": "doritos", "descrição": "veveno ao quadrado", "preco": 12344.0, "imagem": ""},
    {"nome": "agua", "descrição": "legal", "preco": 12.0, "imagem": ""}
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

@app.route("/produto/cadastro")
def cadastro_produto():
    return render_template("cadastro.html")

# POST
@app.route("/produtos", methods=["POST"])
def salvar_produto():
    lista_produtos.append({"nome": request.form["nome"], "descrição": request.form["descricao"], "preco": request.form["preco"] ,"imagem": request.form["imagem"]})
    return redirect(url_for("produtos"))
app.run()