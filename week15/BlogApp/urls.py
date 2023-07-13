from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('post/', views.post_list, name="post_list"),
    path('posts/<int:pk>/', views.post_details, name="post_details"),
    # path('categories/', views.category_list),
    # path('categories/<int:pk>/', views.categories_details),
    # path('authors/', views.author_list),
    # path('authors/<int:pk>/', views.authors_details),

]
