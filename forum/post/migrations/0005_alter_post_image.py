# Generated by Django 3.2.8 on 2022-03-27 17:50

from django.db import migrations, models
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20220327_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to=post.models.Post.file_path),
        ),
    ]