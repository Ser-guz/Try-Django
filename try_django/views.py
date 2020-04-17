from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from blog.models import BlogPost

def home_page(request):
    title = "Добро пожаловать в Try Django"
    qs = BlogPost.objects.all()[:5]
    context = {"title": title, "blog_list": qs}
    return render(request, "home.html", context)


def contact_page(request):
    return HttpResponse('<h1>Контакты наших друзей</h1>')


def about_page(request):
    return HttpResponse('<h1>Хотите поговорить о нашем проекте?</h1>')


def example_page(request):
    context = {
        "title": "Дело было осенью...",
        "head_title": "Осень"
    }
    template_name = "hello_world.html"
    template_obj  = get_template(template_name)
    return HttpResponse(template_obj.render(context))