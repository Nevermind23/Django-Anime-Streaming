# Generated by Django 2.0.4 on 2018-04-10 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0009_auto_20180411_0142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='episode',
            old_name='anime_id',
            new_name='anime',
        ),
        migrations.AlterField(
            model_name='anime',
            name='timer',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='episode',
            unique_together={('anime', 'episode_id')},
        ),
    ]