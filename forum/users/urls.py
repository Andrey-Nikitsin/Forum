from django.urls import path
from django.shortcuts import redirect
from users.views import UsersView, login_user, RegisterView, log_out


urlpatterns = [
    path("users/", UsersView.as_view(), name="all_users"),
    path("login/", login_user, name="user_login"),
    path("register/", RegisterView.as_view(), name="register_user"),
    path("logout/", log_out, name="logout_page"),
    path("", lambda request: redirect("all_users"))
]