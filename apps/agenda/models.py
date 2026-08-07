from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome do Evento")
    data = models.DateField(verbose_name="Data do Evento")
    horario = models.TimeField(verbose_name="Horário")
    local = models.CharField(max_length=255, verbose_name="Local/Cidade")
    link_ingresso = models.URLField(blank=True, null=True, verbose_name="Link para Informações/Ingresso")
    descricao = models.TextField(blank=True, verbose_name="Descrição Breve")

    def __str__(self):
        return f"{self.nome} - {self.data.strftime('%d/%m/%Y')}"
