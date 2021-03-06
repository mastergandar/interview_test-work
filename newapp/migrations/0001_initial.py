# Generated by Django 3.2.4 on 2021-06-12 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('GraphId', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('GraphT', models.DateTimeField(null=True, verbose_name='t')),
                ('GraphFunction', models.CharField(max_length=255, verbose_name='Функция')),
                ('GraphInterval', models.IntegerField(verbose_name='глубина периода моделирования в днях')),
                ('GraphDt', models.IntegerField(verbose_name='Шаг в часах')),
                ('GraphDateTime', models.DateTimeField(null=True, verbose_name='Дата')),
            ],
        ),
    ]
