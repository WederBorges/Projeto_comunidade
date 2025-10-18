from comunidade_im.main import app, database
from comunidade_im.models import Usuario, Post

#with app.app_context():
#    database.create_all()


#with app.app_context():
    #usuario = Usuario(user_name='Weder Borges', email_cadastro='wedinho_dograu@gmail.com', senha_cadastro='weder123')
    #usuario2 = Usuario(user_name='raruminha', email_cadastro ='rarume_Um@gmail.com', senha_cadastro='weder1234')
    
    #database.session.add(usuario)
    #database.session.add(usuario2)

    #database.session.commit()

# with app.app_context():
#     meus_usuarios = Usuario.query.all()
#     usuario_name = [nome_user.user_name for nome_user in meus_usuarios]
#     usuario_teste = Usuario.query.filter_by(id=2).first()
#     print(usuario_teste.posts['corpo'])

#with app.app_context():

    #post_weder = Post(titulo="Farofa de Banana", corpo="Quem não gosta de Farofa de Banana em Cuiabá? ", id_usuario=1)

    #database.session.add(post_weder)

    #database.session.commit()

# with app.app_context():
#     todos_posts = Post.query.first()
#     print(todos_posts.Autor.user_name)
#     print(todos_posts.titulo)
#     print(todos_posts.corpo)

with app.app_context():
    database.drop_all()
    database.create_all()