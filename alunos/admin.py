from django.contrib import admin
from .models import Aluno

# Register your models here

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'curso', 'user')
    search_fields = ('nome', 'matricula', 'curso', 'user__username')
    filter_horizontal = ('disciplinas',)
