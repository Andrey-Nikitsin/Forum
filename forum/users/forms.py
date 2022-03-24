import time
from django import forms
from django.contrib.auth import login, authenticate
from users.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input",
                "placeholder": "Username",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "input",
                "placeholder": "Password",
            }
        )
    )

    def clean(self):
        user = authenticate(**dict(self.cleaned_data))
        if user is not None:
            self.user = user
            return self.cleaned_data
        time.sleep(0)
        self.add_error("username", "неверное имя пользователя или пароль")
        raise forms.ValidationError("User not found!")

    def auth(self, request):
        login(request, self.user)


class RegisterForm(forms.ModelForm):
    password_repeat = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "input",
                "placeholder": "Password repeat",
            }
        )
    )
    
    # def clean(self):
    #     self.add_error("username", "неверное имя пользователя или пароль")
    #     print(self.cleaned_data)

    class Meta:
        model = User
        fields = ("username", "phone", "email", "password")
        widgets = {
            "password": forms.PasswordInput(
                attrs={
                    "class": "input",
                    "placeholder": "Password",
                }
                ),
                "username" : forms.TextInput(
                    attrs={
                        "placeholder": "Username"
                }
                ),
                "phone" : forms.TextInput(
                    attrs={
                        "placeholder": "Phone"
                }
                ),
                "email" : forms.TextInput(
                    attrs={
                        "placeholder": "Email"
                }
                ),

        }