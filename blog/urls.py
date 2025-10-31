from django.urls import path
from . import views  # O "." significa "da pasta atual", importe o views.py

urlpatterns = [
    # Este é o nosso interruptor:
    # 1. '' (aspas vazias) = a URL raiz (ex: /blog/)
    # 2. views.pagina_inicial = a "lâmpada" que ele acende
    # 3. name='pagina_inicial' = um "apelido" para esta URL
    path('', views.pagina_inicial, name='pagina_inicial'),

    # 2. Página de Detalhe (Um Post Específico)
    path('post/<int:pk>/', views.pagina_detalhe, name='pagina_detalhe'),
    # 3. Página de Cadastro (página onde o usuário se cadastra)
    path('cadastro/', views.pagina_cadastro, name='pagina_cadastro'),
    # 4. Página de logout 
    path('logout/', views.pagina_logout, name='pagina_logout'),
    # 5. Página de login
    path('login/', views.pagina_login, name='pagina_login'),
    # 6. Novo Post
    path('post/novo/', views.pagina_criar_post, name='pagina_criar_post'),
    # 7. Editar um Post
    path('post/<int:pk>/editar/', views.pagina_editar_post, name='pagina_editar_post'),
    # 8. Deletar um Post
    path('post/<int:pk>/deletar/', views.pagina_deletar_post, name='pagina_deletar_post'),
]