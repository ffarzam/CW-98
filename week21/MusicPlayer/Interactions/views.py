import logging
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView
from .models import Like, Playlist
from Songs.models import Song
from django.http import JsonResponse
from .forms import CommentForm

# Create your views here.


logger = logging.getLogger("django")
played_song_logger = logging.getLogger("played_song")


@login_required
def like(request, song_id):
    if request.method == "POST":
        if not request.user.is_permitted:
            return JsonResponse({"Error": "Not Allowed"}, status=404)
        action = request.POST.get("like_button")
        if action == "unlike":
            Like.objects.filter(song__id=song_id, user=request.user).delete()
        if action == "like":
            Like.objects.create(song_id=song_id, user=request.user)

        count = Song.objects.get(id=song_id).number_of_likes
        return JsonResponse({'count': count}, status=200)


@login_required
def create_playlist(request):
    if request.method == "GET":
        if not request.user.is_permitted:
            return JsonResponse({"Error": "Not Allowed"}, status=404)
        title = request.GET.get("playlist_title")
        try:
            qs = Playlist.objects.select_related("user").filter(user=request.user)
            for playlist in qs.iterator():
                if playlist.title == title:
                    raise ValueError

            playlist_obj = Playlist.objects.create(title=title, user=request.user)
            logger.info(f"{request.user.username} created {playlist_obj}")
            return JsonResponse(
                {'message': f"Playlist {title} was created", "id": playlist_obj.id, "title": playlist_obj.title},
                status=200)
        except ValueError:
            return JsonResponse(
                {'message': f"You already have a playlist titled {title}"},
                status=200)


@login_required
def add_to_playlist(request, song_id):
    if request.method == "POST":
        if not request.user.is_permitted:
            return JsonResponse({"Error": "Not Allowed"}, status=404)

        playlist_id = request.POST.get("playlist_id_input")
        try:
            qs = Playlist.objects.filter(id=playlist_id)
            if qs.exists():
                playlist = qs.get()
                song = Song.objects.get(id=song_id)
                playlist.song.add(song)
                subject = "Add to Playlist"
                content = f"{song} added to {playlist}"
                send_mail(subject, content,
                          settings.DEFAULT_FROM_EMAIL, [request.user.email])
                return JsonResponse({'message': f"song {song} added to the {playlist.title}"}, status=200)
        except Exception:
            return JsonResponse({'message': "error"}, status=200)


@login_required
def comment(request):
    if request.method == "POST":
        if not request.user.is_permitted:
            return JsonResponse({"Error": "Not Allowed"}, status=404)
        form = CommentForm(request.POST)
        song_id = request.POST.get("song_id")

        if form.is_valid():
            comment_obj = form.save(commit=False)
            comment_obj.user = request.user
            comment_obj.song = Song.objects.get(id=song_id)
            comment_obj.save()

            return JsonResponse({'message': "Comment saved and after confirmation will be published"}, status=200)


class PlaylistView(LoginRequiredMixin, ListView):
    model = Playlist
    template_name = "playlist/playlist.html"
    context_object_name = 'playlists'
    ordering = ['-created_at']

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_permitted:
            return JsonResponse({"Error": "Not Allowed"}, status=404)

        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Playlist.objects.select_related('user').filter(user=self.request.user)


class PlaylistSongsView(LoginRequiredMixin, DetailView):
    model = Playlist
    template_name = "playlist/playlist_songs.html"
    context_object_name = 'playlist'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_permitted:
            return JsonResponse({"Error": "Not Allowed"}, status=404)

        return super().dispatch(request, *args, **kwargs)


class DeletePlaylist(LoginRequiredMixin, DeleteView):
    model = Playlist
    template_name = "playlist/playlist_delete.html"
    success_url = reverse_lazy("playlist")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_permitted:
            return JsonResponse({"Error": "Not Allowed"}, status=404)

        return super().dispatch(request, *args, **kwargs)


class DeleteSongFromPlaylist(LoginRequiredMixin, View):

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.song_id = None
        self.playlist_id = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_permitted:
            return JsonResponse({"Error": "Not Allowed"}, status=404)
        self.playlist_id = kwargs['playlist_id']
        self.song_id = kwargs['song_id']
        return super().dispatch(request, *args, **kwargs)

    def get(self, *args, **kwargs):
        song_obj = Song.objects.get(id=self.song_id)
        Playlist.objects.get(id=self.playlist_id).song.remove(song_obj)
        return redirect("playlist_songs", self.playlist_id)


def song_played(request):
    if request.method == "GET":
        song_id = request.GET.get("song_id")
        song_obj = Song.objects.get(id=song_id)
        message = f"{song_obj} was played by anonymous users"
        if request.user.is_authenticated:
            message = f"{request.user.username} played {song_obj}"

        played_song_logger.info(message)
        return JsonResponse({"message": message})
