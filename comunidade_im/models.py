from comunidade_im import database, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    user_name = database.Column(database.String, nullable=False)
    email_cadastro = database.Column(database.String, nullable=False, unique=True)
    senha_cadastro = database.Column(database.String, nullable=False)
    foto_perfil =  database.Column(database.String, default='default.jpg')
    posts = database.relationship('Post', backref='Autor', lazy=True)
    cursos = database.Column(database.String, nullable=False, default="Não Informado")

class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.Text, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default = datetime.utcnow())
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)

