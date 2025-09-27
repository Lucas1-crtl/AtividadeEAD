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

class RelatorioForm(forms.Form):
    colaborador = forms.CharField(
        required=False, 
        label="colaborador", 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    equipamento = forms.CharField(
        required=False, 
        label="equipamento", 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    status = forms.ChoiceField(
        required=False, 
        label="status",
        choices=[('', '--- Todos ---')] + EPI.STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )