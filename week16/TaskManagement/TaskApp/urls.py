from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('tasks/', views.TaskListView.as_view(), name="tasks"),
    path('tasks/<int:pk>/', views.TaskDetailsView.as_view(), name="task_details"),
    path('search/', views.search, name='search'),
    path('search_result/', views.search_result, name='search_result'),
    path('category/', views.CategoryListView.as_view(), name='category'),
    path('category_task/<int:pk>/', views.category_task, name='category_task'),
    path('about_us', views.about_us, name='about_us'),
    path('download_file/<filename>', views.download_file, name='download_file'),
    path('view_file/<filename>', views.view_file, name='view_file'),
    path('tag_details/<int:pk>', views.tag_details, name='tag_details'),
    path('delete_category/<int:pk>', views.delete_category, name='delete_category'),
    path('delete_task/<int:pk>', views.delete_task, name='delete_task'),
    path('tag_list/', views.tag_list, name='tag_list'),
    path('delete_tag/<int:pk>', views.delete_tag, name='delete_tag'),
    path('create_tag/<int:pk>', views.create_tag, name='create_tag'),
    path('Histories/', views.Histories, name='Histories'),

]
