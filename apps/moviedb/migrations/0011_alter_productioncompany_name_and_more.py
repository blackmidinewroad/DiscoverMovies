# Generated by Django 5.2.4 on 2025-07-04 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedb', '0010_remove_productioncompany_origin_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productioncompany',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='productioncompany',
            name='slug',
            field=models.SlugField(blank=True, max_length=130, unique=True),
        ),
        migrations.AddIndex(
            model_name='country',
            index=models.Index(fields=['name'], name='moviedb_cou_name_7f2602_idx'),
        ),
        migrations.AddIndex(
            model_name='genre',
            index=models.Index(fields=['name'], name='moviedb_gen_name_4a4077_idx'),
        ),
        migrations.AddIndex(
            model_name='language',
            index=models.Index(fields=['name'], name='moviedb_lan_name_e1fe74_idx'),
        ),
        migrations.AddIndex(
            model_name='productioncompany',
            index=models.Index(fields=['name'], name='moviedb_pro_name_7fb449_idx'),
        ),
    ]
