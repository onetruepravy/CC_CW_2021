# Generated by Django 3.0.2 on 2021-04-08 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0023_auto_20210407_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tweets.Author'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='post_identifier',
            field=models.CharField(blank=True, default='38852', editable=False, max_length=5, unique=True),
        ),
    ]
