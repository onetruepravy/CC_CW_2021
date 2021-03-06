# Generated by Django 3.0.2 on 2021-04-17 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0038_auto_20210417_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='likes',
            name='post_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tweets.Post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='likes',
            name='like_or_dislike',
            field=models.CharField(choices=[('neutral', 'Neutral'), ('like', 'Like'), ('dislike', 'Dislike')], default='neutral', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_identifier',
            field=models.CharField(blank=True, default='4677', editable=False, max_length=5),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
