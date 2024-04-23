from django import forms
from .models import Cliente, Funcionario

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'username', 'email', 'senha', 'cpf', 'contato']
        widgets = {
            'senha': forms.PasswordInput(),
        }

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'email_empresa', 'senha', 'username']
        widgets = {
            'senha': forms.PasswordInput(),
        }
