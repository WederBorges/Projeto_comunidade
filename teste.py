from flask import render_template, request, redirect, url_for, flash
from comunidade_im import app, database, bcrypt
from comunidade_im.forms import Form_Login, Form_Criar_Conta, Form_EditarPerfil
from comunidade_im.models import Usuario, Post
from flask_login import login_user, logout_user, current_user, login_required
import secrets
import os
from PIL import Image

print(current_user.cursos)
print(current_user)