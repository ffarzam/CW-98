from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Comment
from users.models import Author
from django.http import HttpResponse


# Create your views here.


def home(request):
    if not request.COOKIES.get('home'):
        context = {}
        response = render(request, 'index.html', context)
        response.set_cookie('home', 'Welcome back')
        return response
    else:
        res = request.COOKIES.get('home')
        context = {"res": res}
        return render(request, 'index.html', context)



def post_list(request):
    all_posts = Post.objects.all()

    return render(request, "Blog/post_list.html", {"all_posts": all_posts})


def post_details(request, pk):
    context = {}
    if request.method == 'GET':
        post = Post.objects.get(id=pk)
        all_comments = Comment.objects.all()
        context = {"post": post, "all_comments": all_comments}
    return render(request, "Blog/post.html", context)


def category_list(request):
    all_category = Category.objects.all()
    return render(request, "Blog/category_list.html", {"all_category": all_category})


def category_details(request, pk):
    category = Category.objects.get(id=pk)
    return render(request, "Blog/category_details.html", {"category": category})


def search_result(request):
    if request.method == "GET":
        searched = request.GET.get('searched')
        if searched:
            # results = list(set(chain(Task.objects.filter(title__icontains=searched),
            #                          Task.objects.filter(description__icontains=searched),
            #                          Task.objects.filter(tag__name__icontains=searched)
            #                          )
            #                    )
            #                )
            results = Post.objects.filter(Q(title__icontains=searched)
                                          | Q(content__icontains=searched)
                                          ).distinct()

            return render(request, 'Blog/search_result.html', {"searched": searched, "results": results})
        else:
            return render(request, 'Blog/search_result.html', {"searched": searched})
