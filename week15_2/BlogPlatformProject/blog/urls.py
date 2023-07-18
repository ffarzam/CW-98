from django.urls import path
from .views import home, post_list,post_details,category_details,category_list,search_result

urlpatterns = [
    path('', home, name="home"),
    path('post/', post_list, name="post_list"),
    path('post/<int:pk>/', post_details, name="post_details"),
    path('categories/', category_list, name="category_list"),
    path('categories/<int:pk>/', category_details, name="category_details"),
    path('search_result/', search_result, name="search_result"),


]