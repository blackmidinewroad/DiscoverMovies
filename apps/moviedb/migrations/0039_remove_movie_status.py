# Generated by Django 5.2.4 on 2025-07-14 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviedb', '0038_alter_moviecast_options_alter_moviecrew_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='status',
        ),
    ]
