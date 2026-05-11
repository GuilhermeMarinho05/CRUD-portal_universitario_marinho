from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno
from .forms import AlunoForm
from notas.models import Nota


def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/lista.html', {'alunos': alunos})


def criar_aluno(request):
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_alunos')
    return render(request, 'alunos/form.html', {'form': form})


def editar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    form = AlunoForm(request.POST or None, instance=aluno)
    if form.is_valid():
        form.save()
        return redirect('lista_alunos')
    return render(request, 'alunos/form.html', {'form': form})


def excluir_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    if request.method == 'POST':
        aluno.delete()
        return redirect('lista_alunos')
    return render(request, 'alunos/confirmar_exclusao.html', {'aluno': aluno})


def dashboard_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    
    notas = Nota.objects.filter(aluno=aluno)
    
    if notas.exists():
        soma_medias = sum([nota.media() for nota in notas])
        media_geral = soma_medias / notas.count()
    else:
        media_geral = 0
    
    context = {
        'aluno': aluno,
        'media_geral': round(media_geral, 1),
        'disciplinas_cursando': notas.count(),
        'total_faltas': 'Não registrado',
        'proxima_atividade': 'Verifique o calendário acadêmico',
    }
    
    return render(request, 'alunos/dashboard.html', context)