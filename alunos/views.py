from django.shortcuts import render, redirect
from .models import Aluno
from .forms import AlunoForm
from django.shortcuts import get_object_or_404


def lista_alunos(request):

    alunos = Aluno.objects.all()

    return render(request, 'alunos/lista.html', {
        'alunos': alunos
    })


def criar_aluno(request):

    form = AlunoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_alunos')

    return render(request, 'alunos/form.html', {
        'form': form
    })

def editar_aluno(request, id):

    aluno = get_object_or_404(
        Aluno,
        id=id
    )

    form = AlunoForm(
        request.POST or None,
        instance=aluno
    )

    if form.is_valid():
        form.save()
        return redirect('lista_alunos')

    return render(request, 'alunos/form.html', {
        'form': form
    })

def excluir_aluno(request, id):

    aluno = get_object_or_404(
        Aluno,
        id=id
    )

    if request.method == 'POST':

        aluno.delete()

        return redirect('lista_alunos')

    return render(request, 'alunos/confirmar_exclusao.html', {
        'aluno': aluno
    })

def excluir_aluno(request, id):

    aluno = get_object_or_404(
        Aluno,
        id=id
    )

    if request.method == 'POST':

        aluno.delete()

        return redirect('lista_alunos')

    return render(
        request,
        'alunos/confirmar_exclusao.html',
        {
            'aluno': aluno
        }
    )