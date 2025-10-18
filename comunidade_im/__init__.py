import time
from flask import Flask, render_template, url_for, request, flash, redirect
from comunidade_im.forms import Form_Criar_Conta, Form_Login
import email
from flask_sqlalchemy import SQLAlchemy
from comunidade_im.models import Usuario, Post

app = Flask(__name__)

app.config['SECRET_KEY'] = '355fcc96736a56eb286df457be1f3597e6e4400d11baed7dccd4f23b76fd0da3262bb29aa85137b88972de87ee11cffca5cd'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)