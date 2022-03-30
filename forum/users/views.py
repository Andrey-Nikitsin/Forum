import json
from django.shortcuts import redirect
from users.models import User
from users.forms import LoginForm, RegisterForm
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView
from django.urls import reverse
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required



class UsersView(ListView):
    paginate_by = 2
    model = User
    template_name = "users.html"


class RegisterView(FormView):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = "/posts/all/"

    # def get_success_url(self) -> str:
    #     next_url = self.request.GET.get("next")
    #     if next_url is not None:
    #         return next_url
    #     return reverse("all_users")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


def login_user(request):
    if request.user.is_authenticated:
        return redirect("all_users")
    context = {"login_form": LoginForm()}
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            login_form.auth(request)
            return redirect("all_posts")
        context.update(login_form=login_form)
    return render(request, "login.html", context)



def log_out(request):
    logout(request)
    return redirect("all_theme")