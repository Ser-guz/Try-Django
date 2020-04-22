from django.urls import path
from .views import (
    blog_post_detail_page,
    # blog_post_list_view,
    # blog_post_create_view,
    BlogPostCreate,
    BlogPostListView,
    blog_post_update_view,
    blog_post_delete_view,
)

urlpatterns = [
    # path('blog/<int:post_id>/', blog_post_detail_page, name='blog_view'),
    path('blog/<str:slug>/', blog_post_detail_page, name='blog_view'),
    path('blog/<str:slug>/edit', blog_post_update_view, name='blog_post_update'),
    path('blog/<str:slug>/delete', blog_post_delete_view, name='blog_post_delete'),
    # path('blog/', blog_post_list_view, name='blog_post_list'),
    path('blog/', BlogPostListView.as_view(), name='blog_post_list'),
    path('blog/create_post', BlogPostCreate.as_view(), name='blog_post_create'),
    # path('blog/create_post', blog_post_create_view, name='blog_post_create'),
]
