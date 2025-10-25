from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidade_im.models import Usuario
from flask_login import current_user


class Form_Criar_Conta(FlaskForm):
    user_name = StringField("Nome de Usuário", validators=[DataRequired(), Length(3, 20)])
    email_cadastro = StringField("E-mail", validators=[DataRequired(),Email()])
    senha_cadastro = PasswordField("Senha", validators=[DataRequired(), Length(6, 50)])
    confirmar_senha = PasswordField("Confirmar senha", validators=[DataRequired(), Length(6, 50), EqualTo('senha_cadastro')])
    botao_submit_criar_conta = SubmitField("Criar Conta")

    def validate_email_cadastro(self, email_cadastro):
        usuario = Usuario.query.filter_by(email_cadastro=email_cadastro.data).first()
        if usuario:
            raise ValidationError('Email já cadastrado. Utilize outro E-mail ou faça Login para continuar.')

class Form_Login(FlaskForm):
    email_login = StringField("E-mail", validators=[DataRequired(),Email()])
    senha_login = PasswordField("Senha", validators=[DataRequired(), Length(6, 50)])
    botao_submit_login = SubmitField("Realizar Login")
    lembrar_dados = BooleanField('Lembrar dados')

class Form_EditarPerfil(FlaskForm):
    user_name = StringField("Nome de Usuário", validators=[DataRequired(), Length(3, 20)])
    email_cadastro = StringField("E-mail", validators=[DataRequired(),Email()])
    foto_perfil = FileField("Editar foto de perfil", validators=[FileAllowed(['jpg', 'png'])])
    botao_editar_perfil = SubmitField("Confirmar Edição")

    curso_excel = BooleanField('Excel')
    curso_bi = BooleanField('Power BI')
    curso_python = BooleanField('Python')
    curso_sql = BooleanField('Sql')
    
    def validate_email_cadastro(self, email_cadastro):
        if current_user.email_cadastro != email_cadastro.data:
            usuario = Usuario.query.filter_by(email_cadastro=email_cadastro.data).first()
            if usuario:
                raise ValidationError('Email já cadastrado. Utilize outro E-mail.')
