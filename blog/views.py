from django.urls import reverse_lazy

from .models import BlogPost
from .forms import CreatePostModelForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView


class BlogPostDetailView(DetailView):
    template_name = 'blog/blog_post_detail.html'
    model = BlogPost


class BlogPostCreate(CreateView):
    queryset = BlogPost.objects.all()
    form_class = CreatePostModelForm
    template_name = "blog/blog_post_create.html"


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_post_list.html'
    queryset = BlogPost.objects.all().published()


class BlogPostUpdateView(UpdateView):
    template_name = 'blog/blog_post_create.html'
    form_class = CreatePostModelForm
    model = BlogPost


class BlogPostDeleteView(DeleteView):
    template_name = 'blog/blog_post_delete.html'
    success_url = reverse_lazy('app_blog:list')
    model = BlogPost
