from django.db import models

class Funcionario(models.Model):
    nome_completo = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, blank=True, null=True)
    setor = models.CharField(max_length=100, blank=True, null=True)
    cargo = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    epis_fornecidos = models.TextField(blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome_completo


class EPI(models.Model):
    STATUS_CHOICES = [
        ('fornecido', 'Fornecido'),
        ('em_uso', 'Em uso'),
        ('emprestado', 'Emprestado'),
        ('devolvido', 'Devolvido'),
        ('danificado', 'Danificado'),
        ('perdido', 'Perdido'),
    ]

    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='fornecido')
    funcionario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True, blank=True)
    ultima_atualizacao = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.nome} - {self.get_status_display()}"
