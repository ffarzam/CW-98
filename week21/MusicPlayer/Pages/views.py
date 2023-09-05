from django.db.models import Q
from Songs.models import Song
from django.views.generic.list import ListView


# Create your views here.


class Home(ListView):
    model = Song
    context_object_name = 'songs'
    template_name = "home/home.html"
    paginate_by = 3
    ordering = ['-upload_date']

    def get_queryset(self):
        search = self.request.GET.get("search")
        if search:
            queryset = self.model.objects.filter(Q(title__icontains=search))
        else:
            queryset = self.model.objects.all()
        return queryset
