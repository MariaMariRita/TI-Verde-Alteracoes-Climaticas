from flask import Blueprint, redirect, session, render_template

user_bp = Blueprint('user', __name__, template_folder='templates')

@user_bp.route('/')
def portal():
    return render_template('portal_usuario.html')

@user_bp.before_app_request
def checar_autenticacao():
    if 'criado' not in session:
        return redirect('/login')

