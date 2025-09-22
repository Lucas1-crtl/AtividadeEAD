from django.shortcuts import render , redirect
from .forms import FuncionarioForm, EPIForm
from .models import Funcionario, EPI

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

def cadastrar_epi(request):
    if request.method == "POST":
        form = EPIForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_epi')
    else:
        form = EPIForm()
    return render(request, 'cadastrar_epi.html', {'form': form})

def listar_epi(request):
    epis = EPI.objects.all()
    return render(request, 'listar_epi.html', {'epis': epis})