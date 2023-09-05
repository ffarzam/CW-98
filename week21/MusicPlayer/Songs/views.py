from django.views.generic.detail import DetailView
from .models import Song
from Interactions.models import Playlist, Comment
from Interactions.forms import CommentForm
from django.core.paginator import Paginator


# Create your views here.


class SongDetails(DetailView):
    model = Song
    template_name = "song/song_details.html"
    context_object_name = "song"
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["playlists"] = None
        if self.request.user.is_authenticated:
            user = self.request.user
            context["playlists"] = Playlist.objects.filter(user=user)

        comment_list = Comment.objects.filter(song=self.get_object(), is_confirmed=True)
        paginator = Paginator(comment_list, 1)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context["comments"] = page_obj

        context["form"] = self.form_class
        return context
