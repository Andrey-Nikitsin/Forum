from django.shortcuts import render
from post.models import Post, Category
from django.views.generic import ListView
from post.forms import PostForm, CatForm
from django.shortcuts import redirect
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic import FormView
from django.urls import reverse


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
        print(form.is_valid)
        if form.is_valid():
            form.save()
            return redirect("all_posts")
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


# class new_post(FormView):
#     form_class = PostForm
#     template_name = 'new_post.html'
    
#     def get_success_url(self) -> str:
#         next_url = self.request.GET.get("next")
#         if next_url is not None:
#             return next_url
#         return reverse("all_users")

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

def new_post(request):
    context = {"form": PostForm()}
    if request.method == "POST":
        copy_post = request.POST.copy()
        copy_post["author"] = request.user
        form = PostForm(copy_post, request.FILES)
        print(form.is_valid)
        if form.is_valid():
            form.save()
            return redirect("all_posts")
        context.update(form=form)
    return render(request, "new_post.html", context)


# def single_post(request, url):
#     try:
#         context = {
#             "post": Post.objects.get(url=url)
#         }
#     except Post.DoesNotExist:
#         raise Http404("Post not found.")
#     except Post.MultipleObjectsReturned:
#         ...
#     if request.META.get("HTTP_REFERER"):
#         context.update(back=request.META["HTTP_REFERER"])
#     context["post"].views += 1
#     context["post"].save()

#     # print(request.META)

#     return render(request, "single_post.html", context)


class PostDetail(DetailView):
    model = Post
    template_name="single_post.html"


    def single_post(self):
        d = self.kwargs['slug']
        context = { "post": Post.objects.get(slug=d)}
        context["post"].views += 1
        context["post"].save()