from django.urls import path
from . import views

urlpatterns = [
    path('todo_api/', views.api_todo, name='api_todo')
]