from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('criar_tarefa/', views.criar_tarefa, name='criar_tarefa'),
    path('detalhes_tarefa/<int:id>/', views.detalhes_tarefa, name='detalhes_tarefa'),
    path('excluir_tarefa/<int:id>', views.excluir_tarefa, name='excluir_tarefa'),
]