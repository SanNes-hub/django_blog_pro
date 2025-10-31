import pytest
from django.contrib.auth.models import User
from .models import Post
from pytest_django.asserts import assertContains

# Esta "marca" 🛡️ é essencial!
# Ela diz ao pytest: "Este teste precisa de acesso 
# ao banco de dados 🗄️ (para criar o Post)."
@pytest.mark.django_db
def test_post_str_method():
    """
    Testa se o método __str__ do Model Post
    retorna corretamente o 'titulo'.
    
    Este é um exemplo de "Teste de Unidade".
    """
    
    # 1. ARRANGE (Organizar): Crie os dados necessários
    # (Temos que criar um autor 'User' primeiro, 
    # pois o 'autor' do Post é obrigatório)
    autor = User.objects.create_user(username='test_author', password='password123')
    
    # Criamos o Post, linkado ao autor
    post = Post.objects.create(
        autor=autor,
        titulo="Meu Post de Teste",
        conteudo="Este é o conteúdo do teste."
    )

    # 2. ACT (Agir): Execute a ação que queremos testar
    # (Neste caso, chamamos a função 'str()' no nosso objeto post)
    resultado = str(post)

    # 3. ASSERT (Verificar): Cheque se o resultado é o esperado
    # O resultado (resultado) é igual ao 'titulo' que definimos?
    assert resultado == "Meu Post de Teste"

@pytest.mark.django_db
def test_pagina_inicial_view(client):
    """
    Testa se a página inicial (lista de posts) carrega corretamente.
    
    Este é um exemplo de "Teste de Integração".
    
    O 'client' é um "navegador de mentira" que o Pytest
    nos dá para "visitar" nossas páginas.
    """
    
    # 1. ARRANGE (Organizar):
    #    (Não precisamos criar dados, só queremos ver se a página carrega)
    
    # 2. ACT (Agir):
    #    Use o 'client' 🤖 para "visitar" a URL raiz ('/').
    url = "/" # A URL da nossa 'pagina_inicial'
    response = client.get(url)

    # 3. ASSERT (Verificar):
    
    # Verificação 1: O servidor respondeu "OK" (código 200)?
    assert response.status_code == 200
    
    # Verificação 2: O HTML da resposta contém o título da nossa página?
    # (Isso prova que o template correto foi usado)
    assertContains(response, "Blog Profissional")