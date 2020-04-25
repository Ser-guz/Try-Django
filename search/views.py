from django.shortcuts import render
from django.views.generic import CreateView

from .forms import SearchQueryModelForm
from .models import SearchQuery
from blog.models import BlogPost

""" 
Создание объекта "Запрос", получение набора объектов из модели "BlogPost" по фильтрам и отрисовка на странице.
Совмещение функций CreateView и ListView.
"""
class SearchCreateView(CreateView):
    model = SearchQuery
    form_class = SearchQueryModelForm
    template_name = 'search/search_view.html'

    def post(self, request, *args, **kwargs):
        query = request.GET.get('q')
        if request.user.is_authenticated:
            user = request.user
        if query is not None:
            SearchQuery.objects.create(user=user, query=query)
        return super().post(request, *args, **kwargs)

    def get_context_data(self, query, **kwargs):
        context = super(SearchCreateView, self).get_context_data(**kwargs)
        context['blog_list'] = BlogPost.objects.search(query=query)
        return context

