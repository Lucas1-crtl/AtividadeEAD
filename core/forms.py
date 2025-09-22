from django import forms
from .models import Funcionario, EPI

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = [
            'nome_completo',
            'matricula',
            'setor',
            'cargo',
            'telefone',
            'email',
            'epis_fornecidos',
            'observacoes',
        ]

class EPIForm(forms.ModelForm):
    class Meta:
        model = EPI
        fields = [
            'nome',
            'descricao',
            'status',
            'funcionario',
        ]
