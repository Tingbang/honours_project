# Generated by Django 3.0.3 on 2020-03-20 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20200319_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='additional_content_1',
            field=models.CharField(blank=True, default='', max_length=1500),
        ),
        migrations.AddField(
            model_name='lesson',
            name='additional_content_2',
            field=models.CharField(blank=True, default='', max_length=1500),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='all_the_content',
            field=models.CharField(max_length=1500),
        ),
    ]