# Generated by Django 2.0.4 on 2018-04-10 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0010_auto_20180411_0203'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='poster',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
