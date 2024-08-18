from flask import Blueprint, render_template
from database.cliente import CLIENTES


clientes_rotas = Blueprint('clientes', __name__)


"""
Rota de clientes

    - /clientes/ (GET) - Listar os clientes
    - /clientes/ (POST) - Inserir o cliente no servidor
    - /clientes/new (GET) - renderizar o formulario para criar um cliente
    - /clientes/<id> (GET) - obter os dados de um cliente
    - /clientes/<id>/edit (GET) - renderizar o formulario para editar um cliente
    - /clientes/<id>/update (PUT) - atualizar os dados do cliente
    - /clientes/<id>/delete (DELETE) - deleta o registro do usuario
"""

@clientes_rotas.route('/')
def listar_clientes():
    """Listar os clientes"""
    return render_template('lista_clientes.html', clientes=CLIENTES)


@clientes_rotas.route('/', methods=['POST'])
def inserir_cliente():
    """Inserir o cliente no servidor"""
    pass


@clientes_rotas.route('/new', methods=['GET'])
def form_cliente():
    """Formulario para cadastrar um cliente"""
    return render_template('form_cliente.html')


@clientes_rotas.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    """Exibir detalhe do cliente"""
    return render_template('detalhe_cliente.html')


@clientes_rotas.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    """Formulario para editar um cliente"""
    return render_template('form_edit_cliente.html')


@clientes_rotas.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    """atualizar informaçoes do cliente"""
    pass


@clientes_rotas.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    """deletar cliente"""
    pass