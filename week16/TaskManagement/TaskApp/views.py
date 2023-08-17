from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Task, Tag
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator
from datetime import datetime
import mimetypes
from django.http.response import HttpResponse, FileResponse
import os
from django.conf import settings
from .forms import CreateTaskForm, CreateTagForm, CreateCategoryForm
from .mixins import TaskMixin
from django.views import View
from django.views.generic import ListView


# Create your views here.

def home(request):
    if request.method == "GET":

        all_tasks = Task.objects.all().order_by("?")
        for task in all_tasks:
            if task.due_date < datetime.now().date():
                Task.objects.filter(id=task.id).update(status="done")
        all_tasks = Task.objects.all().order_by("?")

        context = {"tasks": all_tasks}
        return render(request, "home.html", context=context)


def task_filter(sorting_method, filter_method=None):
    if filter_method is None or filter_method == "all":
        all_tasks = Task.objects.all()

    else:
        all_tasks = Task.objects.filter(status=filter_method)

    if sorting_method == 'Title_ASC':
        all_tasks = all_tasks.order_by('title')
    elif sorting_method == 'Title_DESC':
        all_tasks = all_tasks.order_by('-title')
    elif sorting_method == 'Date_ASC':
        all_tasks = all_tasks.order_by('due_date')
    elif sorting_method == 'Date_DESC':
        all_tasks = all_tasks.order_by('-due_date')
    elif sorting_method == 'No Order':
        all_tasks = all_tasks
    else:
        all_tasks = all_tasks.order_by('due_date')
    return all_tasks


# def tasks(request):
#     if request.method == "GET":
#         all_category = Category.objects.all()
#         all_tags = Tag.objects.all()
#
#         filter_method = request.GET.get('gridRadios')
#         sorting_method = request.GET.get('select')
#
#         if filter_method == "all":
#             all_tasks = task_filter(sorting_method, filter_method)
#
#         elif filter_method == "done":
#             all_tasks = task_filter(sorting_method, filter_method)
#
#         elif filter_method == "doing":
#             all_tasks = task_filter(sorting_method, filter_method)
#
#         elif filter_method == "todo":
#             all_tasks = task_filter(sorting_method, filter_method)
#
#         else:
#             all_tasks = task_filter(sorting_method)
#
#         paginator = Paginator(all_tasks, 3)
#         page_number = request.GET.get("page")
#         page_obj = paginator.get_page(page_number)
#
#         status_list = []
#         for i in Task.status_choice:
#             status_list.append(i[0])
#         form = CreateTaskForm
#         context = {"tasks": page_obj, "all_category": all_category, "all_tags": all_tags,
#                    "all_status": status_list, 'form': form}
#         return render(request, "tasks.html", context=context)
#
#     elif request.method == "POST":
#         form = CreateTaskForm(request.POST)
#         if form.is_valid():
#             task = form.save(commit=False)
#             task.user = request.user
#             task.save()
#         return redirect(request.path)


class TaskListView(ListView):
    model = Task
    template_name = "tasks.html"
    paginate_by = 3
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        status_list = []
        for i in Task.status_choice:
            status_list.append(i[0])

        all_category = Category.objects.all()
        all_tags = Tag.objects.all()
        context["all_category"] = all_category
        context["all_tags"] = all_tags
        context["form"] = CreateTaskForm
        context["status_list"] = status_list
        context["tasks"] = kwargs["object_list"]
        return context

    def get(self, request, *args, **kwargs):

        filter_method = request.GET.get('gridRadios')
        sorting_method = request.GET.get('select')

        if filter_method == "all":
            all_tasks = task_filter(sorting_method, filter_method)

        elif filter_method == "done":
            all_tasks = task_filter(sorting_method, filter_method)

        elif filter_method == "doing":
            all_tasks = task_filter(sorting_method, filter_method)

        elif filter_method == "todo":
            all_tasks = task_filter(sorting_method, filter_method)

        else:
            all_tasks = task_filter(sorting_method)

        context = self.get_context_data(object_list=all_tasks)

        return render(request, self.template_name, context=context)

    def post(self, request):
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
        return redirect(request.path)


