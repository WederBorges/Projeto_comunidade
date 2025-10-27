import os
import secrets
teste1 = 'default.jpg'

nome, extensao = os.path.splitext(teste1)
cod = secrets.token_hex(4)

def teste():
    lista = []
    nomes = 'weder', 'joao', 'pedra'

    for n in nomes:
        lista.append(n)

    print(lista)

    return ';'.join(lista)

teste()
    