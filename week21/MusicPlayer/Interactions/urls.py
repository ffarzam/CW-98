from django.urls import path
from . import views

urlpatterns = [
    path('like/<int:song_id>', views.like, name="like"),
    path('create_playlist/', views.create_playlist, name="create_playlist"),
    path('add_to_playlist/<int:song_id>', views.add_to_playlist, name="add_to_playlist"),
    path('comment/', views.comment, name="comments"),
    path('playlist/', views.PlaylistView.as_view(), name="playlist"),
    path('playlist_songs/<str:pk>', views.PlaylistSongsView.as_view(), name="playlist_songs"),
    path('delete_playlist/<str:pk>', views.DeletePlaylist.as_view(), name="delete_playlist"),
    path('delete_song_from_playlist/<str:playlist_id>/<str:song_id>', views.DeleteSongFromPlaylist.as_view(), name="delete_song_from_playlist"),
    path('song_played/', views.song_played, name="song_played"),

]
