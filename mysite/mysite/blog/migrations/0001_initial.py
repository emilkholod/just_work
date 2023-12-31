# Generated by Django 4.2.7 on 2023-12-01 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.IntegerField(default=0)),
                ('title', models.CharField()),
                ('sequence', models.PositiveSmallIntegerField(default=0)),
                ('video_url', models.URLField()),
                ('subtitles_url', models.URLField()),
                ('page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.page')),
            ],
            options={
                'ordering': ['sequence', 'id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.IntegerField(default=0)),
                ('title', models.CharField()),
                ('sequence', models.PositiveSmallIntegerField(default=0)),
                ('text', models.TextField()),
                ('page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.page')),
            ],
            options={
                'ordering': ['sequence', 'id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.IntegerField(default=0)),
                ('title', models.CharField()),
                ('sequence', models.PositiveSmallIntegerField(default=0)),
                ('bitrate', models.IntegerField(default=0)),
                ('page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.page')),
            ],
            options={
                'ordering': ['sequence', 'id'],
                'abstract': False,
            },
        ),
    ]
