from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from django.http import Http404


def blog_post_detail_page(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    # obj = BlogPost.objects.get(id=post_id)
    template_name = 'blog/blog_post_detail.html'
    context = {'object': obj}
    return render(request, template_name, context)
