from flask import Flask, render_template
from auth import auth_bp

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/dados")
def dados():
    return render_template("dados.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuario/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario = nome_usuario)

# Registrando blueprint.
app.register_blueprint(auth_bp, url_prefix='/login')

if __name__ == "__main__":
    app.run(debug= True )