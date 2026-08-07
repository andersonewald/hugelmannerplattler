from django.shortcuts import render
from datetime import date
# 🌟 MUDANÇA AQUI: Buscando o Evento correto de dentro do app institucional!
from apps.institucional.models import Evento 

def agenda(request):
    # 🌟 Buscando os eventos futuros filtrados pelo campo real 'data_inicio'
    eventos_futuros = Evento.objects.filter(data_inicio__gte=date.today()).order_by("data_inicio")
    
    return render(request, "agenda.html", {"eventos": eventos_futuros})