# Generated by Django 5.2.4 on 2025-07-04 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedb', '0004_alter_movie_imdb_id_alter_movie_original_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('code', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'countries',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('code', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'languages',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['name'], 'verbose_name_plural': 'genres'},
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['title', '-release_date'], 'verbose_name_plural': 'movies'},
        ),
        migrations.AlterModelOptions(
            name='productioncompany',
            options={'ordering': ['name'], 'verbose_name_plural': 'production companies'},
        ),
        migrations.AddField(
            model_name='movie',
            name='imdb_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='kp_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='lb_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='tmdb_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='original_language',
            field=models.CharField(blank=True, default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='movie',
            name='production_countries',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='productioncompany',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
