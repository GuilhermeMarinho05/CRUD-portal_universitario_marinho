from django.shortcuts import render, redirect, get_object_or_404
from .models import Nota
from .forms import NotaForm


# LISTAR
def lista_notas(request):
    notas = Nota.objects.all()
    return render(request, 'notas/lista.html', {'notas': notas})


# CRIAR
def criar_nota(request):
    form = NotaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_notas')

    return render(request, 'notas/form.html', {'form': form})


# EDITAR
def editar_nota(request, id):
    nota = get_object_or_404(Nota, id=id)
    form = NotaForm(request.POST or None, instance=nota)

    if form.is_valid():
        form.save()
        return redirect('lista_notas')

    return render(request, 'notas/form.html', {'form': form})


# DELETAR
def deletar_nota(request, id):
    nota = get_object_or_404(Nota, id=id)

    if request.method == 'POST':
        nota.delete()
        return redirect('lista_notas')

    return render(request, 'notas/confirmar_exclusao.html', {'nota': nota})
