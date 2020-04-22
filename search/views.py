from django.shortcuts import render
from .models import SearchQuery
from blog.models import BlogPost


def search_view(request):
    template_name = 'search/search_view.html'
    query = request.GET.get('q', )
    user = None
    if request.user.is_authenticated:
        user = request.user
    context = {'query': query}
    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        blog_list = BlogPost.objects.search(query=query)
        context['blog_list'] = blog_list
    return render(request, template_name, context)