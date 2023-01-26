from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('criar_tarefa/', views.criar_tarefa, name='criar_tarefa')
]