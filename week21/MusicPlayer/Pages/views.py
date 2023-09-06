from django.contrib.auth.decorators import login_required
from django.db.models import Q
from Songs.models import Song
from Accounts.models import Base, User, Artist
from Accounts.forms import BaseUpdateForm, MyUserUpdateForm, ArtistUpdateForm
from django.shortcuts import render, redirect
from django.views.generic.list import ListView


# Create your views here.


class Home(ListView):
    model = Song
    context_object_name = 'songs'
    template_name = "home/home.html"
    paginate_by = 3
    ordering = ['-upload_date']

    def get_queryset(self):
        search = self.request.GET.get("search")
        if search:
            queryset = self.model.objects.filter(Q(title__icontains=search))
        else:
            queryset = self.model.objects.all()
        return queryset


@login_required
def profile(request, id):
    user = Base.objects.get(id=id)
    recently_listened_songs = None
    if request.COOKIES.get('recently_listen_song_id'):
        recently_listened_songs_id = eval(request.COOKIES.get('recently_listen_song_id'))

        recently_listened_songs_id = list(map(int, recently_listened_songs_id))

        songs = Song.objects.filter(id__in=recently_listened_songs_id)
        recently_listened_songs = sorted(songs, key=lambda x: recently_listened_songs_id.index(x.id))
    return render(request, "profile.html", context={"user": user, "recently_listened_songs": recently_listened_songs})


@login_required()
def profile_edit(request):
    if request.method == "GET":
        if request.user.get_user():
            account = request.user.get_user()
            form = MyUserUpdateForm(instance=account)
        elif request.user.get_artist():
            account = request.user.get_artist()
            form = ArtistUpdateForm(instance=account)
        else:
            account = request.user
            form = BaseUpdateForm(instance=account)

        return render(request, 'home/profile_edit.html', {"account": account, "form": form})

    elif request.method == "POST":
        if request.user.get_user():
            account = request.user.get_user()
            form = MyUserUpdateForm(request.POST, instance=account)
        elif request.user.get_artist():
            account = request.user.get_artist()
            form = ArtistUpdateForm(request.POST, instance=account)
        else:
            account = request.user
            form = BaseUpdateForm(request.POST, instance=account)

        if form.is_valid():

            form.save()
            return redirect('profile', request.user.id)

        else:
            if request.user.get_user():
                account = request.user.get_user()
                form = MyUserUpdateForm(instance=account)
            elif request.user.get_artist():
                account = request.user.get_artist()
                form = ArtistUpdateForm(instance=account)
            else:
                account = request.user
                form = BaseUpdateForm(instance=account)

    return render(request,
                  'home/profile_edit.html',
                  {'form': form})
