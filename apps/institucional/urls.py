from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('o-grupo/', views.o_grupo, name='o_grupo'),
    path('integrantes/', views.integrantes, name='integrantes'),
    path('contato/', views.contato, name='contato'),
    # 🌟 A LINHA QUE FALTAVA:
    path('store/', views.store, name='store'),
]