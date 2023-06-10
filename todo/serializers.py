from rest_framework import serializers
from .models import Todo

class TodoSerializer (serializers.ModelsSerializers):
    class Meta:
        model = Todo
        filds = ('title', 'description', 'completed')