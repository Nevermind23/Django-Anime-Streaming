# Generated by Django 2.0.4 on 2018-04-10 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mal_id', models.IntegerField(unique=True)),
                ('vost_id', models.IntegerField(unique=True)),
                ('slug', models.SlugField(max_length=500)),
                ('title', models.CharField(max_length=500)),
                ('geo_title', models.CharField(max_length=500)),
                ('eng_title', models.CharField(max_length=500)),
                ('jp_title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('type', models.CharField(max_length=500)),
                ('episodes', models.IntegerField()),
                ('status', models.CharField(max_length=500)),
                ('aired', models.CharField(max_length=500)),
                ('premiered', models.CharField(max_length=500)),
                ('studio', models.CharField(max_length=500)),
                ('studio_slug', models.SlugField(max_length=500)),
                ('duration', models.CharField(max_length=500)),
                ('rating', models.CharField(max_length=500)),
                ('genre', models.CharField(max_length=5000)),
                ('timer', models.IntegerField()),
                ('views', models.IntegerField()),
                ('score_rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('score_votes', models.IntegerField()),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('episode_id', models.IntegerField()),
                ('videos_vost', models.TextField()),
                ('videos_manual', models.TextField()),
                ('anime_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.Anime')),
            ],
        ),
    ]
