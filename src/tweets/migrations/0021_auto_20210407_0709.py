# Generated by Django 3.0.2 on 2021-04-07 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0020_auto_20210406_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_identifier',
            field=models.CharField(blank=True, default='37684', editable=False, max_length=5, unique=True),
        ),
    ]
