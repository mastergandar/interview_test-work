# Generated by Django 3.2.4 on 2021-06-14 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0007_auto_20210614_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='GraphFuncId',
            field=models.CharField(default='', max_length=255, verbose_name='TaskId'),
        ),
    ]
