from django.urls import path
from django.shortcuts import redirect
from post.views import PostsView, new_post, PostDetail, ThemeView, CategoryView, new_cat

urlpatterns = [

    path("all/", PostsView.as_view(), name="all_posts"),
    path("theme/", ThemeView.as_view(), name='all_theme' ),
    path("cat/", CategoryView.as_view(), name='all_theme' ),
    path("new/", new_post, name="new_post"),
    path("new_cat/", new_cat, name="new_cat"),
    path("<slug:slug>/", PostDetail.as_view(), name="single_post")
]