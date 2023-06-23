from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .backends import CustomBackendAuthentication
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required




# Create your views here.
@login_required
@api_view(['GET'])
def todoList(request):
    todos = Todo.objects.filter(user=request.user)
    serializer= TodoSerializer(todos, many=True)
    return Response(serializer.data)

@login_required
@api_view(['GET'])
def todoDetail(request,pk):
    try:
        todo=Todo.objects.get(id=pk)
        if todo.user == request.user:
            serializer = TodoSerializer(todo)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@login_required
@api_view(['POST'])
def todoCreate(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response({'message': 'Todo created successfully'}, status=status.HTTP_201_CREATED)
    return Response({'message': "Todo can't be created"}, status=status.HTTP_400_BAD_REQUEST)



@login_required
@api_view(['PUT'])
def todoUpdate(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
        if todo.user == request.user:
            serializer = TodoSerializer(todo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Todo updated successfully'}, status= status. HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    except:
        Todo.DoesNotExist
        return Response({'message': "Todo doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

@login_required
@api_view(['DELETE'])
def todoDelete(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
        if todo.user == request.user:
            todo.delete()
            return Response({'message': 'Todo deleted successfully'}, status= status. HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
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
            return redirect('todoList')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'todo/login.html')


@api_view(['POST', 'GET'])
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            messages.success(request, 'Your account has been created, You are now able to login')
            return redirect('login')
        else:
            messages.error(request, 'invalid data , pls re-enter the data')
            return redirect('register')
    else:
        form = RegistrationForm()
        return render(request, 'todo/registration.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'are you sure you want to log out?')
    return render(request, 'todo/logout.html')














