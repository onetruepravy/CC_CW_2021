# Generated by Django 3.0.2 on 2021-04-10 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0030_auto_20210410_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_identifier',
            field=models.CharField(blank=True, default='54121', editable=False, max_length=5),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
