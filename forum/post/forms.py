from django import forms
from post.models import Post


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
            # "tags": forms.Select(
            #     attrs={
            #         'class': 'cteate-post__select'
            #     }
            # ),
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