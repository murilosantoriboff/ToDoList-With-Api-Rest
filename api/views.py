from django.shortcuts import render
from todo.models import Tarefa
from rest_framework.decorators import api_view
from .serializer import TarefaSerializer
from rest_framework.response import Response

@api_view(['GET'])
def api_todo(request):
    tarefa = Tarefa.objects.all()
    serializer = TarefaSerializer(tarefa, many=True)
    return Response(serializer.data)