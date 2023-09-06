from django.urls import path
from . import views

urlpatterns = [

    path('song_details/<int:pk>', views.SongDetailsView.as_view(), name="song_details"),
    path('upload_song/', views.SongUploadView.as_view(), name="upload_song"),
]
