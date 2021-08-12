from django.urls import path
from .views import TodoApiView,DetailApiView
app_name="todos"
urlpatterns = [
    
    # path("todo_create", CreateTodoAPIView.as_view(), name="creat_todo"),
    path('<int:id>',DetailApiView.as_view(),name='detail'),
    path("", TodoApiView.as_view(), name="todos"),
]
