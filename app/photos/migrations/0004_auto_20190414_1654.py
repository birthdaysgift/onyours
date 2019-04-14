# Generated by Django 2.1.7 on 2019-04-14 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20190413_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userphoto',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posted_photos', to=settings.AUTH_USER_MODEL),
        ),
    ]
