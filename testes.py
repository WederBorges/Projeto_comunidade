import os
import secrets
teste1 = 'default.jpg'

nome, extensao = os.path.splitext(teste1)
cod = secrets.token_hex(4)

t = os.path.join(nome,cod,extensao)
t2 = nome + cod + extensao

print(t)

print(t2)