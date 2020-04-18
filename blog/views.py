from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from django.http import Http404
from .forms import CreatePostModelForm
from django.views.generic import CreateView
from django.utils import timezone


def blog_post_detail_page(request, slug):
    print("DJANGO говорит", request.method, request.path, request.user)
    # queryset = BlogPost.objects.filter(slug=slug) # метод filter() дает набор объектов
    # if queryset.count() == 0:
    #     raise Http404
    # obj = queryset.first()
    obj = get_object_or_404(BlogPost, slug=slug)
    # obj = BlogPost.objects.get(id=post_id) - метод get() дает только один объект
    template_name = 'blog/blog_post_detail.html'
    context = {'object': obj}
    return render(request, template_name, context)

# @login_required
@staff_member_required
def blog_post_create_view(request):
    form = CreatePostModelForm(request.POST or None)
    template_name = "blog/blog_post_create.html"
    if form.is_valid():
        # obj = BlogPost.objects.create(**form.cleaned_data)
        # form.save()
        obj = form.save(commit=False)
        obj.title = form.cleaned_data.get("title") # + "0"  добавление символа к заголовку
        # obj.user = request.user # используется для ограничения незаголиненных пользователей создавать посты
        # # вместо декоратора @staff_member_required
        obj.save()

        form = CreatePostModelForm()
    context = {"form": form}
    return render(request, template_name, context)


# # Почему-то вызывается ошибка "type object 'CreatePostForm' has no attribute '_meta' "
# class BlogPostCreate (CreateView):
#     model = BlogPost
#     form_class = CreatePostModelForm
#     # form = CreatePostModelForm(request.POST or None)
#     template_name = "blog/blog_post_create.html"
#     # fields = ['title', 'slug', 'content']


def blog_post_list_view(request):
    # qs = BlogPost.objects.all()
    # now = timezone.now()
    # qs = BlogPost.objects.filter(publish_date__lte=now)
    qs = BlogPost.objects.all().published()
    # qs = BlogPost.objects.filter(title__icontains="Философия")
    template_name = "blog/blog_post_list.html"
    context = {"object_list": qs}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/blog_post_detail.html'
    context = {'object': obj}
    return render(request, template_name, context)

@staff_member_required
def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = CreatePostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'blog/blog_post_create.html'
    context = {'form': form, "title": f'Редактирование публикации "{obj.title}"'}
    return render(request, template_name, context)


@staff_member_required
def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/blog_post_delete.html'
    context = {'object': obj}
    if request.method == "POST":
        obj.delete()
        return redirect ("/blog")
    return render(request, template_name, context)