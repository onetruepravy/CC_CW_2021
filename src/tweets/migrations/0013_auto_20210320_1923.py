# Generated by Django 3.0.2 on 2021-03-20 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0012_auto_20210320_1859'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Topics',
        ),
        migrations.AddField(
            model_name='post',
            name='downvote',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='upvote',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_identifier',
            field=models.CharField(blank=True, default='41386', editable=False, max_length=5, unique=True),
        ),
    ]
