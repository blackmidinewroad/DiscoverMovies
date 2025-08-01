# Generated by Django 5.2.4 on 2025-07-23 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedb', '0051_alter_movie_adult_movie_moviedb_mov_adult_14eec7_idx'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='movie',
            name='moviedb_mov_adult_14eec7_idx',
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(max_length=32),
        ),
    ]
