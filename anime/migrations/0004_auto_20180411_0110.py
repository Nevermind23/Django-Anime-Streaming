# Generated by Django 2.0.4 on 2018-04-10 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0003_auto_20180411_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='timer',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='episode',
            name='videos_manual',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='episode',
            name='videos_vost',
            field=models.TextField(blank=True, null=True),
        ),
    ]