# Generated by Django 3.0.2 on 2021-04-17 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0045_auto_20210417_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_identifier',
            field=models.CharField(blank=True, default='62552', editable=False, max_length=5),
        ),
    ]
