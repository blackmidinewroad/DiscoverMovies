# Generated by Django 5.2.4 on 2025-07-03 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedb', '0003_remove_movie_genre_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdb_id',
            field=models.CharField(blank=True, default='', max_length=16),
        ),
        migrations.AlterField(
            model_name='movie',
            name='original_title',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='movie',
            name='overview',
            field=models.CharField(blank=True, default='', max_length=1024),
        ),
        migrations.AlterField(
            model_name='movie',
            name='spoken_languages',
            field=models.CharField(blank=True, default='', max_length=1024),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tagline',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=256),
        ),
    ]
