from flask import render_template, request, redirect, url_for, flash
from comunidade_im import app, database, bcrypt
from comunidade_im.forms import Form_Login, Form_Criar_Conta, Form_EditarPerfil, Form_Criar_Post
from comunidade_im.models import Usuario, Post
from flask_login import login_user, logout_user, current_user, login_required
import secrets
import os
from PIL import Image

@app.route('/')
def home():
    posts = Post.query.order_by(Post.id.desc())
    cursos = None
    if current_user.is_authenticated:
        cursos = current_user.cursos

    return render_template('home.html', posts=posts, cursos=cursos)

@app.route('/usuarios')
@login_required
def users():
    lista_usuarios = [usuario for usuario in Usuario.query.all()]
    cursos = current_user.cursos
    if "Não informado" in cursos or cursos =="":
        total_cursos = 0
    else:
        total_cursos = len(cursos.split(';')) 

    return render_template('usuarios.html', lista_usuarios=lista_usuarios, total_cursos=total_cursos)
@app.route('/contato')
@login_required
def contato():
    return render_template('contato.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = Form_Login()
    form_criar_conta = Form_Criar_Conta()

    # primeiro: qual botão foi enviado?
    if 'botao_submit_login' in request.form and form_login.validate_on_submit():
        usuario = Usuario.query.filter_by(email_cadastro=form_login.email_login.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha_cadastro, form_login.senha_login.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            flash("Login realizado com sucesso", "success")
            parametro_next = request.args.get('next')
            if parametro_next:
                return redirect(parametro_next)
            else:
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

@app.route('/sair')
@login_required
def sair():
    logout_user()
    flash("Logout feito com sucesso", "primary")
    return redirect(url_for('home'))
    

@app.route('/perfil')
@login_required
def perfil():
    cursos = current_user.cursos
    foto_perfil = url_for('static', filename='fotos_perfil/{}'.format(current_user.foto_perfil))

    if "Não informado" in cursos or cursos =="":
        total_cursos = 0
    else:
        total_cursos = len(cursos.split(';')) 

    return render_template('perfil.html',usuario=current_user, foto_perfil=foto_perfil, total_cursos=total_cursos)



@app.route('/post/criar', methods=['GET', 'POST'])
@login_required
def criar_post():
    form = Form_Criar_Post()
    if form.validate_on_submit():
        post = Post(titulo=form.titulo.data, 
                    corpo=form.corpo.data,
                    autor = current_user)
        database.session.add(post)
        database.session.commit()
        flash('Post criado com sucesso', 'alert-sucess')
        return redirect(url_for('home'))
    return render_template('criarpost.html', form=form)


def salvar_imagem(imagem):
    codigo = secrets.token_hex(8)
    nome, extensao = os.path.splitext(imagem.filename)
    nome_arquivo = nome + codigo + extensao
    caminho_completo = os.path.join(app.root_path, 'static/fotos_perfil', nome_arquivo)
    
    tamanho = (400, 400)
    img_reduzida = Image.open(imagem)
    img_reduzida.thumbnail(tamanho)

    img_reduzida.save(caminho_completo)
    return nome_arquivo
# adicionar um codigo aleatorio na imagem
# reduzir o tamanho da imagem
# salvo a imagem no fotos_perfil
# altero a imagem do usuario
def atualizar_cursos(form):
    lista_cursos = []
    for campo in form:
        if 'curso_' in campo.name:
            if campo.data==True:
                lista_cursos.append(campo.label.text) 
    return ';'.join(lista_cursos)


@app.route('/perfil/editar', methods=['GET', 'POST'])
@login_required
def editar_perfil():
    form = Form_EditarPerfil()
    cursos = current_user.cursos
    
    if request.method == "GET":
        form.email_cadastro.data = current_user.email_cadastro 
        form.user_name.data = current_user.user_name 
        
  
    if form.validate_on_submit():
        current_user.email_cadastro = form.email_cadastro.data
        current_user.user_name = form.user_name.data
        if form.foto_perfil.data:
            nome_imagem = salvar_imagem(form.foto_perfil.data)
            current_user.foto_perfil = nome_imagem
        current_user.cursos = atualizar_cursos(form) 
        database.session.commit()
        flash("Perfil atualizado com sucesso", "primary")
        redirect(url_for('perfil'))
    else:
        if form.foto_perfil.errors:
            for erro in form.foto_perfil.errors:
                flash(f"Houve um erro: {erro} ao tentar subir novo arquivo de foto.", "danger")
    print(form.foto_perfil.errors)

    if "Não informado" in cursos or cursos =="":
        total_cursos = 0
    else:
        total_cursos = len(cursos.split(';')) 
    
    foto_perfil = url_for('static', filename='fotos_perfil/{}'.format(current_user.foto_perfil))
    
    return  render_template('editar_perfil.html', usuario=current_user, foto_perfil=foto_perfil, form=form, total_cursos=total_cursos)

@app.route('/post/<post_id>')
def exibir_post(post_id):
    post = Post.query.get(post_id)

    return render_template('exibir_post.html', post=post)