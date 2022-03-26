from cProfile import label
from logging import PlaceHolder
import time
from django import forms
from django.contrib.auth import login, authenticate
from users.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "reg__form-input",
                "placeholder": "Username",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "reg__form-input",
                "placeholder": "Password",
            }
        )
    )

    def clean(self):
        user = authenticate(**dict(self.cleaned_data))
        if user is not None:
            self.user = user
            return self.cleaned_data
        time.sleep(1)
        self.add_error("username", "неверное имя пользователя или пароль")
        raise forms.ValidationError("User not found!")

    def auth(self, request):
        login(request, self.user)


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'reg__form-input'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'placeholder': 'Password repeat', 'class': 'reg__form-input'}))
    phone = forms.CharField(label='Номер телефона', widget=forms.TextInput(attrs={'placeholder': 'Phone', 'class': 'reg__form-input'}))
    
    class Meta:
        model = User
        fields = ("username", "phone", "email", "password1", "password2")
        widgets = {
            "password1": forms.PasswordInput(
                attrs={
                    'class': 'reg__form-input',
                    "placeholder": "Password",
                }
                ),
                "username" : forms.TextInput(
                    attrs={
                        'class': 'reg__form-input', 
                        "placeholder": "Username"
                }
                ),
                "phone" : forms.TextInput(
                    attrs={
                        'class': 'reg__form-input',
                        "placeholder": "Phone"
                }
                ),
                "email" : forms.TextInput(
                    attrs={
                        'class': 'reg__form-input',
                        "placeholder": "Email"
                }
                ),

        }