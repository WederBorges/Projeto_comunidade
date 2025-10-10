import time
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/usuarios')
def users():
    lista_usuarios = ["Nicolau BOBO CHERA CHERA"]

    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

if __name__ == "__main__":
    app.run(debug=True) #Nunca usar isso em prod