from django.contrib import admin
from .models import Receita

# Register your models here.

#Sem essa linha, não mostra no admin do Django a minha receita
admin.site.register(Receita)
