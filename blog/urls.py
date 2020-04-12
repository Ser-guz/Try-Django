from django.urls import path
from .views import blog_post_detail_page

urlpatterns = [
    # path('blog/<int:post_id>/', blog_post_detail_page, name='blog_view'),
    path('blog/<str:slug>/', blog_post_detail_page, name='blog_view'),
]
