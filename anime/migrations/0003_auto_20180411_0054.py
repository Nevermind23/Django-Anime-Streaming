# Generated by Django 2.0.4 on 2018-04-10 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0002_auto_20180411_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='videos_manual',
            field=models.TextField(default='null', null=True),
        ),
        migrations.AlterField(
            model_name='episode',
            name='videos_vost',
            field=models.TextField(default='null', null=True),
        ),
    ]
