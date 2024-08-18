"""
Este arquivo separado dentro de uma pasta serve para organizar rotas especificas
Neste arquivo estão somente as rotas destinadas as rotas home
"""

# importando o Blueprint e agregando uma variavel "home_rotas" 
from flask import Blueprint, render_template

home_rotas = Blueprint('home', __name__) # estes parametros sao obrigatorios! são responsáveis

# aqui voce faz igual fez no arquivo principal, só que usando a variavel => home_rotas que foi agregada ao Bluepirnt
@home_rotas.route('/')
def index():
    return render_template('home.html')

