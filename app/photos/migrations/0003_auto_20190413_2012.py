# Generated by Django 2.1.7 on 2019-04-13 20:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photos', '0002_auto_20181208_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photodislike',
            name='user',
        ),
        migrations.RemoveField(
            model_name='photodislike',
            name='userphoto',
        ),
        migrations.RemoveField(
            model_name='photolike',
            name='user',
        ),
        migrations.RemoveField(
            model_name='photolike',
            name='userphoto',
        ),
        migrations.AddField(
            model_name='userphoto',
            name='users_who_disliked',
            field=models.ManyToManyField(related_name='disliked_photos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userphoto',
            name='users_who_liked',
            field=models.ManyToManyField(related_name='liked_photos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='PhotoDislike',
        ),
        migrations.DeleteModel(
            name='PhotoLike',
        ),
    ]