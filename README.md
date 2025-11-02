Projeto Blog Profissional (django_blog_pro)
Olá! 👋 Bem-vindo(a) a um dos meus principais projetos de portfólio.

Este não é um blog "simples". Eu me desafiei a construir um projeto completo do zero, focando em todas as funcionalidades que um desenvolvedor back-end precisa saber.

O objetivo era aprender e demonstrar como todas as peças do Django se conectam: desde o banco de dados até a autenticação de usuários, testes e até mesmo uma API!

✨ Funcionalidades Principais (Features)
Este projeto é um sistema de blog completo onde:

📰 CRUD de Posts: Usuários podem Criar, Ler, Atualizar (Editar) e Deletar posts.

🔐 Autenticação Completa: Sistema de Cadastro, Login e Logout para usuários comuns.

🛡️ Permissões por Usuário: A funcionalidade mais legal! Um usuário só pode editar ou deletar os posts que ele mesmo criou.

🤖 API RESTful: Criei uma "porta dos fundos" (API) com o Django Rest Framework. Isso permite que outros programas (como um app de celular) leiam e escrevam posts usando dados JSON.

🧪 Testes Automatizados: Escrevi testes com Pytest para garantir que a lógica principal (como a criação de posts e a página inicial) funcione como esperado.

🕹️ Painel de Admin: O /admin do Django foi configurado para gerenciar os posts.

🛠️ Tecnologias Utilizadas
Para construir este projeto, eu usei as seguintes ferramentas:

Python 3

Django (O framework principal)

Django Rest Framework (DRF) (Para construir a API 🤖)

Pytest (Para os testes 🧪)

HTML5 & CSS3 (Para o front-end simples)

SQLite3 (Banco de dados usado no desenvolvimento)

🏃‍♀️ Como Rodar o Projeto Localmente
Se você quiser testar este projeto na sua máquina, é bem simples:

1. Clone o repositório:

Bash

git clone https://github.com/SanNes-hub/django_blog_pro.git
(Substitua pelo link do seu repositório se for diferente)

2. Entre na pasta:

Bash

cd django_blog_pro
3. Crie e ative o ambiente virtual:

Bash

# Criar o ambiente
python -m venv .venv

# Ativar (no Windows PowerShell)
.\.venv\Scripts\activate
4. Instale as ferramentas (do "bilhete de compras"):

Bash

pip install -r requirements.txt
5. Crie o banco de dados: (Isso vai criar o arquivo db.sqlite3 na sua pasta)

Bash

python manage.py migrate
6. Crie seu "Super-Usuário" (para o /admin): (Siga as instruções e crie sua senha)

Bash

python manage.py createsuperuser
7. Rode o servidor!

Bash

python manage.py runserver
Pronto! Agora você pode testar:
O Site (Porta da Frente): http://127.0.0.1:8000/

O Admin (Bastidores): http://127.0.0.1:8000/admin/

A API (Porta dos Fundos): http://127.0.0.1:8000/api/posts/
