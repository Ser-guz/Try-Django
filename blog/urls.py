from django.urls import path
from .views import (
    BlogPostCreate,
    BlogPostListView,
    BlogPostDetailView,
    BlogPostUpdateView,
    BlogPostDeleteView,
)


app_name = 'app_blog'
urlpatterns = [
    path('blog/<str:slug>/', BlogPostDetailView.as_view(), name='blog_view'),
    path('blog/<str:slug>/edit', BlogPostUpdateView.as_view(), name='blog_post_update'),
    path('blog/<str:slug>/delete', BlogPostDeleteView.as_view(), name='blog_post_delete'),
    path('blog/', BlogPostListView.as_view(), name='list'),
    path('blog/create_post', BlogPostCreate.as_view(), name='blog_post_create'),
]
