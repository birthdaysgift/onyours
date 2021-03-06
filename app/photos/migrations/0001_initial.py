# Generated by Django 2.0.7 on 2018-12-08 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='')),
                ('thumbnail', models.ImageField(default='', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoDislike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos_user_dislike', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos_user_like', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos_photo', to='photos.Photo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='photolike',
            name='userphoto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos_userphoto_like', to='photos.UserPhoto'),
        ),
        migrations.AddField(
            model_name='photodislike',
            name='userphoto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos_userphoto_dislike', to='photos.UserPhoto'),
        ),
    ]
