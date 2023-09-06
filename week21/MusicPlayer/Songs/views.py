from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from .models import Song
from Interactions.models import Playlist, Comment
from Interactions.forms import CommentForm
from django.core.paginator import Paginator
from .forms import SongUploadForm


# Create your views here.


class SongDetailsView(DetailView):
    model = Song
    template_name = "song/song_details.html"
    context_object_name = "song"
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["playlists"] = None
        if self.request.user.is_authenticated:
            user = self.request.user
            context["playlists"] = Playlist.objects.select_related('user').filter(user=user)

        comment_list = Comment.objects.filter(song=self.get_object(), is_confirmed=True)
        paginator = Paginator(comment_list, 1)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context["comments"] = page_obj
        context["form"] = self.form_class
        return context


class SongUploadView(LoginRequiredMixin, CreateView):
    model = Song
    form_class = SongUploadForm
    template_name = "song/song_upload.html"
    success_url = "profile"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.get_artist:
            return JsonResponse({"Error": "Not Allowed"}, status=404)

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        song = form.save()
        song.genres.set(form.cleaned_data["genre"])
        song.save()
        artist = self.request.user.get_artist()
        artist.song.add(song)
        for artist in form.cleaned_data["other_artists"]:
            artist.song.add(song)
        # return JsonResponse({"message":"ok"})
        return redirect(self.success_url, self.request.user.id)
