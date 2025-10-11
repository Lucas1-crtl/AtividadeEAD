import pytest
from core.models import Funcionario, EPI

@pytest.mark.django_db
def test_criacao_funcionario():
    funcionario = Funcionario.objects.create(
        nome_completo="Lucas Schatz",
        matricula="12345",
        setor="Engenharia Civil",
        cargo="Engenheiro",
        telefone="(11) 99999-9999",
        email="lucas@example.com",
        epis_fornecidos="Capacete, Botina, Colete",
        observacoes="Funcionário regularizado"
    )

    assert funcionario.id is not None
    assert str(funcionario) == "Lucas Schatz"
    assert funcionario.setor == "Engenharia Civil"


@pytest.mark.django_db
def test_criacao_epi_relacionado_a_funcionario():
    funcionario = Funcionario.objects.create(nome_completo="Lucas Schatz")
    epi = EPI.objects.create(
        nome="Capacete",
        descricao="Capacete de segurança classe A",
        status="fornecido",
        funcionario=funcionario
    )

    assert epi.id is not None
    assert str(epi) == "Capacete - Fornecido"
    assert epi.funcionario.nome_completo == "Lucas Schatz"
    assert epi.status == "fornecido"


@pytest.mark.django_db
def test_ultima_atualizacao_auto():
    funcionario = Funcionario.objects.create(nome_completo="Maria Silva")
    epi = EPI.objects.create(nome="Botina", funcionario=funcionario)
    
    data_inicial = epi.ultima_atualizacao
    epi.status = "em uso"
    epi.save()

    # Verifica se o campo foi atualizado após salvar novamente
    assert epi.ultima_atualizacao > data_inicial


