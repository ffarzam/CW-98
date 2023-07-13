from django.shortcuts import render
from .models import Post


# Create your views here.


def home(request):
    return render(request, "home.html")


def post_list(request):
    all_posts = Post.objects.all
    return render(request, "post_list.html", {"all_posts": all_posts})

# def posts_details(request,)
