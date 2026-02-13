import unittest
import json
from app import app

class TestUsuariosAPI(unittest.TestCase):
    
    def setUp(self):
        """Configuração antes de cada teste"""
        self.app = app
        self.client = self.app.test_client()
    
    def test_rota_inicial(self):
        """Testa a rota inicial"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('mensagem', response.json)
    
    def test_criar_usuario(self):
        """Testa criação de usuário"""
        usuario = {
            'nome': 'João Silva',
            'email': 'joao@email.com',
            'senha': 'senha123',
            'cpf': '12345678900'
        }
        response = self.client.post('/usuarios', 
                                    data=json.dumps(usuario),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('mensagem', response.json)
    
    def test_listar_usuarios(self):
        """Testa listagem de usuários"""
        # Criar um usuário primeiro
        usuario = {
            'nome': 'Maria Santos',
            'email': 'maria@email.com',
            'senha': 'senha456',
            'cpf': '98765432100'
        }
        self.client.post('/usuarios',
                        data=json.dumps(usuario),
                        content_type='application/json')
        
        # Listar usuários
        response = self.client.get('/usuarios')
        self.assertEqual(response.status_code, 200)
        self.assertIn('usuarios', response.json)
    
    def test_buscar_usuario_por_cpf(self):
        """Testa busca de usuário por CPF"""
        # Criar usuário
        usuario = {
            'nome': 'Pedro Costa',
            'email': 'pedro@email.com',
            'senha': 'senha789',
            'cpf': '11111111111'
        }
        self.client.post('/usuarios',
                        data=json.dumps(usuario),
                        content_type='application/json')
        
        # Buscar por CPF
        response = self.client.get('/usuarios/11111111111')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['usuario']['cpf'], '11111111111')
    
    def test_buscar_usuario_inexistente(self):
        """Testa busca de usuário que não existe"""
        response = self.client.get('/usuarios/99999999999')
        self.assertEqual(response.status_code, 404)
        self.assertIn('erro', response.json)
    
    def test_deletar_usuario(self):
        """Testa deletar um usuário"""
        # Criar usuário
        usuario = {
            'nome': 'Ana Silva',
            'email': 'ana@email.com',
            'senha': 'senha999',
            'cpf': '22222222222'
        }
        self.client.post('/usuarios',
                        data=json.dumps(usuario),
                        content_type='application/json')
        
        # Deletar usuário
        response = self.client.delete('/usuarios/22222222222')
        self.assertEqual(response.status_code, 200)
        
        # Verificar que foi deletado
        response = self.client.get('/usuarios/22222222222')
        self.assertEqual(response.status_code, 404)
    
    def test_criar_usuario_cpf_duplicado(self):
        """Testa criação com CPF duplicado"""
        usuario = {
            'nome': 'Lucas Ferreira',
            'email': 'lucas@email.com',
            'senha': 'senha111',
            'cpf': '33333333333'
        }
        
        # Criar primeiro
        self.client.post('/usuarios',
                        data=json.dumps(usuario),
                        content_type='application/json')
        
        # Tentar criar outro com mesmo CPF
        usuario2 = {
            'nome': 'Outro Nome',
            'email': 'outro@email.com',
            'senha': 'senha222',
            'cpf': '33333333333'
        }
        response = self.client.post('/usuarios',
                                   data=json.dumps(usuario2),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('erro', response.json)

if __name__ == '__main__':
    unittest.main()
