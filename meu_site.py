from flask import Flask, render_template
from auth import auth_bp
from user import user_bp
from secrets import token_hex

app = Flask(__name__, static_folder= 'imagens')

app.config['SECRET_KEY'] = token_hex(24)

@app.route("/")
def homepage():
    return render_template("homepage.html", active_page="home")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/dados")
def dados():
    return render_template("dados.html")

# Registrando blueprint.
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(user_bp, url_prefix='/user')

if __name__ == "__main__":
    app.run(debug=True)
