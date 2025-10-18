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
        flash("Login realizado com sucesso", "success")
        return redirect(url_for('home'))

    elif 'botao_submit_criar_conta' in request.form and form_criar_conta.validate_on_submit():
        flash("Cadastro realizado com sucesso", "primary")
        return redirect(url_for('home'))

    return render_template('login.html', form_login=form_login, form_criar_conta=form_criar_conta)
