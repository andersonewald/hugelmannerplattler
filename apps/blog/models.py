from django.db import models
from django.utils.text import slugify

class Post(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    slug = models.SlugField(unique=True, blank=True)
    conteudo = models.TextField(verbose_name="Conteúdo da Publicação")
    imagem = models.ImageField(upload_to='blog_fotos/', verbose_name="Imagem de Destaque")
    texto_descritivo_imagem = models.CharField(max_length=255, verbose_name="Texto Alternativo (Acessibilidade/SEO)")
    data_publicacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Publicação")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo
