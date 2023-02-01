from todo.models import Tarefa
from rest_framework.serializers import ModelSerializer

class TarefaSerializer(ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'
