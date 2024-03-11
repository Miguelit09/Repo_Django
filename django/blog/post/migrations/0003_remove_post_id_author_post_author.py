# Generated by Django 5.0.3 on 2024-03-11 17:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_author_post_id_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='id_author',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='post.author'),
        ),
    ]
