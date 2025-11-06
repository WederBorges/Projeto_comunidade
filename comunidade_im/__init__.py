from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import sqlalchemy
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

base_dir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = '355fcc96736a56eb286df457be1f3597e6e4400d11baed7dccd4f23b76fd0da3262bb29aa85137b88972de87ee11cffca5cd'

# Configurar banco de dados
try:
    if os.getenv("DATABASE_URL"):
        # Railway pode fornecer DATABASE_URL com postgres://, mas SQLAlchemy precisa postgresql://
        database_url = os.getenv("DATABASE_URL").replace("postgres://", "postgresql://", 1)
        app.config['SQLALCHEMY_DATABASE_URI'] = database_url
        logger.info("Usando DATABASE_URL do ambiente")
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(base_dir,'comunidade.db')}"
        logger.info("Usando SQLite local")
except Exception as e:
    logger.error(f"Erro ao configurar banco de dados: {e}")
    raise
    
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

# Importar models
try:
    from comunidade_im import models
    logger.info("Models importados com sucesso")
except Exception as e:
    logger.error(f"Erro ao importar models: {e}")
    raise

# Criar tabelas se não existirem
try:
    with app.app_context():
        # Verificar se as tabelas existem
        engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
        inspector = sqlalchemy.inspect(engine)
        
        if not inspector.has_table('usuario'):
            logger.info("Criando tabelas do banco de dados...")
            database.create_all()
            logger.info("Tabelas criadas com sucesso")
        else:
            logger.info("Tabelas já existem no banco de dados")
except Exception as e:
    logger.error(f"Erro ao verificar/criar tabelas: {e}")
    # Não levantar exceção aqui para permitir que a aplicação inicie mesmo se houver problema com o banco

# Importar routes
try:
    from comunidade_im import routes
    logger.info("Routes importados com sucesso")
except Exception as e:
    logger.error(f"Erro ao importar routes: {e}")
    raise

logger.info("Aplicação Flask inicializada com sucesso")