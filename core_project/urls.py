from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# 🌟 Adicionado 'store' no import abaixo:
from apps.institucional.views import home, o_grupo, contato, integrantes, store
from apps.agenda.views import agenda
from apps.blog.views import lista_posts, detalhe_post

urlpatterns = [
    # Rota da Área Administrativa
    path('admin/', admin.site.urls),
    
    # Rota Nativa para Troca de Idiomas (Bandeirinhas)
    path('i18n/', include('django.conf.urls.i18n')),
    
    # Rotas do Site
    path('', home, name='home'),
    path('o-grupo/', o_grupo, name='o_grupo'),
    path('agenda/', agenda, name='agenda'),
    path('blog/', lista_posts, name='lista_posts'),
    path('blog/<slug:slug>/', detalhe_post, name='detalhe_post'),
    path('contato/', contato, name='contato'),
    path('integrantes/', integrantes, name='integrantes'),
    # 🌟 Corrigido de 'views.store' para apenas 'store':
    path('store/', store, name='store'),
]

# Ativa o carregamento de imagens de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)