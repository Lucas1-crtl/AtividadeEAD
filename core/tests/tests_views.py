import pytest
from django.urls import reverse
from core.models import Funcionario, EPI


@pytest.mark.django_db
def test_view_home(client):
    """Testa se a página inicial carrega corretamente."""
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200
    assert 'tela.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_cadastrar_funcionario_get(client):
    """Testa se a página de cadastro de funcionário é exibida."""
    url = reverse('cadastrar_funcionario')
    response = client.get(url)
    assert response.status_code == 200
    assert 'my_db.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_cadastrar_funcionario_post(client):
    """Testa se o formulário de funcionário salva corretamente."""
    url = reverse('cadastrar_funcionario')
    data = {
        'nome_completo': 'João Teste',
        'matricula': '123',
        'setor': 'Engenharia',
        'cargo': 'Técnico',
        'telefone': '(11) 99999-9999',
        'email': 'joao@teste.com'
    }
    response = client.post(url, data)
    assert response.status_code == 302  # redireciona após salvar
    assert Funcionario.objects.filter(nome_completo='João Teste').exists()


@pytest.mark.django_db
def test_listar_funcionarios_view(client):
    """Testa se a listagem de funcionários é renderizada corretamente."""
    Funcionario.objects.create(nome_completo='Maria da Silva')
    url = reverse('listar_funcionarios')
    response = client.get(url)
    assert response.status_code == 200
    assert 'Maria da Silva' in response.content.decode()


@pytest.mark.django_db
def test_cadastrar_epi_post(client):
    """Testa se o cadastro de EPI funciona."""
    funcionario = Funcionario.objects.create(nome_completo='Carlos Souza')
    url = reverse('cadastrar_epi')
    data = {
        'nome': 'Capacete',
        'descricao': 'Capacete de segurança',
        'status': 'fornecido',
        'funcionario': funcionario.id
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert EPI.objects.filter(nome='Capacete').exists()


@pytest.mark.django_db
def test_relatorio_epi_filtra_dados(client):
    """Testa o filtro de relatório por nome e status."""
    func = Funcionario.objects.create(nome_completo='Lucas Tester')
    EPI.objects.create(nome='Botina', funcionario=func, status='em uso')

    url = reverse('relatorio_epi')
    response = client.get(url, {'colaborador': 'Lucas', 'status': 'em uso'})
    assert response.status_code == 200
    content = response.content.decode()
    assert 'Botina' in content
    assert 'Lucas Tester' in content
