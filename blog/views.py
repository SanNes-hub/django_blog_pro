from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required  # O "escudo" 
from .forms import PostForm  # O "Formulário Inteligente"
from rest_framework import viewsets, permissions
from .serializers import PostSerializer

# Create your views here.
def pagina_inicial(request):
    todos_os_posts = Post.objects.all()

    # 2. Preparar o "pacote" de dados (o contexto)
    contexto = {
        'posts': todos_os_posts,  # O rótulo 'posts' vai levar nossos dados
    }
    # 3. Renderizar e retornar a página
    return render(request, 'blog/pagina_inicial.html', contexto)

def pagina_detalhe(request, pk):
    post_unico = Post.objects.get(pk=pk)

    contexto = {
        'post': post_unico,  # A variável 'post_unico' nos leva ao post em específico que queremos
    }
    # 3. Renderiza um novo template
    return render(request, 'blog/pagina_detalhe.html', contexto)

def pagina_cadastro(request):
    # 1. Checa se o método é POST (usuário clicou em "Enviar")
    if request.method == 'POST':
        # 2. Cria o formulário com os dados que o usuário enviou
        form = UserCreationForm(request.POST)
        
        # 3. Verifica se o formulário é válido
        if form.is_valid():
            # 4. Salva o novo usuário no banco de dados
            user = form.save() 
            
            # 5. Faz o login automático do novo usuário
            login(request, user)
            
            # 6. Redireciona para a página inicial
            return redirect('pagina_inicial') 
    
    # 7. Se o método for GET (usuário só visitou a página)
    else:
        # 8. Cria um formulário em branco
        form = UserCreationForm()
        
    # 9. Prepara o contexto e renderiza o template de cadastro
    contexto = {
        'form': form
    }
    return render(request, 'blog/pagina_cadastro.html', contexto)

# --- View de Logout---
def pagina_logout(request):
    # 1. Chama a função de logout do Django
    logout(request)
    
    # 2. Redireciona para a página inicial
    return redirect('pagina_inicial')

def pagina_login(request):
    # 1. Checa se o método é POST (usuário clicou em "Entrar")
    if request.method == 'POST':
    # 2. Cria o formulário com os dados que o usuário enviou
        # 3. O AuthenticationForm é especial, ele precisa do 'request'
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            # 4. Pega o usuário que foi autenticado
            user=form.get_user()
            # 5. Faz o login desse usuário na sessão 
            login(request, user)
            # 6. Redireciona para a página inicial 
            return redirect('pagina_inicial')
    # 7. Se o método for GET (usuário só visitou a página)
    else:
        # 8. Cria um formulário de login em branco
        form = AuthenticationForm()
        
    # 9. Prepara o contexto e renderiza o template de login
    contexto = {
        'form': form
    }
    return render(request, 'blog/pagina_login.html', contexto)

# ... (suas views pagina_inicial, pagina_detalhe, cadastro, login, logout) ...


# --- View para CRIAR um novo post ---
@login_required  # 1. O "ESCUDO" MÁGICO!
def pagina_criar_post(request):
    """
    Se o usuário não estiver logado, o @login_required vai
    automaticamente redirecioná-lo para a página de LOGIN.
    """
    
    # 2. Lógica de GET vs POST (igual ao cadastro/login)
    if request.method == 'POST':
        # 3. Cria o formulário com os dados enviados
        form = PostForm(request.POST)
        
        if form.is_valid():
            # 4. Não salve no banco de dados ainda!
            novo_post = form.save(commit=False) 
            
            # 5. "Carimbe" o autor logado (request.user)
            #    no campo 'autor' do post.
            novo_post.autor = request.user 
            
            # 6. Agora sim, salve o post completo no banco.
            novo_post.save() 
            
            # 7. Redireciona o usuário para a página de 
            #    detalhe DO POST que ele acabou de criar.
            return redirect('pagina_detalhe', pk=novo_post.pk) 
            
    else:
        # 8. Se for GET, apenas mostre um formulário em branco
        form = PostForm()
        
    # 9. Renderiza o template (que vamos criar)
    contexto = {
        'form': form
    }
    return render(request, 'blog/pagina_criar_post.html', contexto)

# --- View para EDITAR um post ---
@login_required # 1. "Escudo": Tem que estar logado
def pagina_editar_post(request, pk):
    # 2. Busca o post pelo 'pk', ou retorna "Página Não Encontrada"
    post = get_object_or_404(Post, pk=pk)
    
    # 3. A VERIFICAÇÃO DE PERMISSÃO MAIS IMPORTANTE:
    #    Se o autor do post NÃO FOR o usuário logado...
    if post.autor != request.user:
        # (Idealmente, mostraríamos um erro 403 - Proibido, 
        # mas por enquanto vamos só redirecionar para a inicial)
        return redirect('pagina_inicial') 

    # 4. Se a permissão estiver OK, o resto é igual ao "Criar Post",
    #    mas agora passamos o 'post' existente para dentro do formulário.
    if request.method == 'POST':
        # Passamos 'instance=post' para dizer ao form que estamos EDITANDO
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save() # Salva as mudanças no post existente
            
            # Redireciona para a página de detalhe do post editado
            return redirect('pagina_detalhe', pk=post.pk) 
    else:
        # Se for GET, mostra o formulário JÁ PREENCHIDO com os dados do post
        form = PostForm(instance=post)
        
    contexto = {
        'form': form,
        'post': post # Enviamos o post para o template
    }
    return render(request, 'blog/pagina_editar_post.html', contexto)

# --- View para DELETAR um post ---
@login_required # 1. "Escudo": Tem que estar logado
def pagina_deletar_post(request, pk):
    # 2. Busca o post pelo 'pk'
    post = get_object_or_404(Post, pk=pk)
    
    # 3. A VERIFICAÇÃO DE PERMISSÃO:
    if post.autor != request.user:
        # Se não for o autor, não pode deletar.
        return redirect('pagina_inicial') 

    # 4. Esta é a lógica de DELEÇÃO:
    #    Só deletamos se o método for POST (confirmado)
    if request.method == 'POST':
        post.delete() # O comando para deletar
        
        # Redireciona para a página inicial (o post não existe mais)
        return redirect('pagina_inicial') 
        
    # 5. Se o método for GET (a primeira visita):
    #    Apenas mostre a página de confirmação
    contexto = {
        'post': post
    }
    return render(request, 'blog/pagina_deletar_post.html', contexto)

# --- LÓGICA DA API ---
# --- O "ViewSet" para o Model Post ---

class PostViewSet(viewsets.ModelViewSet):
    """
    Esta é a "porta dos fundos" (API) para os nossos Posts.
    
    O ModelViewSet magicamente já sabe como lidar com:
    - GET /posts/ (Listar todos)
    - POST /posts/ (Criar novo)
    - GET /posts/<pk>/ (Ler um)
    - PUT /posts/<pk>/ (Editar um)
    - DELETE /posts/<pk>/ (Deletar um)
    """
    
    # 1. O "escudo" de permissão da API:
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    # 2. O "Tradutor" que ele deve usar:
    serializer_class = PostSerializer
    
    # 3. O conjunto de dados que ele deve gerenciar:
    queryset = Post.objects.all()

    # 4. O "Toque Profissional" (que fizemos no site):
    #    Quando um novo post for criado pela API, "carimbe"
    #    o autor logado (request.user) automaticamente.
    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)



