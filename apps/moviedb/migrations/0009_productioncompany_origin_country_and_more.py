# Generated by Django 5.2.4 on 2025-07-04 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedb', '0008_movie_origin_country_alter_country_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productioncompany',
            name='origin_country',
            field=models.ManyToManyField(blank=True, related_name='origin_country_company', to='moviedb.country'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='origin_country',
            field=models.ManyToManyField(blank=True, related_name='origin_country_movie', to='moviedb.country'),
        ),
    ]
