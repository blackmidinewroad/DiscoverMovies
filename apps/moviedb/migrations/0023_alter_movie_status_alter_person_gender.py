# Generated by Django 5.2.4 on 2025-07-07 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedb', '0022_alter_movieengagement_tmdb_popularity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='status',
            field=models.CharField(blank=True, choices=[('', 'Undefined'), ('Rumored', 'Rumored'), ('Planned', 'Planned'), ('In Production', 'In Production'), ('Post Production', 'Post Production'), ('Released', 'Released'), ('Canceled', 'Canceled')], default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(blank=True, choices=[('', 'Unknown'), ('F', 'Female'), ('M', 'Male'), ('NB', 'Non-binary')], default='', max_length=2),
        ),
    ]