def task_details(request, pk):
    if request.method == "GET":
        status_list = []
        for i in Task.status_choice:
            status_list.append(i[0])

        all_category = Category.objects.all()
        all_tags = Tag.objects.all()

        task = get_object_or_404(Task, id=pk)
        form = CreateTagForm
        context = {"task": task, "name": os.path.basename(f"{task.file}"), "all_category": all_category,
                   "all_tags": all_tags,
                   "all_status": status_list,
                   "form": form}
        return render(request, "task_details.html", context=context)

    elif request.method == "POST":
        task = get_object_or_404(Task, id=pk)

        if request.POST.get("title"):
            category = Category.objects.get(id=int(request.POST.get("category")))

            task = Task.objects.filter(id=pk).update(title=request.POST.get("title"),
                                                     description=request.POST.get("content"),
                                                     due_date=request.POST.get("due_date"),
                                                     status=request.POST.get("status"),
                                                     category=category,
                                                     )
            if request.FILES.get('file'):
                # file_name = file.name
                # f = FileSystemStorage(location=settings.MEDIA_ROOT/"uploads/")
                # print(f)
                # main_file = f.save(file_name, file)
                # file_url = f.url(main_file)
                # print(file_url)

                task = task.get()
                task.file = request.FILES.get('file')
                task.save()

            task = Task.objects.get(id=pk)

            if dict(request.POST).get('tag'):
                task.tag.set([])
                for i in dict(request.POST)['tag']:
                    tag = Tag.objects.get(id=int(i))
                    task.tag.add(tag)
                task.save()
            ######################################################333
            if not request.COOKIES.get('history'):

                response = redirect(request.path)
                response.set_cookie('history', ['You update a Task'])
                return response
            else:
                res = request.COOKIES.get('history')
                print(res)
                res = eval(res)
                res.append('You update a Task')

                response = redirect(request.path)
                response.set_cookie('history', res)
                return response
            ######################################################333


def create_tag(request, pk):
    task = get_object_or_404(Task, id=pk)
    form = CreateTagForm(request.POST)
    print(form.is_valid())
    if form.is_valid():
        tag = form.save()
        task.tag.add(tag)
        task.save()
        if not request.COOKIES.get('history'):
            response = redirect("task_details", pk)
            response.set_cookie('history', ['You create a Tag'])
            return response

        else:
            res = request.COOKIES.get('history')
            print(res)
            res = eval(res)
            res.append('You create a Tag')
            response = redirect("task_details", pk)
            response.set_cookie('history', res)
            return response


def search(request):
    if request.method == "GET":
        return render(request, 'search.html')


def search_result(request):
    if request.method == "GET":
        searched = request.GET.get('searched')
        if searched:

            results = Task.objects.filter(Q(title__contains=searched)
                                          | Q(description__contains=searched)
                                          | Q(tag__name__contains=searched)
                                          ).distinct()
            paginator = Paginator(results, 2)
            page_number = request.GET.get("page")
            page_obj = paginator.get_page(page_number)

            return render(request, 'search_result.html', {"searched": searched, "results": page_obj})
        else:
            return render(request, 'search_result.html', {"searched": searched})


class CategoryListView(ListView):
    model = Category
    template_name = "category.html"
    paginate_by = 3
    context_object_name = "categories"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CreateCategoryForm

        return context

    def post(self, request):
        form = CreateCategoryForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect(request.path)


# def category(request):
#     if request.method == "GET":
#         all_categories = Category.objects.all()
#         paginator = Paginator(all_categories, 3)
#         page_number = request.GET.get("page")
#         page_obj = paginator.get_page(page_number)
#         context = {"categories": page_obj}
#         return render(request, "category.html", context=context)
#
#     elif request.method == "POST":
#
#         cat = Category.objects.create(name=request.POST.get("cat"),
#                                       description=request.POST.get("description"),
#                                       image=request.FILES.get('file'))
#         return redirect(request.path)


