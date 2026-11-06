
☆ API REST para gerenciamento de usuários e pedidos, desenvolvida com FastAPI. Inclui autenticação com tokens JWT, controle de acesso por usuário e administração, e persistência em SQLite.

◇ Recursos

➱ Cadastro e autenticação de usuários
➱ Geração de tokens de acesso e atualização
➱ Criação e gerenciamento de pedidos
➱ Inclusão e remoção de itens nos pedidos
➱ Cálculo do preço total do pedido
➱ Controle de acesso para usuários e administradores
➱ Migrações do banco de dados com Alembic
  
◇ Tecnologias

➱ Python
➱ FastAPI
➱ SQLAlchemy
➱ SQLite
➱ Alembic
➱ JWT

◇ Requisitos

➱ Python 3.10 ou superior
➱ pip

◇ Instalação

-------------------------------------------------
Clone o repositório e entre na pasta do projeto:
git clone <URL_DO_REPOSITORIO>
cd Curso-FastAPI
-------------------------------------------------
⁍ Crie e ative um ambiente virtual.

◇ Windows:

-------------------------------
python -m venv .venv
.venv\Scripts\Activate.ps1
-------------------------------

◇ Linux ou macOS:

-------------------------------
python3 -m venv .venv
source .venv/bin/activate
-------------------------------

◇ Instale as dependências:

⁍ pip install fastapi uvicorn sqlalchemy sqlalchemy-utils alembic passlib[bcrypt] python-dotenv python-jose[cryptography] python-multipart requests


◇ Configuração

⁍ Crie um arquivo .env na raiz do projeto com as configurações usadas para assinar e validar os tokens:

---------------------------------
SECRET_KEY=sua_chave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
---------------------------------

⁍ Use uma chave secreta própria e não compartilhe o arquivo .env.

◇ Banco de dados

⁍ O projeto usa SQLite e cria o banco banco.db na raiz. Para aplicar as migrações do Alembic:

---------------------------------
alembic upgrade head
---------------------------------

◇ Executar a API

⁍ Na raiz do projeto, execute:

---------------------------------
uvicorn main:app --reload
---------------------------------

◇ A API ficará disponível em:

▻ http://127.0.0.1:8000

▻ Documentação interativa: http://127.0.0.1:8000/docs


◇ Endpoints principais


➠ Método	Endpoint	Descrição

➠ GET	/auth/	Rota inicial de autenticação

➠ POST	/auth/criar_conta	Cadastra um usuário

➠ POST	/auth/login	Autentica com e-mail e senha

➠ POST	/auth/login-form	Autentica usando formulário OAuth2

➠ GET	/auth/refresh	Gera um novo token de acesso

➠ GET	/order/	Rota inicial de pedidos 

➠ POST	/order/pedido	Cria um pedido

➠ GET	/order/pedido/{id_pedido}	Consulta um pedido

➠ POST	/order/pedido/adicionar-item/{id_pedido}	Adiciona um item ao pedido

➠ POST	/order/pedido/remover-item/{id_item_pedido}	Remove um item do pedido

➠ POST	/order/pedido/cancelar/{id_pedido}	Cancela um pedido

➠ POST	/order/pedido/finalizar/{id_pedido}	Finaliza um pedido

➠ GET	/order/listar	Lista todos os pedidos; requer acesso de administrador

➠ GET	/order/listar/pedidos-usuario	Lista os pedidos do usuário autenticado


◇ As rotas de pedidos exigem autenticação. Envie o token de acesso no cabeçalho:

--------------------------------------
Authorization: Bearer <access_token>
--------------------------------------

◇ Exemplos de requisição

⁍ Cadastro de usuário:

---------------------------------
{
  "nome": "Maria",
  "email": "maria@example.com",
  "senha": "uma_senha",
  "ativo": true,
  "admin": false
}
---------------------------------


◇ Login:
---------------------------------
{
  "email": "maria@example.com",
  "senha": "uma_senha"
}
---------------------------------

◇ Criação de pedido:

---------------------------------
{
  "usuario": 1
}
---------------------------------

◇ Adição de item:

---------------------------------
{
  "quantidade": 2,
  "sabor": "calabresa",
  "tamanho": "grande",
  "preco_unitario": 45.0,
  "id_pedido": 1
}
---------------------------------

◇ Estrutura do projeto


➠ main.py: configura a aplicação FastAPI e a autenticação

➠ auth_routes.py: cadastro, login e tokens

➠ order_routes.py: rotas de pedidos e itens

➠ models.py: modelos e conexão com o SQLite

➠ shemas.py: esquemas de entrada e resposta

➠ dependeces.py: sessão do banco e validação de tokens

➠ alembic/: configuração e versões das migrações

➠ teste.py: exemplo de requisição à API


⊛ Observação

O projeto não inclui um arquivo requirements.txt. O comando de instalação acima lista os pacotes identificados no código.


