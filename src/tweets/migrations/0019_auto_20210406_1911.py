# Generated by Django 3.0.2 on 2021-04-06 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0018_auto_20210406_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_identifier',
            field=models.CharField(blank=True, default='20308', editable=False, max_length=5, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
