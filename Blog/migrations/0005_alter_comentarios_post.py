# Generated by Django 4.0.3 on 2022-04-27 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_alter_posts_contenido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='Blog.posts'),
        ),
    ]