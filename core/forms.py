from django import forms
from .models import Funcionario

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
            'observacoes'
        ]
