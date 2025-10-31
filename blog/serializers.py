from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    """
    O "Tradutor" que converte nosso Model 'Post'
    em dados JSON (e vice-versa).
    """
    
    # --- O Toque Profissional 💼 ---
    # Por padrão, o DRF mostraria o 'autor' apenas como o ID (ex: 1).
    # Nós queremos que ele mostre o 'username' (ex: "Bela").
    # Esta linha "substitui" o campo 'autor' para ser um
    # campo "Somente Leitura" que pega o 'username' do autor.
    autor = serializers.ReadOnlyField(source='autor.username')

    class Meta:
        model = Post
        
        # A lista de campos do nosso Model 🏛️ que
        # queremos expor na nossa "porta dos fundos" 🤖 (API).
        fields = [
            'pk', 
            'titulo', 
            'conteudo', 
            'autor',  # (Este agora é o 'username' que definimos acima)
            'data_publicacao'
        ]