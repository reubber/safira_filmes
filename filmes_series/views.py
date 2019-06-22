from django.shortcuts import render, redirect
from .models import Filme
from .forms import FilmeForm
from django.core.files.storage import FileSystemStorage
# Create your views here.


def criar_filmes(request):
    if request.method == "POST":
        form = FilmeForm(request.POST, request.FILES)
        # myfile = request.FILES['id_cover']
        # fs = FileSystemStorage()
        if form.is_valid():
            print(form)
            form.save()
            return redirect('/')
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
         return render(request, 'index.html', {"filmes": filmes} )

