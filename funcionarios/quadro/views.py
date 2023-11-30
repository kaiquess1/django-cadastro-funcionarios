from django.shortcuts import render
from .models import funcionarios
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from .forms import funcionariosForm


# Create your views here.
def index(request):
    return render(request,'quadro/index.html',{
      'quadro':funcionarios.objects.all()
      })


def view_funcionario(request,id):
  #quadro= funcionarios.objects.get(pk=id)
  return HttpResponseRedirect(reverse('index'))


def add(request):
  if request.method == 'POST':
    form = funcionariosForm(request.POST)
    if form.is_valid():
       novo_nome = form.cleaned_data['nome']
       novo_sobrenome = form.cleaned_data['sobrenome']
       novo_nascimento = form.cleaned_data['nascimento']
       novo_endereco = form.cleaned_data['endereco']
       novo_email = form.cleaned_data['email']
       novo_telefone = form.cleaned_data['telefone']
       nova_matricula = form.cleaned_data['matricula']
       novo_cargo = form.cleaned_data['cargo']
       novo_estado_civil = form.cleaned_data['estado_civil']

       novo_funcionarios = funcionarios(
        nome=novo_nome,
        sobrenome=novo_sobrenome,
        nascimento=novo_nascimento,
        email=novo_email,
        telefone=novo_telefone,
        matricula=nova_matricula,
        cargo=novo_cargo,
        estado_civil=novo_estado_civil
      )
       novo_funcionarios.save()
       return render(request, 'quadro/add.html', {
          'form': funcionariosForm(),
          'success': True
      })
  else:
    form = funcionariosForm()
  return render(request, 'quadro/add.html', {
    'form': funcionariosForm()
  })

def edit(request, id):
  if request.method == 'POST':
    quadros = funcionarios.objects.get(pk=id)
    form = funcionariosForm(request.POST, instance=quadros)
    if form.is_valid():
      form.save()
      return render(request, 'quadro/edit.html', {
        'form': form,
        'success': True
      })
  else:
    quadros = funcionarios.objects.get(pk=id)
    form = funcionariosForm(instance=quadros)
  return render(request, 'quadro/edit.html', {
    'form': form
  })


def delete(request, id):
  if request.method == 'POST':
    quadro = funcionarios.objects.get(pk=id)
    quadro.delete()
  return HttpResponseRedirect(reverse('index'))
            





