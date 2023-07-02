from flask import Flask, render_template, request, redirect, session, flash


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo("gran turismo", "corrida", "Ps1, Ps2")
jogo2 = Jogo("GTA", "açao", "Ps4, Ps5, PC")
jogo3 = Jogo("Wormate.IO", "passatempo", "Pc, Android")

lista_jogos = [jogo1, jogo2, jogo3]

app = Flask(__name__)
app.secret_key = "sul"


@app.route("/")
def index():
    return render_template("lista.html", titulo="Jogos", jogos=lista_jogos)


@app.route("/novo")
def add():
    return render_template("novo.html", titulo="Novo Jogo")


@app.route(
    "/criar",
    methods=[
        "POST",
    ],
)
def criar():
    nome = request.form["nome"]
    categoria = request.form["categoria"]
    console = request.form["console"]
    jogo = Jogo(nome, categoria, console)
    lista_jogos.append(jogo)

    return redirect("/")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route(
    "/autenticar",
    methods=[
        "POST",
    ],
)
def autenticar():
    if "azul" == request.form["senha"]:
        session["usuario_logado"] = request.form["usuario"]
        flash(session["usuario_logado"] + ", logado com sucesso")
        return redirect("/")
    else:
        flash("Usuário não logado")
        return redirect("/login")


if __name__ == "__main__":
    app.run(debub=True)