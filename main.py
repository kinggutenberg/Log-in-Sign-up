from flask import Flask, render_template, request, url_for, flash, redirect, session
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
        return render_template('index.html')

def check_usuarios(email, senha):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('SELECT email, senha, senha FROM users WHERE email=? and senha=?', (email, senha))

    resultado = cur.fetchone()
    if resultado:
        return True
    else:
        return False

@app.route('/login/', methods=('GET', 'POST'))
def login():
    if (session):
        return redirect(url_for('index'))
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        if not email:
            flash('email is required')
        elif not senha:
            flash('password is required')
        elif(check_usuarios(email, senha)):
            session['email'] = email
            flash('Login done successfully')
            return redirect(url_for('index'))
        else:
            flash('email or password incorrect')
    
    return render_template('telalogin.html')

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))


@app.route('/cadastro/', methods=('GET', 'POST'))
def cadastro(): 
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        if not nome:
            flash('Name is required!')
        elif not email:
            flash('Email is required!')
        elif not senha:
            flash('Senha is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO users (nome, email, senha) VALUES (?, ?, ?)',
                         (nome, email, senha))
            conn.commit()
            conn.close()
            flash('successful registration, now log in')
            return redirect(url_for('login'))

    return render_template('telacadastro.html')


app.run(host='0.0.0.0', port=81, debug=True)