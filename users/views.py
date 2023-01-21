from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as lgn
from django.contrib.auth import logout as lgt

def cadastrar(request):
    if request.method == 'GET':
        status = request.GET.get('status')
        return render(request, 'cadastrar.html', {'status':status})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        if len(nome.strip()) == 0 or len(email.strip()) == 0:
            messages.add_message(request, messages.constants.ERROR, 'Nome ou E-mail invalidos.')
            return redirect('/auth/cadastrar/')

        if len(senha.strip()) < 8:
            messages.add_message(request, messages.constants.ERROR, 'Senha invalida ou muito curta.')
            return redirect('/auth/cadastrar/')

        else:
            try:
                user = User.objects.create_user(username=nome, email=email, password=senha)
                user.save()
                messages.add_message(request, messages.constants.SUCCESS, 'Conta criada, agora faça LOGIN.')
                return redirect('/auth/cadastrar/')
            except:
                messages.add_message(request, messages.constants.ERROR, 'Erro na hora de cadastrar.')
                return redirect('/auth/cadastrar/?status=3')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        user = authenticate(username=nome, password=senha)
        if user is not None:
            lgn(request, user)
            return redirect('/todo_list/home/')
        else:
            messages.add_message(request, messages.constants.ERROR, 'Nome ou senha invalidos.')
            return redirect('/auth/login')
    
def logout(request):
    lgt(request)
    messages.add_message(request, messages.constants.WARNING, 'Conta DESVINCULADA, faça login se quiser.')
    return redirect('/auth/login/')