# Generated by Django 5.2.4 on 2025-07-14 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviedb', '0039_remove_movie_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='status_int',
            new_name='status',
        ),
    ]
