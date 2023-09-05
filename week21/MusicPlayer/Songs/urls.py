from django.urls import path
from . import views

urlpatterns = [

    path('song_details/<int:pk>', views.SongDetails.as_view(), name="song_details"),
]
