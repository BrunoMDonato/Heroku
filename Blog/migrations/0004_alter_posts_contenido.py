# Generated by Django 4.0.3 on 2022-04-26 22:24

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_posts_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='contenido',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
