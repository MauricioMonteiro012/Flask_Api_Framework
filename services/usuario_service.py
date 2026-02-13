from models.usuario import Usuario

class UsuarioService:
    """Serviço de usuários - lógica de negócio"""
    
    def __init__(self):
        self.usuarios = []
    
    def criar_usuario(self, nome, email, senha, cpf):
        """Cria um novo usuário"""
        # Validar se CPF já existe
        if self._verificar_cpf_existe(cpf):
            return {'erro': 'CPF já cadastrado'}, 400
        
        # Validar campos obrigatórios
        if not self._validar_campos(nome, email, senha, cpf):
            return {'erro': 'Todos os campos são obrigatórios'}, 400
        
        usuario = Usuario(nome, email, senha, cpf)
        self.usuarios.append(usuario.to_dict())
        
        return {'mensagem': 'Usuário criado com sucesso', 'usuario': usuario.to_dict()}, 201
    
    def listar_todos_usuarios(self):
        """Lista todos os usuários"""
        if not self.usuarios:
            return {'mensagem': 'Nenhum usuário cadastrado', 'usuarios': []}, 200
        
        return {'usuarios': self.usuarios, 'total': len(self.usuarios)}, 200
    
    def buscar_usuario_por_cpf(self, cpf):
        """Busca um usuário pelo CPF"""
        usuario = self._encontrar_usuario_por_cpf(cpf)
        
        if usuario is None:
            return {'erro': 'Usuário não encontrado'}, 404
        
        return {'usuario': usuario}, 200
    
    def deletar_usuario(self, cpf):
        """Deleta um usuário pelo CPF"""
        usuario = self._encontrar_usuario_por_cpf(cpf)
        
        if usuario is None:
            return {'erro': 'Usuário não encontrado'}, 404
        
        self.usuarios.remove(usuario)
        return {'mensagem': 'Usuário deletado com sucesso'}, 200
    
    def _encontrar_usuario_por_cpf(self, cpf):
        """Encontra um usuário pelo CPF"""
        for usuario in self.usuarios:
            if usuario['cpf'] == cpf:
                return usuario
        return None
    
    def _verificar_cpf_existe(self, cpf):
        """Verifica se um CPF já existe"""
        return self._encontrar_usuario_por_cpf(cpf) is not None
    
    def _validar_campos(self, nome, email, senha, cpf):
        """Valida os campos obrigatórios"""
        return all([nome, email, senha, cpf])
