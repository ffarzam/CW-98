from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Comment
from users.models import Author
from django.http import HttpResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def home(request):
    if not request.COOKIES.get('home'):
        context = {"res": "Hello, welcome to my website :)"}
        response = render(request, 'index.html', context)
        response.set_cookie('home', 'Welcome back')
        return response
    else:
        res = request.COOKIES.get('home')
        context = {"res": res}
        return render(request, 'index.html', context)


def post_list(request):
    if request.method == "GET":
        all_posts = Post.objects.all()
        return render(request, "Blog/post_list.html", {"all_posts": all_posts})


def post_details(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'GET':
        all_comments = Comment.objects.filter(post=post.id)
        all_author = Author.objects.all()
        context = {"post": post, "all_comments": all_comments, "all_author": all_author}
        return render(request, "Blog/post.html", context)
    elif request.method == "POST":
        author = Author.objects.get(id=int(request.POST.get("select")))

        comment = Comment.objects.create(post=post,
                                         author=author,
                                         content=request.POST.get("comments"),
                                         comment_date=datetime.now())

        # return redirect(request.build_absolute_uri())
        # return redirect(request.path)
        return redirect("post_details", pk)


def category_list(request):
    if request.method == "GET":
        all_category = Category.objects.all()
        return render(request, "Blog/category_list.html", {"all_category": all_category})
    elif request.method == "POST":
        cat = Category.objects.create(name=request.POST.get("cat"), description=request.POST.get("description"))
        return redirect(request.path)


def category_details(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == "GET":

        posts = Post.objects.all()
        all_author = Author.objects.all()
        return render(request, "Blog/category_details.html",
                      {"category": category, "posts": posts, "all_author": all_author})
    elif request.method == "POST":
        author = Author.objects.get(id=int(request.POST.get("select")))
        post = Post.objects.create(title=request.POST.get("title"),
                                   content=request.POST.get("content"),
                                   category=category,
                                   author=author)
        return redirect(request.path)


def search_result(request):
    if request.method == "GET":
        searched = request.GET.get('searched')
        if searched:
            results = Post.objects.filter(Q(title__icontains=searched)
                                          | Q(content__icontains=searched)
                                          ).distinct()

            return render(request, 'Blog/search_result.html', {"searched": searched, "results": results})
        else:
            return render(request, 'Blog/search_result.html', {"searched": searched})
