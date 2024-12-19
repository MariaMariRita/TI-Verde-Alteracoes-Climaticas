from flask import Blueprint, request, redirect, url_for, session, render_template

auth_bp = Blueprint('auth', __name__, template_folder='templates')

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        session['user'] = usuario
        session['criado'] = True
        return redirect(url_for('meu_site.homepage'))
    return render_template("login.html")