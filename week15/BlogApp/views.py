from django.shortcuts import render
from .models import Post, Category


# Create your views here.


def home(request):
    return render(request, "home.html")


def post_list(request):
    all_posts = Post.objects.all()
    return render(request, "post_list.html", {"all_posts": all_posts})


def post_details(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, "post_details.html", {"post": post})


def category_list(request):
    all_category = Category.objects.all()
    return render(request, "category_list.html", {"all_category": all_category})


def categories_details(request, pk):
    category = Category.objects.get(id=pk)
    return render(request, "category_details.html", {"category": category})
