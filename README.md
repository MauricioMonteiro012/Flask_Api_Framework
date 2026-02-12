# API de Usuários - CRUD com Flask

## 👥 Autores
- **Emilly Silva Eduardo Pereira** (2403751)
- **Gabrielly Soares Marinho** (2403430)
- **Maurício Monteiro Filho** (2302967)
- **Analice Ferreira** (2404038)

## 📋 Descrição
Aplicação API em Python desenvolvida com Flask para realizar operações básicas de CRUD (Create, Read, Delete) de usuários. A aplicação utiliza arquitetura MVC + Service com armazenamento de dados em lista (array).

## 🏗️ Arquitetura
```
Api - Framework/
├── models/              # Camada de Modelos
│   └── usuario.py      # Modelo de Usuário
├── controllers/        # Camada de Controle (MVC)
│   └── usuario_controller.py  # Controlador de Usuários
├── services/          # Camada de Serviços (Lógica de Negócio)
│   └── usuario_service.py    # Serviço de Usuários
├── app.py            # Aplicação Principal (Flask)
├── requirements.txt  # Dependências do Projeto
└── README.md        # Este arquivo
```

## 🔧 Tecnologias Utilizadas
- **Python 3.x**
- **Flask** - Framework Web
- **Arquitetura MVC + Service** - Separação clara de responsabilidades

## 📦 Instalação

### 1. Verificar Python instalado
```bash
python --version
```

### 2. Instalar dependências
```bash
pip install -r requirements.txt
```

## 🚀 Como Usar

### 1. Executar a aplicação
```bash
python app.py
```

A API estará disponível em: `http://localhost:5000`

### 2. Endpoints disponíveis

#### **POST /usuarios** - Criar Usuário
Cria um novo usuário com os dados fornecidos.

**Request:**
```json
POST http://localhost:5000/usuarios
Content-Type: application/json

{
  "nome": "João Silva",
  "email": "joao@email.com",
  "senha": "senha123",
  "cpf": "12345678900"
}
```

**Response (201):**
```json
{
  "mensagem": "Usuário criado com sucesso",
  "usuario": {
    "nome": "João Silva",
    "email": "joao@email.com",
    "senha": "senha123",
    "cpf": "12345678900"
  }
}
```

---

#### **GET /usuarios** - Listar Todos os Usuários
Retorna uma lista de todos os usuários cadastrados.

**Request:**
```bash
GET http://localhost:5000/usuarios
```

**Response (200):**
```json
{
  "usuarios": [
    {
      "nome": "João Silva",
      "email": "joao@email.com",
      "senha": "senha123",
      "cpf": "12345678900"
    },
    {
      "nome": "Maria Santos",
      "email": "maria@email.com",
      "senha": "senha456",
      "cpf": "98765432100"
    }
  ],
  "total": 2
}
```

---

#### **GET /usuarios/{cpf}** - Buscar Usuário por CPF
Busca e retorna um usuário específico pelo seu CPF.

**Request:**
```bash
GET http://localhost:5000/usuarios/12345678900
```

**Response (200):**
```json
{
  "usuario": {
    "nome": "João Silva",
    "email": "joao@email.com",
    "senha": "senha123",
    "cpf": "12345678900"
  }
}
```

**Response (404):**
```json
{
  "erro": "Usuário não encontrado"
}
```

---

#### **DELETE /usuarios/{cpf}** - Deletar Usuário
Remove um usuário da lista pelo CPF.

**Request:**
```bash
DELETE http://localhost:5000/usuarios/12345678900
```

**Response (200):**
```json
{
  "mensagem": "Usuário deletado com sucesso"
}
```

**Response (404):**
```json
{
  "erro": "Usuário não encontrado"
}
```

---

#### **GET /** - Rota Inicial
Retorna informações sobre a API e suas rotas.

**Request:**
```bash
GET http://localhost:5000/
```

**Response (200):**
```json
{
  "mensagem": "Bem-vindo à API de Usuários",
  "rotas": {
    "POST /usuarios": "Criar novo usuário",
    "GET /usuarios": "Listar todos os usuários",
    "GET /usuarios/<cpf>": "Buscar usuário pelo CPF",
    "DELETE /usuarios/<cpf>": "Deletar usuário pelo CPF"
  }
}
```

## ✅ Funcionalidades Implementadas

- ✓ **Criar Usuário** - Adiciona novo usuário com validação de campos obrigatórios
- ✓ **Listar Todos os Usuários** - Retorna lista completa de usuários cadastrados
- ✓ **Buscar Usuário por CPF** - Localiza e retorna usuário específico
- ✓ **Deletar Usuário** - Remove usuário da lista por CPF
- ✓ **Validação de Dados** - Verifica campos obrigatórios e CPF duplicado
- ✓ **Tratamento de Erros** - Respostas HTTP apropriadas com mensagens claras

## 🧪 Testando a API com cURL

### Criar Usuário
```bash
curl -X POST http://localhost:5000/usuarios \
  -H "Content-Type: application/json" \
  -d '{"nome":"João Silva","email":"joao@email.com","senha":"senha123","cpf":"12345678900"}'
```

### Listar Todos
```bash
curl http://localhost:5000/usuarios
```

### Buscar por CPF
```bash
curl http://localhost:5000/usuarios/12345678900
```

### Deletar Usuário
```bash
curl -X DELETE http://localhost:5000/usuarios/12345678900
```

## 📝 Campos de Usuário

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| nome | String | ✓ | Nome completo do usuário |
| email | String | ✓ | Email do usuário |
| senha | String | ✓ | Senha do usuário |
| cpf | String | ✓ | CPF do usuário (identificador único) |

## 🔐 Considerações de Segurança

⚠️ **Nota**: Esta é uma aplicação de demonstração. Para produção:
- Implementar hash de senhas (eg: bcrypt)
- Adicionar autenticação/autorização (JWT)
- Validar formato de email
- Criptografar dados sensíveis
- Implementar rate limiting

## 📄 Licença
Projeto desenvolvido para fins educacionais.
