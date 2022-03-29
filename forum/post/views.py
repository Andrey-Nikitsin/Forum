from abc import abstractmethod
from dataclasses import fields
from turtle import title
from urllib import request
from django.shortcuts import render
from post.models import Post, Category, Comment
from django.views.generic import ListView
from post.forms import PostForm, CatForm, CommitForm
from django.shortcuts import redirect
from django.views.generic.detail import DetailView
from django.views.generic import FormView, CreateView
from django.urls import reverse
from functools import wraps



class PostsView(ListView):
    paginate_by = 5
    model = Post
    template_name = "all_records.html"



def new_cat(request):
    context = {"form": CatForm()}
    if request.method == "POST":
        copy_post = request.POST.copy()
        copy_post["author"] = request.user
        form = CatForm(copy_post, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("all_theme")
        context.update(form=form)
    return render(request, "new_cat.html", context)


class CategoryView(ListView):
    paginate_by = 5
    model = Post
    template_name = "cat.html"

    @staticmethod
    def get_category():
        return Category.objects.all()
    

class ThemeView(ListView):
    paginate_by = 5
    model = Post
    template_name = "theme.html"

def new_post(request):
    context = {"form": PostForm()}
    if request.method == "POST":
        copy_post = request.POST.copy()
        copy_post["author"] = request.user
        form = PostForm(copy_post, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("all_posts")
        context.update(form=form)
    return render(request, "new_post.html", context)


class PostDetail(DetailView, FormView):
   
    model = Post
    form_class = CommitForm
    template_name= "single_post.html"
    
    
    def get_success_url(self):
        url = self.kwargs['slug']
        return f'/../posts/{url}/'

    @staticmethod
    def get_comment():
        return Comment.objects.all()
    
    def single_post(self):
        d = self.kwargs['slug']
        context = { "post": Post.objects.get(slug=d)}
        context["post"].views += 1
        context["post"].save()
        return None
    
    def get_url(self):
        return self.url

    def form_valid(self, form):
        form.instance.author= self.request.user
        a=Post.objects.filter(slug=self.kwargs['slug'])
        for elem in a:
            form.instance.post_name = elem        
        form.save()
        return super().form_valid(form)   
    