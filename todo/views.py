from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth import  authenticate ,login
from django.shortcuts import render, redirect



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



@api_view(['PUT'])
def todoUpdate(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Todo updated successfully'}, status= status. HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except:
        Todo.DoesNotExist
        return Response({'message': "Todo doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def todoDelete(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
        todo.delete()
        return Response({'message': 'Todo deleted successfully'}, status= status. HTTP_200_OK)
    except Todo.DoesNotExist:
        return Response({'message': "Todo doesn't exist"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST', 'GET'])
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('todos/')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'todo/login.html', {'error_message': error_message})
    else:
        return render(request, 'todo/login.html')

    # @api_view(['POST', 'GET'])
    # def register_view(request):
    #     if request.method=='POST':









