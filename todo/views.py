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


@api_view(['POST'])
def todoCreate(request):
    serializer = TodoSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Todo created successfully'},status=status.HTTP_201_CREATED)

    return Response({'message': "Todo can't be created"},status= status.HTTP_400_BAD_REQUEST)








