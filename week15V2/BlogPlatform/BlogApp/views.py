from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Comment
from django.http import Http404


# Create your views here.


def home(request):
    return render(request, "BlogApp/home.html")


def post_list(request):
    all_posts = Post.objects.all()
    return render(request, "BlogApp/post_list.html", {"all_posts": all_posts})


def post_details(request, pk):
    try:
        post = get_object_or_404(Post, id=pk)
        print(post.title)
        comments = list(Comment.objects.all())
        print(comments)
        res = []
        for comment in comments:
            if comment.post.title == post.title:
                res.append(comment)

        return render(request, "BlogApp/post_details.html", {"post": post, "comments": res})
    except:
        raise Http404("No MyModel matches the given query.")


def category_list(request):
    all_category = Category.objects.all()
    return render(request, "BlogApp/category_list.html", {"all_category": all_category})


def categories_details(request, pk):
    category = Category.objects.get(id=pk)
    return render(request, "BlogApp/category_details.html", {"category": category})
