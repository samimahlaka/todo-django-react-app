from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def todoList(request):
    todos = Todo.objects.all()
    serializer= TodoSerializer(todos, many=True)
    return Response(serializer.data)

