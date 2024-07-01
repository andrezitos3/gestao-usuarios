from flask import Blueprint, render_template

cliente_route = Blueprint('cliente', __name__)

"""
Rota de clientes
- /clientes/ (GET) - listar os clientes
- /clientes/ (POST) - inserir o cliente no servidor
- /clientes/new (GET) - renderizar o formulario para criar um cliente
- /clientes/<id> (GET) - obter os dados de um cliente
- /clientes/<id>/edit (GET) - renderizar um formulario para editar um cliente
- /clientes/<id>/update (PUT) - atualizar os dados do cliente
- /clientes/<id>/delete (DELETE) - deleta o registro do usuario

"""


@cliente_route.route('/')
def listaClientes():
    # lista de clientes
    return render_template('lista_clientes.html')

@cliente_route.route('/', methods=['POST'])
def inserirCliente():
    # inserir os dados do cliente
    pass

@cliente_route.route('/new')
def formularioCliente():
    # formulario para cadastrar cliente
    return render_template('form_clientes.html')
    

@cliente_route.route('/<int:cliente_id>')
def detalheCliente(cliente_id):
    # exibir detalhes dos clientes
    return render_template('detalhe_cliente.html')

@cliente_route.route('/int:cliente_id>/edit')
def formularioEditCliente(cliente_id):
    # formulario para editar um cliente
    return render_template('form_edit_cliente.html')

@cliente_route.route('/int:cliente_id>/update', methods=['PUT'])
def updateCliente(cliente_id):
    # atualizar informacoes do cliente
    pass

@cliente_route.route('/int:cliente_id>/delete', methods=['DELETE'])
def deletarCliente(cliente_id):
    # deletar um cliente
    pass

