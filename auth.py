from flask import Blueprint, request, redirect, url_for, session, render_template
from datetime import datetime
auth_bp = Blueprint('auth', __name__, template_folder='templates')

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        session['nome'] = request.form['nome']
        session['email'] = request.form['email']
        session['senha'] = request.form['senha']
        session['genero'] = request.form['genero']
        # Só foematando pra dd/mm/yyyy
        data_obj = datetime.strptime(request.form['data'], '%Y-%m-%d')
        session['data'] = data_obj.strftime('%d/%m/%Y')
        session['criado'] = True
        return redirect(url_for('homepage'))
    return render_template("signup.html")

@auth_bp.route('/logout')
def logout():
    session.pop('nome')
    session.pop('email')
    session.pop('senha')
    session.pop('genero')
    session.pop('data')
    session.pop('criado')
    return redirect(url_for('homepage'))