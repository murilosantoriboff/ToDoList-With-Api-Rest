from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required(login_url='/auth/login/')
def home(request):
    # Mandar para home os dados da model Tarefa
    return render(request, 'home.html')