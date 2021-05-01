from django.contrib import admin
from .models import Post

# Register your models here.

# Modificações da páginma de Admin


@admin.register(Post)


class PostAdmin(admin.ModelAdmin): 
    list_display = ('titulo', 'autor','publicado','status','pk')# insere no campo de posts as informações passadas na tupla
    list_filter = ('status','criado','publicado','autor') # insere os campos do filtro de pesquisa
    raw_id_fields = ('autor',)
    date_hierarchy = 'publicado' #Insere um ahierarquia para os intens publicados
    search_fields = ('titulo', 'conteudo') # campos de busca
    prepopulated_fields = {'slug':('titulo',)} # auto insere um slug com base nno título

