from django.shortcuts import render
from django_filters import filterset
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.serializers import Serializer
from todos.models import Todo
from rest_framework import permissions,filters
from todos.serializers import TodoSerializer
from rest_framework import response,status
from django_filters.rest_framework import  DjangoFilterBackend
# Create your views here.

class TodoApiView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['id','title','is_complete',]
    search_fields = ['id','title','is_complete',]
    
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    

class DetailApiView(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TodoSerializer
    lookup_field = 'id'
    
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)
    
    

# class CreateTodoAPIView(CreateAPIView):
#     serializer_class = TodoSerializer
#     permission_classes = [permissions.IsAuthenticated,]
#     def perform_create(self, serializer):
#         return serializer.save(owner=self.request.user)

# class TodosListAPIView(ListAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = TodoSerializer
    
#     def get_queryset(self):
#         return Todo.objects.filter(owner=self.request.user)
        
        
        
    