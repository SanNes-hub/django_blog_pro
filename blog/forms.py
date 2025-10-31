from django import forms
from .models import Post  # Importamos nossa planta baixa do Post

class PostForm(forms.ModelForm):
    # Esta é a "classe de configuração" interna do formulário
    class Meta:
        # 1. Dizemos qual Model ele deve usar para se construir
        model = Post
        
        # 2. Dizemos quais campos ele deve mostrar
        # (Nós não pedimos o 'autor' ou a 'data', pois serão automáticos!)
        fields = ['titulo', 'conteudo']