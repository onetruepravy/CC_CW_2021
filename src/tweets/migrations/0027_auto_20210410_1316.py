# Generated by Django 3.0.2 on 2021-04-10 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0026_auto_20210410_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='tweets.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_identifier',
            field=models.CharField(blank=True, default='5784', editable=False, max_length=5, unique=True),
        ),
    ]
