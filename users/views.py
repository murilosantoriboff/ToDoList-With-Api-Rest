from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

def cadastrar(request):
    if request.method == 'GET':
        return render(request, 'cadastrar.html')

def login(request):
    return HttpResponse('Login')