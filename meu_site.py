from flask import Flask, render_template, request

app = Flask(__name__, static_folder= 'imagens')

@app.route("/")
def homepage():
    return render_template("homepage.html", active_page="home")

@app.route("/dados")
def dados():
    return render_template("dados.html", active_page="dados")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html", active_page="sobre")

if __name__ == "__main__":
    app.run(debug=True)
