# Generated by Django 3.0.2 on 2021-04-17 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0039_auto_20210417_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_identifier',
            field=models.CharField(blank=True, default='65643', editable=False, max_length=5),
        ),
    ]
