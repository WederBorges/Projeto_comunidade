import time
from flask import Flask, render_template, url_for, request, flash, redirect
from forms import Form_Criar_Conta, Form_Login
import email
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '355fcc96736a56eb286df457be1f3597e6e4400d11baed7dccd4f23b76fd0da3262bb29aa85137b88972de87ee11cffca5cd'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/usuarios')
def users():
    lista_usuarios = ["Nicolau BOBO CHERA CHERA"]

    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = Form_Login() 
    form_criar_conta = Form_Criar_Conta()

    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        flash("Login realizado com sucesso", "sucess")
        return(redirect(url_for('home')))
    
    if form_criar_conta.validate_on_submit() and 'botao_submit_criar_conta' in request.form:
        flash("Cadastro realizado com sucesso", "Primary")
        return(redirect(url_for('home')))
    
    return render_template('login.html', form_login=form_login, form_criar_conta=form_criar_conta)
    

if __name__ == "__main__":
    app.run(debug=True) #Nunca usar isso em prod