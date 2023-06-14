from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def todoList(request):
    todos = Todo.objects.all()
    serializer= TodoSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def todoDetail(request,pk):

    try:
        todo=Todo.objects.get(id=pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)





