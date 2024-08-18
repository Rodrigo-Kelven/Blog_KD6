from flask import Flask
from routes.home import home_rotas # aqui eu estou importando a variavel que foi agregada com o Blueprint
from routes.clientes import clientes_rotas


# inicializaçao do Flask
app = Flask(__name__)

"""
Agora a variavel " app " que foi declarada AQUI pode receber a varivael que fo importanda!
Usando a função " register_blueprint " e passando no parametro a função que foi importada
"""


app.register_blueprint(home_rotas)
app.register_blueprint(clientes_rotas, url_prefix='/clientes') """ este | url_prefix='' | serve basicamente para setar uma "restrição" em todas as urls da rota /clientes.
Exemplo: para acessar a rota /new, tenho que acessar a rota /clientes . só assim posso acessar a rota /clientes/new
"""

# Execução do Flask em modo debug= True
app.run(debug=True)