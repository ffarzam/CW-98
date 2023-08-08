from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('todos/', views.TodoListView.as_view(), name='todo_list'),
    path('todos/<int:pk>/', views.TodoDetailView.as_view(), name='todo_detail'),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('permissiondenied/', views.permission_denied, name='permissiondenied'),
]
