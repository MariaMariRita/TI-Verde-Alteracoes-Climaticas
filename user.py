from flask import Blueprint, redirect, session, render_template

user_bp = Blueprint('user', __name__, template_folder='templates')

@user_bp.route('/')
def portal():
    return render_template('portal_usuario.html')



