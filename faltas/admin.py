from django.contrib import admin
from .models import Falta, Chamada, PresencaChamada, LimiteFaltas


@admin.register(Falta)
class FaltaAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'disciplina', 'data', 'justificada', 'criado_em')
    list_filter = ('justificada', 'data', 'disciplina')
    search_fields = ('aluno__nome', 'disciplina__nome')
    date_hierarchy = 'data'  
    ordering = ('-data',)


@admin.register(Chamada)
class ChamadaAdmin(admin.ModelAdmin):
    list_display = ('disciplina', 'data', 'professor', 'realizado_em')
    list_filter = ('disciplina', 'data')
    search_fields = ('disciplina__nome', 'professor__username')
    date_hierarchy = 'data'
    ordering = ('-data',)


@admin.register(PresencaChamada)
class PresencaChamadaAdmin(admin.ModelAdmin):
    list_display = ('chamada', 'aluno', 'presente')
    list_filter = ('presente', 'chamada__disciplina')
    search_fields = ('aluno__nome', 'chamada__disciplina__nome')
    raw_id_fields = ('chamada', 'aluno')  

@admin.register(LimiteFaltas)
class LimiteFaltasAdmin(admin.ModelAdmin):
    list_display = ('disciplina', 'carga_horaria_total', 'percentual_maximo', 'faltas_maximas')
    list_filter = ('disciplina',)
    search_fields = ('disciplina__nome',)
    readonly_fields = ('faltas_maximas',)  