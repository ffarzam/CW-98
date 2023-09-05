from django.urls import path
from . import views

urlpatterns = [
    path('like/<int:song_id>', views.like, name="like"),
    path('playlist/', views.playlist, name="playlist"),
    path('comment/', views.comment, name="comments"),


]
