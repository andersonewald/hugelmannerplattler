from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao')
    prepopulated_fields = {'slug': ('titulo',)}
    search_fields = ('titulo', 'conteudo')
