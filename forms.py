from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo



class Form_Criar_Conta(FlaskForm):
    user_name = StringField("Nome de Usuário", validators=[DataRequired(), Length(3, 20)])
    email_cadastro = StringField("E-mail", validators=[DataRequired(),Email()])
    senha_cadastro = PasswordField("Senha", validators=[DataRequired(), Length(6, 50)])
    confirmar_senha = PasswordField("Confirmar senha", validators=[DataRequired(), Length(6, 50), EqualTo('senha')])
    botao_submit_criar_conta = SubmitField("Criar Conta")

class Form_Login(FlaskForm):
    email_login = StringField("E-mail", validators=[DataRequired(),Email()])
    senha_login = PasswordField("Senha", validators=[DataRequired(), Length(6, 50)])
    botao_submit_login = SubmitField("Realizar Login")
    lembrar_dados = BooleanField('Lembrar dados')