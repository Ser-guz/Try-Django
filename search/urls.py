from django.urls import path
from .views import (
    # search_view,
    SearchCreateView
)

urlpatterns = [
    # path('search/', search_view, name='search_view'),
    path('search/', SearchCreateView.as_view(), name='search_view'),
]
