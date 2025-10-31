"""
URL configuration for blog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, include
from rest_framework import routers
from blog import views as blog_views

# Criar o roteador para a API e registra o viewset
router = routers.DefaultRouter()

# Registre o 'PostViewSet' no Roteador
# 1. 'posts': O "apelido" da nossa API (vai criar a URL /api/posts/)
# 2. blog_views.PostViewSet: A lógica ⚙️ que ele deve usar
router.register(r'posts', blog_views.PostViewSet, basename='post')

urlpatterns = [
    
    #Os bastidores(o admin)
    path('admin/', admin.site.urls),
    #A porta da frente(site)
    path('', include('blog.urls')), 

    # A "porta dos fundos" (A NOVA API)
    # Qualquer URL que comece com /api/ será
    # gerenciada pelo 'router' do DRF.
    path('api/', include(router.urls)),
]

