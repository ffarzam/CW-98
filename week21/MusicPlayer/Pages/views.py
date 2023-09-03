from django.shortcuts import render
from Songs.models import Song


# Create your views here.

def home(request):
    if request.method == "GET":
        all_songs = Song.objects.all()

        context = {"tasks": all_songs}
        return render(request, "home/home.html", context=context)
