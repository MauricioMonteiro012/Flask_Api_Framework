from flask import Flask
from controllers.usuario_controller import UsuarioController

app = Flask(__name__)
usuario_controller = UsuarioController()

# Rotas de Usuários

@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    """POST - Criar novo usuário"""
    return usuario_controller.criar_usuario()

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    """GET - Listar todos os usuários"""
    return usuario_controller.listar_todos_usuarios()

@app.route('/usuarios/<cpf>', methods=['GET'])
def buscar_usuario(cpf):
    """GET - Buscar usuário pelo CPF"""
    return usuario_controller.buscar_usuario_por_cpf(cpf)

@app.route('/usuarios/<cpf>', methods=['DELETE'])
def deletar_usuario(cpf):
    """DELETE - Deletar usuário pelo CPF"""
    return usuario_controller.deletar_usuario(cpf)

@app.route('/', methods=['GET'])
def home():
    """GET - Rota inicial da API"""
    return {
        'mensagem': 'Bem-vindo à API de Usuários',
        'rotas': {
            'POST /usuarios': 'Criar novo usuário',
            'GET /usuarios': 'Listar todos os usuários',
            'GET /usuarios/<cpf>': 'Buscar usuário pelo CPF',
            'DELETE /usuarios/<cpf>': 'Deletar usuário pelo CPF'
        }
    }, 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
