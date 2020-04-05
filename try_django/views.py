from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def home_page(request):
    my_title = "Дело было летом..."
    context = {"title": my_title}
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