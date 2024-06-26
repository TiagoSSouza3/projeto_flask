from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def obter_produtos():
    with open("produtos.csv") as file:
        lista_produtos = []
        for linha in file:
            valores = linha.strip().split(",")
            nome, descricao, preco, imagem = valores
            produto = {
                "nome": nome,
                "descricao": descricao,
                "preco": preco,
                "imagem": imagem
            }
            lista_produtos.append(produto)

        return(lista_produtos)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contato")
def contato():
    return "<a style='color: black; text-decoration: none;' href='/'><h1>Contato</h1></a>"

@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos = obter_produtos())

@app.route("/produtos/<nome>")
def produto(nome):
    for produto in obter_produtos():
        if produto['nome'] == nome:
            return render_template("produto.html", produto = produto)
    return "Achei não"

@app.route("/produto/cadastro")
def cadastro_produto():
    return render_template("cadastro.html")

def adicionar_produto(produto):
    with open("produtos.csv", "a") as file:
        linha = f"{produto['nome']},{produto['descricao']},{produto['preco']},{produto['imagem']}\n"
        file.write(linha)

# POST
@app.route("/produtos", methods=["POST"])
def salvar_produto():
    produto = {"nome": request.form["nome"], "descricao": request.form["descricao"], "preco": request.form["preco"] ,"imagem": request.form["imagem"]}
    adicionar_produto(produto)
    return redirect(url_for("produtos"))
app.run()