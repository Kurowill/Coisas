from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset()\
                                           .filter(status='publicado')



class Post (models.Model):
    STATUS = (
        ('rascunho','Rascunho'),
        ('pulbicado','Publicado'),
    )

    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length = 250) 
    autor = models.ForeignKey(User, 
                                on_delete=models.CASCADE)
    conteudo = models.TextField()
    publicado = models.DateTimeField(default=timezone.now)
    criado = models.DateTimeField(auto_now_add=True)
    auterado = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS,
                              default='rascunho')
    
    
    objects = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse('post_detail',args=[self.slug])


    def get_absolute_url_edit(self):
        return reverse('post_edit',args=[self.slug])
    

    class Meta:
        ordering = ('publicado',) #Ordenação dos posts um - muda o sentido


    def __str__(self):
        return '{}'.format(self.titulo) # Pode-se mudar o que aparece na lista de posts


