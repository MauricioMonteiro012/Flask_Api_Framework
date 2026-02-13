class Usuario:
    """Modelo de usuário"""
    
    def __init__(self, nome, email, senha, cpf):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cpf = cpf
    
    def to_dict(self):
        """Converte o usuário para dicionário"""
        return {
            'nome': self.nome,
            'email': self.email,
            'senha': self.senha,
            'cpf': self.cpf
        }
    
    @staticmethod
    def from_dict(dados):
        """Cria um usuário a partir de um dicionário"""
        return Usuario(
            nome=dados.get('nome'),
            email=dados.get('email'),
            senha=dados.get('senha'),
            cpf=dados.get('cpf')
        )
