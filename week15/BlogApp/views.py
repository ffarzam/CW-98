from django.shortcuts import render
from .models import Post


# Create your views here.


def home(request):
    return render(request, "home.html")


def post_list(request):
    all_posts = Post.objects.all
    return render(request, "post_list.html", {"all_posts": all_posts})


def post_details(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, "post_details.html", {"post": post})
