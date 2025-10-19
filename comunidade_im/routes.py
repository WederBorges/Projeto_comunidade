from flask import render_template, request, redirect, url_for, flash
from comunidade_im import app, database, bcrypt
from comunidade_im.forms import Form_Login, Form_Criar_Conta
from comunidade_im.models import Usuario, Post
from flask_login import login_user

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

    # primeiro: qual botão foi enviado?
    if 'botao_submit_login' in request.form and form_login.validate_on_submit():
        usuario = Usuario.query.filter_by(email_cadastro=form_login.email_login.data).first()
        if usuario and bcrypt.check_password_hash(senha_cript, form_login.senha_login.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            flash("Login realizado com sucesso", "success")
            return redirect(url_for('home'))
        else:
            flash("Falha no Login, email ou senha incorretos", "alert-danger")

    elif 'botao_submit_criar_conta' in request.form and form_criar_conta.validate_on_submit():
        senha_cript = bcrypt.generate_password_hash(form_criar_conta.senha_cadastro.data)
        usuario = Usuario(user_name=form_criar_conta.user_name.data, #Nome do usuario
                         email_cadastro=form_criar_conta.email_cadastro.data, #Email do usuario 
                         senha_cadastro= senha_cript) #Campo de senha
        database.session.add(usuario)
        database.session.commit()
        flash(f"Cadastro realizado com sucesso seja bem-vindo {form_criar_conta.user_name.data} !", "primary")
        return redirect(url_for('home'))

    return render_template('login.html', form_login=form_login, form_criar_conta=form_criar_conta)
