# Generated by Django 2.1.5 on 2019-03-08 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordinance', '0005_auto_20190308_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coapkbkmenu',
            name='kbk',
            field=models.CharField(max_length=255, verbose_name='КБК'),
        ),
    ]
