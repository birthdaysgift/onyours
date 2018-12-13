# Generated by Django 2.0.7 on 2018-12-06 10:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0014_postdislike_postlike'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoDislike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('userphoto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.UserPhoto')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('userphoto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.UserPhoto')),
            ],
        ),
    ]