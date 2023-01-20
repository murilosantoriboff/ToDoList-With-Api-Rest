from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

def cadastrar(request):
    if request.method == 'GET':
        status = request.GET.get('status')
        return render(request, 'cadastrar.html', {'status':status})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        if len(nome.strip()) == 0 or len(email.strip()) == 0:
            messages.add_message(request, messages.constants.ERROR, 'Nome ou E-mail invalidos')
            return redirect('/auth/cadastrar/')

        if len(senha.strip()) < 8:
            messages.add_message(request, messages.constants.ERROR, 'Senha invalida ou muito curta')
            return redirect('/auth/cadastrar/')

        else:
            try:
                user = User.objects.create_user(username=nome, email=email, password=senha)
                user.save()
                messages.add_message(request, messages.constants.SUCCESS, 'Conta criada, agora faça LOGIN')
                return redirect('/auth/cadastrar/')
            except:
                messages.add_message(request, messages.constants.ERROR, 'Erro na hora de cadastrar')
                return redirect('/auth/cadastrar/?status=3')
def login(request):
    return HttpResponse('Login')