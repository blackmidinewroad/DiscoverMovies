# Generated by Django 5.2.4 on 2025-07-09 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedb', '0030_movie_directors_movie_is_documentary_movie_is_short_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='is_documentary',
            new_name='documentary',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='is_short',
            new_name='short',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='is_tv_movie',
            new_name='tv_movie',
        ),
        migrations.AlterField(
            model_name='movie',
            name='directors',
            field=models.ManyToManyField(blank=True, related_name='directed_movies', to='moviedb.person', verbose_name='Directed by'),
        ),
    ]
