from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required(login_url='/auth/login/')
def home(request):
    # Renderizar a base.html e ver se o botao de sair está tudo certo
    return render(request, 'home.html')