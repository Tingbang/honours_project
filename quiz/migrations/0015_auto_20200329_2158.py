# Generated by Django 2.2.6 on 2020-03-29 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0014_auto_20200329_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
