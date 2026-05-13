from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Aluno
from .forms import AlunoForm
from faltas.models import Falta
from notas.models import Nota
from users.access import is_aluno, is_professor, role_required


@role_required('professor')
def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/lista.html', {'alunos': alunos})


@role_required('professor')
def criar_aluno(request):
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_alunos')
    return render(request, 'alunos/form.html', {'form': form})


@role_required('professor')
def editar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    form = AlunoForm(request.POST or None, instance=aluno)
    if form.is_valid():
        form.save()
        return redirect('lista_alunos')
    return render(request, 'alunos/form.html', {'form': form})


@role_required('professor')
def excluir_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    if request.method == 'POST':
        aluno.delete()
        return redirect('lista_alunos')
    return render(request, 'alunos/confirmar_exclusao.html', {'aluno': aluno})


@login_required
def dashboard_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)

    if is_aluno(request.user) and aluno.user_id != request.user.id:
        raise PermissionDenied
    
    notas = Nota.objects.filter(aluno=aluno)
    faltas = Falta.objects.filter(aluno=aluno)
    
    if notas.exists():
        soma_medias = sum([nota.media() for nota in notas])
        media_geral = soma_medias / notas.count()
    else:
        media_geral = 0
    
    context = {
        'aluno': aluno,
        'media_geral': round(media_geral, 1),
        'disciplinas_cursando': notas.count(),
        'total_faltas': faltas.count(),
        'proxima_atividade': 'Verifique o calendário acadêmico',
    }
    
    return render(request, 'alunos/dashboard.html', context)


@login_required
def minha_area(request):
    if is_professor(request.user):
        return redirect('lista_alunos')

    if not is_aluno(request.user):
        raise PermissionDenied

    aluno = Aluno.objects.filter(user=request.user).prefetch_related('disciplinas').first()
    notas = Nota.objects.none()
    faltas = Falta.objects.none()
    disciplinas = []
    media_geral = 0

    if aluno:
        notas = Nota.objects.filter(aluno=aluno).select_related('disciplina')
        faltas = Falta.objects.filter(aluno=aluno).select_related('disciplina')
        disciplinas = list(aluno.disciplinas.all())

        if not disciplinas:
            disciplinas = [nota.disciplina for nota in notas]

        if notas.exists():
            media_geral = round(
                sum(nota.media() for nota in notas) / notas.count(),
                1
            )

    context = {
        'aluno': aluno,
        'notas': notas,
        'faltas': faltas,
        'disciplinas': disciplinas,
        'media_geral': media_geral,
    }

    return render(request, 'alunos/minha_area.html', context)
