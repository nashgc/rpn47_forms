# Generated by Django 2.1.5 on 2019-01-17 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bylaw', '0015_auto_20190117_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bylawmodel',
            name='base',
            field=models.CharField(default='Unfilled', max_length=255),
        ),
        migrations.AlterField(
            model_name='bylawmodel',
            name='lab_security',
            field=models.CharField(default='Unfilled', max_length=255),
        ),
    ]
