# Generated by Django 2.0.7 on 2018-11-29 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_auto_20181128_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
