from django.urls import path
from .views import home_view, post_create_view, post_list_view, tagged

urlpatterns = [
    path('', home_view, name="home"),
    path('posts/', post_list_view, name="posts"),
    path('posts/<category>/', post_list_view, name="posts_by_category"),
    path('create/posts/', post_create_view, name="create_post"),

    path('tag/<slug:slug>/', tagged, name="tag"),
]
