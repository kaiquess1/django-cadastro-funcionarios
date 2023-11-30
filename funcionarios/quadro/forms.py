from django import forms
from .models import funcionarios


class funcionariosForm(forms.ModelForm):
  class Meta:
    model = funcionarios
    fields = ['nome','sobrenome','nascimento','endereco','email','telefone','matricula','cargo','estado_civil']
    labels = {
      'nome': 'Nome',
      'sobrenome': 'Sobrenome',
      'nascimento':'Nascimento',
      'endereco':'Endereço',
      'email': 'Email',
      'telefone':'Telefone',
      'matricula':'Matricula',
      'cargo':'Cargo',
      'estado_civil':'Estado Civil',
    }
    widgets = {
      'nome': forms.TextInput(attrs={'class': 'form-control'}),
      'sobrenome': forms.TextInput(attrs={'class': 'form-control'}),
      'nascimento': forms.DateInput(attrs={'class': 'form-control'}),
      'endereco': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'telefone': forms.NumberInput(attrs={'class': 'form-control'}),
      'matricula': forms.NumberInput(attrs={'class': 'form-control'}),
      'cargo': forms.TextInput(attrs={'class': 'form-control'}),
      'estado_civil': forms.TextInput(attrs={'class': 'form-control'}),
    }