from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

# 🌟 Importa os modelos do banco de dados
from .models import Integrante, Produto, Parceiro, FotoGaleria # 🌟 Importado FotoGaleria

# 🏠 HOME: Busca os parceiros ativos e as fotos da galeria
def home(request):
    parceiros = Parceiro.objects.filter(ativo=True)
    fotos = FotoGaleria.objects.all()[:12] # Busca as 12 fotos mais recentes
    return render(request, "home.html", {
        'parceiros': parceiros,
        'fotos': fotos,
    })

def o_grupo(request):
    return render(request, "o_grupo.html")

# 🛍️ HÜGEL STORE: Busca produtos disponíveis no banco
def store(request):
    produtos = Produto.objects.filter(disponivel=True)
    return render(request, 'store.html', {'produtos': produtos})

# 👤 INTEGRANTES: Busca integrantes cadastrados no banco
def integrantes(request):
    todos_integrantes = Integrante.objects.all()
    return render(request, 'integrantes.html', {'integrantes': todos_integrantes})

# 📞 CONTATO: Envio de e-mails
def contato(request):
    if request.method == 'POST':
        nome = request.POST.get('name')
        email_cliente = request.POST.get('email')
        assunto = request.POST.get('subject')
        mensagem_corpo = request.POST.get('message')
        
        conteudo_email = f"""
        Nova mensagem recebida pelo site do Hügel Männer Plattler!
        
        Nome/Organização: {nome}
        E-mail de contato: {email_cliente}
        Assunto: {assunto}
        
        Mensagem:
        {mensagem_corpo}
        """
        
        try:
            send_mail(
                subject=f"[Site Contato] {assunto}",
                message=conteudo_email,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['hugelmannerplattler@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'Sua mensagem foi enviada com sucesso! Responderemos em breve.')
            return redirect('contato')
            
        except Exception as e:
            messages.error(request, 'Ocorreu um erro ao enviar a mensagem. Tente novamente mais tarde.')
            
    return render(request, 'contato.html')