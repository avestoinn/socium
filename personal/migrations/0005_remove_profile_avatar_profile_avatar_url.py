# Generated by Django 4.0.4 on 2022-06-02 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_profile_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='avatar',
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar_url',
            field=models.URLField(default='#'),
            preserve_default=False,
        ),
    ]
