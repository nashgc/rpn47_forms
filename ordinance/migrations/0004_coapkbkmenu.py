# Generated by Django 2.1.5 on 2019-03-08 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordinance', '0003_globaldocnumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoapKbkMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coap', models.CharField(max_length=255, unique=True, verbose_name='Статья КоАП РФ')),
                ('kbk', models.CharField(max_length=255, unique=True, verbose_name='КБК')),
            ],
            options={
                'verbose_name_plural': 'Статья КоАП РФ - КБК меню',
            },
        ),
    ]
