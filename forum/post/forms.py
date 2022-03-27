from pyexpat import model
from unicodedata import category
from django import forms
from post.models import Post, Category


class CatForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ("Category",)
        widgets = {
            "name_category": forms.TextInput(
                attrs={
                    'class': 'cteate-post__input'
                })}

    def clean(self):
        print(self.cleaned_data)

        return self.cleaned_data



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ("created", "updated", "is_moderated", "views", "url")
        widgets = {
            "title": forms.TextInput(
                attrs={
                    'class': 'cteate-post__input'
                },                
            ),
            "category": forms.Select(
                attrs={
                    'class': 'cteate-post__select'
                }
            ),
            "text": forms.Textarea(
                attrs={
                    'class': 'cteate-post__input'
                    
                }
            ),
            "image": forms.FileInput(
                attrs={
                    'class': 'cteate-post__input-file'
                }
            ),
            "slug": forms.TextInput(
                attrs={
                    'class': 'cteate-post__input'
                }
            ),
            }

    def clean(self):
        print(self.cleaned_data)

        return self.cleaned_data