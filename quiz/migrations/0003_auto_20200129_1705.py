# Generated by Django 2.2.6 on 2020-01-29 17:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20200127_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='correct_answer',
            field=models.CharField(default=0, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questions',
            name='incorrect_answers',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
    ]
