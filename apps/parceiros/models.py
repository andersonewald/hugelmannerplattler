from django.db import models

class Patrocinador(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Patrocinador")
    logo = models.ImageField(upload_to='logos_patrocinadores/', verbose_name="Logotipo")
    site_url = models.URLField(blank=True, null=True, verbose_name="Site do Patrocinador")
    ordem = models.IntegerField(default=0, verbose_name="Ordem de Exibição")

    def __str__(self):
        return self.nome
