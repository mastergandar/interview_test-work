# Generated by Django 3.2.4 on 2021-06-13 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='GraphImage',
            field=models.ImageField(null=True, upload_to='', verbose_name='График'),
        ),
        migrations.AddField(
            model_name='test',
            name='GraphImageEx',
            field=models.TextField(null=True, verbose_name='Exception'),
        ),
    ]
