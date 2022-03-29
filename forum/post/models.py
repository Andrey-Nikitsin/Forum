from email.policy import default
from typing_extensions import Required

from django.db import models
from users.models import User
from django.db.models.signals import pre_save, pre_delete
from django.dispatch.dispatcher import receiver
from random import randint
from datetime import datetime
from django.conf import settings
import os
from django.urls import reverse


class Category(models.Model):
    name_category = models.TextField(max_length=50)

    def __str__(self) -> str:
        return self.name_category

    class Meta:
        db_table = "Category"
        verbose_name = "Category"

class Post(models.Model):
    def file_path(self, filename):
        file_type = filename.split(".")[-1]
        path_file = datetime.strftime(datetime.now(), "post/%Y/%m/%d/%H/")
        return path_file + str(randint(100000000, 999999999)) + "." + file_type

    title = models.CharField(max_length=256, unique=True, verbose_name="Post title")
    author = models.ForeignKey(
        User,
        related_name="posts",
        on_delete=models.CASCADE,
        verbose_name="Post author",
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="category")
    text = models.TextField(verbose_name="Post data")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Post created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Post update")
    is_moderated = models.BooleanField(default=False)
    views = models.BigIntegerField(default=0)
    image = models.ImageField(blank=True, upload_to=file_path)
    slug = models.SlugField(max_length=256, unique=True, verbose_name="Link to Post")

    def __str__(self) -> str:
        return self.slug
        # return (self.title[:20] + "...") if len(self.title) > 20 else self.title

    class Meta:
        db_table = "posts"
        verbose_name = "Post"
        ordering=("-id",)
    


class Comment(models.Model):
    commit = models.TextField(max_length=70)
    post_name = models.ForeignKey(Post, blank=True, on_delete=models.CASCADE, verbose_name="name_post")
    author = models.ForeignKey(User, blank=True, related_name="name_author", on_delete=models.CASCADE, verbose_name="comit_author")
    created = models.DateTimeField(auto_now_add=True, verbose_name="comment_created")

    def __str__(self) -> str:
        return self.commit

    class Meta:
        db_table = "Commit"
        verbose_name = "Commit"
    
    
@receiver(pre_delete, sender=Post)
def hash_passwd(sender, instance, **kwargs):
    path_to_file = settings.BASE_DIR / str(instance.image.path)
    try:
        path_to_file.unlink()
    except Exception:
        print("HON FOUND")


@receiver(pre_save, sender=Post)
def to_url(sender, instance, **kwargs):
    def ttu(title):
        return title.replace(" ", "_").lower()

    # if (instance.id is None) or (instance.url != ttu(instance.title)):
    #     instance.url = ttu(instance.title)
    #     print(instance.url, "\n\n\n")
