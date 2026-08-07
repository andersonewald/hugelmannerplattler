from django.contrib import admin
from .models import Integrante, Evento, Produto, Parceiro, FotoGaleria # 🌟 Importado FotoGaleria

# 👤 Registro dos Integrantes
@admin.register(Integrante)
class IntegranteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'instagram', 'no_grupo_desde')
    search_fields = ('nome', 'instagram')


# 📅 Registro da Agenda (Eventos)
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'exibir_dias', 'cidade', 'horario')
    list_filter = ('cidade', 'data_inicio')
    search_fields = ('nome', 'local', 'cidade')

    def exibir_dias(self, obj):
        if obj.data_fim and obj.data_inicio != obj.data_fim:
            return f"De {obj.data_inicio.strftime('%d/%m')} a {obj.data_fim.strftime('%d/%m/%Y')}"
        return obj.data_inicio.strftime('%d/%m/%Y')
    
    exibir_dias.short_description = "Data / Período"


# 🛍️ Registro da Hügel Store (Produtos)
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'disponivel', 'criado_em')
    list_filter = ('disponivel', 'criado_em')
    search_fields = ('nome', 'descricao')
    list_editable = ('preco', 'disponivel')


# 🤝 Registro dos Parceiros e Apoiadores
@admin.register(Parceiro)
class ParceiroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'ordem')
    list_editable = ('ativo', 'ordem')
    search_fields = ('nome',)


# 📸 Registro da Galeria de Fotos
@admin.register(FotoGaleria)
class FotoGaleriaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'criado_em')
    search_fields = ('titulo',)