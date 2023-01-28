from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Tarefa
from django.contrib import messages

@login_required(login_url='/auth/login/')
def home(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'home.html', {'tarefas':tarefas})

@login_required(login_url='/auth/login/')
def criar_tarefa(request):
    if request.method == 'GET':
        return render(request, 'criar_tarefa.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome_tarefa')
        data = request.POST.get('data_tarefa')
        feita = request.POST.get('feita_tarefa')
        if feita == None:
            feita = 0
        else:
            feita = 1
        
        if len(nome.strip()) == 0 or len(data.strip()) == 0:
            messages.add_message(request, messages.constants.ERROR, 'Nome ou Data invalidos')
            return redirect('/todo_list/criar_tarefa/')
        else:
            tarefa = Tarefa(nome=nome, data=data, esta_feita=feita)
            tarefa.save()
            messages.add_message(request, messages.constants.SUCCESS, 'Tarefa Criada com sucesso')
            return redirect('/todo_list/home/')

@login_required(login_url='/auth/login/')
def detalhes_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    return render(request, 'detalhes_tarefa.html', {'tarefa':tarefa})

@login_required(login_url='/auth/login/')
def excluir_tarefa(request, id):
    pass