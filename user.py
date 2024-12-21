from flask import Blueprint, redirect, session, render_template, url_for

user_bp = Blueprint('user', __name__, template_folder='templates')

@user_bp.route('/')
def portal():
    nome = session.get('nome')
    email = session.get('email')
    senha = session.get('senha')
    genero = session.get('genero')
    data = session.get('data')
    return render_template('portal_usuario.html', user_nome = nome, user_email = email, user_senha = senha, user_genero = genero, user_data = data)

@user_bp.before_request
def check_login():
    if 'criado' not in session:
        return redirect(url_for('auth.signup'))

