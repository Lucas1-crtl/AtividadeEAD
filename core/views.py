from django.shortcuts import render , redirect
from .forms import FuncionarioForm
from .models import Funcionario

# Create your views here.

def home(request) :
    return render(request, "tela.html")

#def home(request):
   # return redirect('cadastrar_funcionario')

def cadastrar_funcionario(request):
    if request.method == "POST":
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_funcionarios')
    else:
        form = FuncionarioForm()
    return render(request, 'my_db.html', {'form': form})

def lista_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'listar_funcionarios.html', {'funcionarios': funcionarios})

