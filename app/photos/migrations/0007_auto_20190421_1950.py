# Generated by Django 2.1.7 on 2019-04-21 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0006_auto_20190417_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='photos'),
        ),
    ]
