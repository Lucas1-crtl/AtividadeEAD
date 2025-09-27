from django.shortcuts import render , redirect
from .forms import FuncionarioForm, EPIForm
from .models import Funcionario, EPI
from .forms import RelatorioForm

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
    epis = EPI.objects.select_related('funcionario').all()
    return render(request, 'listar_epi.html', {'epis': epis})

def relatorio_epi(request):
    query_nome = request.GET.get("colaborador", "").strip()
    query_epi = request.GET.get("epi", "").strip()
    query_status = request.GET.get("status", "").strip()

    epis = EPI.objects.select_related("funcionario").all()

    if query_nome:
        epis = epis.filter(funcionario__nome_completo__icontains=query_nome)

    if query_epi:
        epis = epis.filter(nome__icontains=query_epi)

    if query_status:
        epis = epis.filter(status=query_status)

    return render(request, "relatorio_epi.html", {"epis": epis})