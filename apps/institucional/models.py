import os
import uuid
from django.db import models
from django.utils.text import slugify

# 🌟 FUNÇÃO DE UPLOAD: FOTOS DOS INTEGRANTES
def caminho_foto_integrante(instance, filename):
    extensao = filename.split('.')[-1]
    nome_limpo = slugify(instance.nome)
    return f'integrantes/{nome_limpo}.{extensao}'

# 🌟 FUNÇÃO DE UPLOAD: CARDS DA AGENDA
def caminho_card_agenda(instance, filename):
    extensao = filename.split('.')[-1]
    nome_limpo = slugify(instance.nome)
    return f'agenda/{nome_limpo}.{extensao}'

# 🌟 FUNÇÃO DE UPLOAD: FOTOS DOS PRODUTOS
def caminho_foto_produto(instance, filename):
    extensao = filename.split('.')[-1]
    nome_limpo = slugify(instance.nome)
    return f'produtos/{nome_limpo}.{extensao}'

# 🌟 FUNÇÃO DE UPLOAD: LOGOS DOS PARCEIROS
def caminho_logo_parceiro(instance, filename):
    extensao = filename.split('.')[-1]
    nome_limpo = slugify(instance.nome)
    return f'parceiros/{nome_limpo}.{extensao}'

# 🌟 FUNÇÃO DE UPLOAD: GALERIA DE FOTOS
def caminho_foto_galeria(instance, filename):
    extensao = filename.split('.')[-1]
    codigo_unico = uuid.uuid4().hex[:8]
    return f'galeria/{codigo_unico}.{extensao}'


# 🛍️ MODELO: PRODUTO (HÜGEL STORE)
class Produto(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome do Produto")
    descricao = models.TextField(verbose_name="Descrição do Produto")
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço (R$)")
    imagem = models.ImageField(upload_to=caminho_foto_produto, verbose_name="Foto do Produto")
    disponivel = models.BooleanField(default=True, verbose_name="Disponível para Venda")
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['-criado_em']

    def __str__(self):
        return f"{self.nome} - R$ {self.preco}"


# 👤 MODELO: INTEGRANTES
class Integrante(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome Completo")
    instagram = models.CharField(max_length=50, help_text="Apenas o @perfil (Ex: hugelmannerplattler)", verbose_name="Instagram")
    no_grupo_desde = models.CharField(max_length=50, help_text="Ex: Julho de 2015", verbose_name="No grupo desde")
    foto = models.ImageField(upload_to=caminho_foto_integrante, verbose_name="Foto do Integrante")

    class Meta:
        verbose_name = "Integrante"
        verbose_name_plural = "Integrantes"
        ordering = ['nome']

    def __str__(self):
        return self.nome


# 📅 MODELO: EVENTOS (AGENDA)
class Evento(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome do Evento")
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_fim = models.DateField(blank=True, null=True, help_text="Preencha apenas se o evento durar mais de um dia", verbose_name="Data de Término")
    horario = models.CharField(max_length=50, help_text="Ex: 19:30h ou Durante o dia", verbose_name="Horário")
    local = models.CharField(max_length=150, help_text="Ex: Praça Central", verbose_name="Local da Apresentação")
    cidade = models.CharField(max_length=100, help_text="Ex: Domingos Martins - ES", verbose_name="Cidade / Estado")
    descricao = models.TextField(blank=True, verbose_name="Breve Descrição do Evento")
    card_divulgacao = models.ImageField(upload_to=caminho_card_agenda, blank=True, null=True, verbose_name="Card de Divulgação (Imagem)")
    link_ingresso = models.URLField(blank=True, null=True, help_text="Link para compra ou mais informações (se houver)", verbose_name="Link Externo / Ingresso")

    class Meta:
        verbose_name = "Evento da Agenda"
        verbose_name_plural = "Eventos da Agenda"
        ordering = ['data_inicio']

    def __str__(self):
        return f"{self.nome} ({self.data_inicio.strftime('%d/%m/%Y')})"


# 🤝 MODELO: PARCEIROS E APOIADORES
class Parceiro(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome do Parceiro / Apoiador")
    logo = models.ImageField(upload_to=caminho_logo_parceiro, verbose_name="Logo / Marca")
    site_url = models.URLField(blank=True, null=True, help_text="Link para o site do parceiro (opcional)", verbose_name="Link Externo")
    ativo = models.BooleanField(default=True, verbose_name="Exibir no site")
    ordem = models.IntegerField(default=0, help_text="Menor número aparece primeiro", verbose_name="Ordem de exibição")

    class Meta:
        verbose_name = "Parceiro / Apoiador"
        verbose_name_plural = "Parceiros e Apoiadores"
        ordering = ['ordem', 'nome']

    def __str__(self):
        return self.nome


# 📸 MODELO: GALERIA DE FOTOS
class FotoGaleria(models.Model):
    titulo = models.CharField(max_length=150, verbose_name="Título / Legenda")
    imagem = models.ImageField(upload_to=caminho_foto_galeria, verbose_name="Foto")
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name="Data de Upload")

    class Meta:
        verbose_name = "Foto da Galeria"
        verbose_name_plural = "Galeria de Fotos"
        ordering = ['-criado_em']  # Fotos mais recentes sempre primeiro

    def __str__(self):
        return self.titulo