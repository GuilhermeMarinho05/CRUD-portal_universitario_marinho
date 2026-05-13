from rolepermissions.roles import AbstractUserRole

from rolepermissions.roles import AbstractUserRole

class Aluno(AbstractUserRole):
    available_permissions = {
        'view_notas': True,
        'view_faltas': True,
        'view_disciplinas': True,
    }

class Professor(AbstractUserRole):
    available_permissions = {
        'add_notas': True,
        'change_notas': True,
        'delete_notas': True,
        'view_notas': True,

        'add_faltas': True,
        'change_faltas': True,
        'delete_faltas': True,
        'view_faltas': True,

        'add_disciplinas': True,
        'change_disciplinas': True,
        'delete_disciplinas': True,
        'view_disciplinas': True,
    }