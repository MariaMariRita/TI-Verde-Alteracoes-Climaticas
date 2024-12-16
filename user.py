from flask import Blueprint, redirect, session, render_template, url_for

user_bp = Blueprint('user', __name__, template_folder='templates')

@user_bp.route('/')
def portal():
    return render_template('portal_usuario.html')

@user_bp.before_request
def check_login():
    if 'criado' not in session:
        return redirect(url_for('templates.login'))

