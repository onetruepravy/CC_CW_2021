# Generated by Django 3.0.2 on 2021-04-06 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0015_auto_20210320_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upvote', models.PositiveIntegerField(default=0)),
                ('downvote', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='downvote',
        ),
        migrations.RemoveField(
            model_name='post',
            name='upvote',
        ),
        migrations.AlterField(
            model_name='post',
            name='post_identifier',
            field=models.CharField(blank=True, default='17699', editable=False, max_length=5, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweets.Author'),
        ),
    ]