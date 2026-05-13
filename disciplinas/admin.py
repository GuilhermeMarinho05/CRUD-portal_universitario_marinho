from django.contrib import admin
from .models import Disciplina

# Register your models here.

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo')

    from django.contrib import admin
from rolepermissions.checkers import has_role
from .models import Disciplina


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):

    def has_view_permission(self, request, obj=None):
        return (
            has_role(request.user, 'aluno') or
            has_role(request.user, 'professor')
        )

    def has_add_permission(self, request):
        return has_role(request.user, 'professor')

    def has_change_permission(self, request, obj=None):
        return has_role(request.user, 'professor')

    def has_delete_permission(self, request, obj=None):
        return has_role(request.user, 'professor')