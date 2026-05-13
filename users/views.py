from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from .access import is_aluno


@login_required
def portal_redirect(request):
    if is_aluno(request.user):
        return redirect('minha_area')

    return redirect('lista_alunos')
