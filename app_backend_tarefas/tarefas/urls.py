from django.urls import path
from .views import TarefaListCreateView, TarefaRetrieveUpdateDestroyView

urlpatterns = [
    path('tarefas/', TarefaListCreateView.as_view(), name='tarefa-list-create'),
    path('tarefas/<int:pk>/', TarefaRetrieveUpdateDestroyView.as_view(), name='tarefa-retrieve-update-destroy'),
]
