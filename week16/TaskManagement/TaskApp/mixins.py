from django.shortcuts import render, redirect
from .models import Task
from .forms import CreateTaskForm


class TaskMixin:
    form_class = CreateTaskForm
    template_name = None

    def dispatch(self, request, *args, **kwargs):
        task = Task.objects.get(id=kwargs['pk'])
        if not task.user == request.user:
            return redirect("permissiondenied")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        form = self.form_class(instance=task)
        return render(request, self.template_name, {'task': task, "form":form})

    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        form = self.form_class(request.POST, instance=task)
        if form.is_valid():
            form.save(commit=False)
            task.user = task.user
            task.tag.set(form.cleaned_data["tag"])
            task.save()
            return redirect('home')
        return render(request, self.template_name, {'task': task})
