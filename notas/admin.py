from django.contrib import admin
from .models import Nota 

# Register your models here.

@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('aluno','disciplina','valor')
    search_fields = ('aluno__nome','disciplina_nome')
    list_filter = ('disciplina',)