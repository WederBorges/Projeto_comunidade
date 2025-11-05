from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import sqlalchemy
app = Flask(__name__)

base_dir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = '355fcc96736a56eb286df457be1f3597e6e4400d11baed7dccd4f23b76fd0da3262bb29aa85137b88972de87ee11cffca5cd'

if os.getenv("DATABASE_URL"):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")     
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(base_dir,'comunidade.db')}"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'


from comunidade_im import models
engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
inspector = sqlalchemy.inspect(engine)
if not inspector.has_table('usuario'):
    with app.app_context():
        database.drop_all()
        database.create_all()
        print("Base de dados criada com sucesso")
else:
    print("Base de dados já existente")

from comunidade_im import routes