from flask import Flask, render_template
from auth import auth_bp

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/dados")
def dados():
    return render_template("dados.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

# Registrando blueprint.
app.register_blueprint(auth_bp, url_prefix='/login')


if __name__ == "__main__":
    app.run(debug= True )