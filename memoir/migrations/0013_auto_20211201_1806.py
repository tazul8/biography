# Generated by Django 3.2.9 on 2021-12-01 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memoir', '0012_auto_20211201_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='hire_me_url',
            field=models.CharField(default='http://127.0.0.1:8000', max_length=500),
        ),
        migrations.AddField(
            model_name='banner',
            name='read_more_url',
            field=models.CharField(default='http://127.0.0.1:8000', max_length=500),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_url',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='social_media_url',
            field=models.CharField(max_length=500),
        ),
    ]