def category_task(request, pk):
    category_item = get_object_or_404(Category, id=pk)
    if request.method == "GET":
        category_item = get_object_or_404(Category, id=pk)
        all_tasks = Task.objects.filter(category=category_item)

        paginator = Paginator(all_tasks, 2)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        all_tags = Tag.objects.all()
        status_list = []
        for i in Task.status_choice:
            status_list.append(i[0])

        context = {"tasks": page_obj, "category": category_item, "all_tags": all_tags,
                   "all_status": status_list}

        return render(request, "category_task.html", context=context)
    elif request.method == "POST":
        if request.POST.get("title"):
            task = Task.objects.create(title=request.POST.get("title"),
                                       description=request.POST.get("content"),
                                       due_date=request.POST.get("due_date"),
                                       status=request.POST.get("status"),
                                       category=category_item,
                                       file=request.FILES['file']
                                       )
            for i in dict(request.POST)['tag']:
                tag = Tag.objects.get(id=int(i))
                task.tag.add(tag)

            # return redirect(request.build_absolute_uri())
            return redirect(request.path)

        elif request.POST.get("cat"):
            Category.objects.filter(id=pk).update(name=request.POST.get("cat"),
                                                  description=request.POST.get("description"),
                                                  image=Category.objects.get(id=pk).image)
            if request.FILES.get('file'):
                category = Category.objects.get(id=pk)
                category.image = request.FILES.get('file')
                category.save()

            ######################################################333
            if not request.COOKIES.get('history'):

                response = redirect(request.path)
                response.set_cookie('history', ['You update a category'])
                return response
            else:
                res = request.COOKIES.get('history')
                print(res)
                res = eval(res)
                res.append('You update a category')

                response = redirect(request.path)
                response.set_cookie('history', res)
                return response
            ######################################################333
            # return redirect(request.path)


def about_us(request):
    return render(request, "about_us.html")


def download_file(request, filename):
    filepath = settings.BASE_DIR / f'media/uploads/{filename}'
    file = open(filepath, 'rb')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = FileResponse(file, content_type=mime_type)
    response['Content-Disposition'] = f"attachment; filename={filename}"
    return response


def view_file(request, filename):
    filepath = settings.BASE_DIR / f'media/uploads/{filename}'
    #
    mime_type, _ = mimetypes.guess_type(filepath)
    with open(filepath, 'rb') as file:
        response = HttpResponse(file.read(), content_type=mime_type)
        response['Content-Disposition'] = f"Inline; filename={filename}"
    # return render(request, "show.html",context={"data":filepath})
    return response


def tag_details(request, pk):
    if request.method == "GET":
        tag = Tag.objects.get(id=pk)
        tasks = Task.objects.filter(tag=tag)
        context = {"tag": tag, "all_task": tasks}

        return render(request, "tag_details.html", context=context)
    elif request.method == "POST":
        Tag.objects.filter(id=pk).update(name=request.POST.get("tag"))
        ######################################################333
        if not request.COOKIES.get('history'):

            response = redirect(request.path)
            response.set_cookie('history', ['You update a tag'])
            return response
        else:
            res = request.COOKIES.get('history')
            print(res)
            res = eval(res)
            res.append('You update a tag')

            response = redirect(request.path)
            response.set_cookie('history', res)
            return response
        ######################################################333


def delete_category(request, pk):
    q = Category.objects.filter(id=pk)
    if q:
        q.delete()
    return redirect("category")


def delete_task(request, pk):
    q = Task.objects.filter(id=pk)
    if q:
        q.delete()
    return redirect("tasks")


def delete_tag(request, pk):
    q = Tag.objects.filter(id=pk)
    if q:
        q.delete()
    return redirect("tag_list")


def tag_list(request):
    all_tags = Tag.objects.all()
    context = {'tags': all_tags}
    return render(request, "tag_list.html", context=context)


def Histories(request):
    if not request.COOKIES.get('history'):
        context = {"massage": ['No History', ]}
        response = render(request, 'histories.html', context=context)
        return response
    else:
        res = request.COOKIES.get('history')
        print(res)
        print(type(res))
        res = eval(res)

        context = {"massage": res}
        response = render(request, 'histories.html', context=context)

        return response


class TaskDetailView(TaskMixin, View):
    template_name = 'task_details.html'
