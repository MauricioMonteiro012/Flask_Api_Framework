from flask import request, jsonify
from services.usuario_service import UsuarioService

class UsuarioController:
    """Controlador de usuários - gerencia as rotas HTTP"""
    
    def __init__(self):
        self.usuario_service = UsuarioService()
    
    def criar_usuario(self):
        """POST - Cria um novo usuário"""
        try:
            dados = request.get_json()
            
            if not dados:
                return jsonify({'erro': 'Dados não fornecidos'}), 400
            
            nome = dados.get('nome')
            email = dados.get('email')
            senha = dados.get('senha')
            cpf = dados.get('cpf')
            
            resposta, status = self.usuario_service.criar_usuario(nome, email, senha, cpf)
            return jsonify(resposta), status
        
        except Exception as e:
            return jsonify({'erro': str(e)}), 500
    
    def listar_todos_usuarios(self):
        """GET - Lista todos os usuários"""
        try:
            resposta, status = self.usuario_service.listar_todos_usuarios()
            return jsonify(resposta), status
        
        except Exception as e:
            return jsonify({'erro': str(e)}), 500
    
    def buscar_usuario_por_cpf(self, cpf):
        """GET - Busca um usuário pelo CPF"""
        try:
            resposta, status = self.usuario_service.buscar_usuario_por_cpf(cpf)
            return jsonify(resposta), status
        
        except Exception as e:
            return jsonify({'erro': str(e)}), 500
    
    def deletar_usuario(self, cpf):
        """DELETE - Deleta um usuário pelo CPF"""
        try:
            resposta, status = self.usuario_service.deletar_usuario(cpf)
            return jsonify(resposta), status
        
        except Exception as e:
            return jsonify({'erro': str(e)}), 500
