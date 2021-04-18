# Generated by Django 3.0.2 on 2021-04-17 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0040_auto_20210417_1141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likes',
            old_name='post_id',
            new_name='post',
        ),
        migrations.RemoveField(
            model_name='post',
            name='votes',
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweets.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_identifier',
            field=models.CharField(blank=True, default='17733', editable=False, max_length=5),
        ),
    ]