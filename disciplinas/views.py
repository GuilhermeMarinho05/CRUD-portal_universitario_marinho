from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from .models import Disciplina
from .forms import DisciplinaForm


def lista_disciplinas(request):

    disciplinas = Disciplina.objects.all()

    return render(
        request,
        'disciplinas/lista.html',
        {
            'disciplinas': disciplinas
        }
    )


def criar_disciplina(request):

    form = DisciplinaForm(
        request.POST or None
    )

    if form.is_valid():

        form.save()

        return redirect(
            'lista_disciplinas'
        )

    return render(
        request,
        'disciplinas/form.html',
        {
            'form': form
        }
    )


def editar_disciplina(request, id):

    disciplina = get_object_or_404(
        Disciplina,
        id=id
    )

    form = DisciplinaForm(
        request.POST or None,
        instance=disciplina
    )

    if form.is_valid():

        form.save()

        return redirect(
            'lista_disciplinas'
        )

    return render(
        request,
        'disciplinas/form.html',
        {
            'form': form
        }
    )


def excluir_disciplina(request, id):

    disciplina = get_object_or_404(
        Disciplina,
        id=id
    )

    if request.method == 'POST':

        disciplina.delete()

        return redirect(
            'lista_disciplinas'
        )

    return render(
        request,
        'disciplinas/confirmar_exclusao.html',
        {
            'disciplina': disciplina
        }
    )