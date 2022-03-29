# Generated by Django 3.2.8 on 2022-03-28 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0005_alter_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commit', models.TextField(max_length=70)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name_author', to=settings.AUTH_USER_MODEL, verbose_name='comit_author')),
                ('post_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post', verbose_name='name_post')),
            ],
            options={
                'verbose_name': 'Commit',
                'db_table': 'Commit',
            },
        ),
    ]