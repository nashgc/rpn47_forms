# Generated by Django 2.1.4 on 2019-03-08 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityTypeMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(max_length=255, verbose_name='Вид деятельности')),
            ],
            options={
                'verbose_name_plural': 'Вид деятельности меню',
            },
        ),
        migrations.CreateModel(
            name='BaseMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base', models.CharField(max_length=255, verbose_name='Базис')),
            ],
            options={
                'verbose_name_plural': 'Базис меню',
            },
        ),
        migrations.CreateModel(
            name='CheckTypesMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_type', models.CharField(max_length=255, verbose_name='Тип проверки')),
            ],
            options={
                'verbose_name_plural': 'Тип проверок меню',
            },
        ),
        migrations.CreateModel(
            name='CoapKbkMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coap', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Статья КоАП РФ')),
                ('kbk', models.CharField(max_length=255, verbose_name='КБК')),
            ],
            options={
                'verbose_name_plural': 'Статья КоАП РФ - КБК меню',
            },
        ),
        migrations.CreateModel(
            name='DepartmentsMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=255, verbose_name='Департамент')),
            ],
            options={
                'verbose_name_plural': 'Департаменты меню',
            },
        ),
        migrations.CreateModel(
            name='DistrictsMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=255, verbose_name='Район')),
            ],
            options={
                'verbose_name_plural': 'Районы меню',
            },
        ),
        migrations.CreateModel(
            name='FizOrUrMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fiz_or_ur', models.CharField(max_length=255, verbose_name='Физ. или Юр. лицо')),
            ],
            options={
                'verbose_name_plural': 'Физ. или Юр. лицо меню',
            },
        ),
        migrations.CreateModel(
            name='LabSecurityMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_security', models.CharField(max_length=255, verbose_name='Лабораторное обеспечение')),
            ],
            options={
                'verbose_name_plural': 'Лабораторное обеспечение меню',
            },
        ),
        migrations.CreateModel(
            name='PerformersMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('performer', models.CharField(max_length=255, verbose_name='Исполнитель')),
            ],
            options={
                'verbose_name_plural': 'Исполнители меню',
            },
        ),
        migrations.CreateModel(
            name='ViolationTypeMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('violation_type', models.CharField(max_length=255, verbose_name='Вид нарушения')),
            ],
            options={
                'verbose_name_plural': 'Вид нарушения меню',
            },
        ),
    ]