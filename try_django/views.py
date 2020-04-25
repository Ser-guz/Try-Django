from blog.models import BlogPost
from django.views.generic import ListView


class HomePageListView(ListView):
    queryset = BlogPost.objects.all()[:5]
    template_name = 'home.html'
    context_object_name = 'blog_list'
