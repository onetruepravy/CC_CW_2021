# Generated by Django 3.0.2 on 2021-03-20 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_auto_20210317_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='expiration_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='post_author',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
