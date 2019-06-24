from django.shortcuts import render, redirect, get_object_or_404
from .models import Filme
from .forms import FilmeForm
from django.views.generic import UpdateView
# Create your views here.


def criar_filmes(request):
    if request.method == "POST":
        form = FilmeForm(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('/filmeteste')
        else:
            print("não é válido")
    else:
        form = FilmeForm()

    filme = Filme.objects.all()
    form = FilmeForm()
    args = {'filmes': filme, 'form': form}
    return render(request, 'formulario.html', args)


def pagina_inicial(request):
    if request.method == "GET":
        filmes = Filme.objects.all()
        return render(request, 'index.html', {"filmes": filmes})


def filme_update(request, pk, template_name='edit.html'):
    filme = get_object_or_404(Filme, pk=pk)
    form = FilmeForm(request.POST or None, instance=filme)
    if form.is_valid():
        form.save()
        return redirect('/filmeteste')
    return render(request, template_name, {'form': form})


def filme_delete(request, pk, template_name='delete.html'):
    filme = get_object_or_404(Filme, pk=pk)
    if request.method == 'POST':
        filme.delete()
        return redirect('/filmeteste')
    return render(request, template_name, {'object': filme})


def filme_list(request, template_name='filme_list.html'):
    filme = Filme.objects.all()  # pega todos os filmes
    data = {}
    data['object_list'] = filme
    return render(request, template_name, {'object_list': filme})


def quem_somos(request):
    return render(request, "quem_somos.html")
