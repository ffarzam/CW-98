from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    # path('post/', views.post_list),
    # path('categories/', views.category_list),
    # path('posts/<int:pk>/', views.posts_details),
    # path('categories/<int:pk>/', views.categories_details),
    # path('authors/', views.author_list),
    # path('authors/<int:pk>/', views.authors_details),

]