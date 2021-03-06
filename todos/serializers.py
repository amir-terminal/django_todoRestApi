from rest_framework import serializers
from todos.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title','desc','is_complete','date_created',)

        
