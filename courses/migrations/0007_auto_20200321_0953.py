# Generated by Django 2.2.6 on 2020-03-21 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_course_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=45)),
        ),
    ]
