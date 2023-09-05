from .models import Like
from Songs.models import Song
from django.http import JsonResponse
from .forms import CommentForm


# Create your views here.


def like(request, song_id):
    if request.method == "POST":
        action = request.POST.get("like_button")
        if action == "unlike":
            Like.objects.filter(song__id=song_id, user=request.user).delete()
        if action == "like":
            Like.objects.create(song_id=song_id, user=request.user)

        count = Song.objects.get(id=song_id).number_of_likes
        return JsonResponse({'count': count}, status=200)


def comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        song_id = request.POST.get("song_id")
        print("1" * 100)
        print(form)

        if form.is_valid():
            comment_obj = form.save(commit=False)
            comment_obj.user = request.user
            comment_obj.song = Song.objects.get(id=song_id)
            comment_obj.save()

            return JsonResponse({'message': "Comment saved and after confirmation will be published"}, status=200)
