from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Tarefa

@login_required(login_url='/auth/login/')
def home(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'home.html', {'tarefas':tarefas})

@login_required(login_url='/auth/login/')
def criar_tarefa(request):
    if request.method == 'GET':
        return render(request, 'criar_tarefa.html')
    #elif request.method == 'POST':
    #    pass