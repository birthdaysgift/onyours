# Generated by Django 2.0.7 on 2018-12-09 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0018_auto_20181209_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendship',
            name='user1',
        ),
        migrations.RemoveField(
            model_name='friendship',
            name='user2',
        ),
        migrations.AlterUniqueTogether(
            name='friendshiprequest',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='friendshiprequest',
            name='from_user',
        ),
        migrations.RemoveField(
            model_name='friendshiprequest',
            name='to_user',
        ),
        migrations.DeleteModel(
            name='Friendship',
        ),
        migrations.DeleteModel(
            name='FriendshipRequest',
        ),
    ]