from django.db import models

'''
Ordinances menu
'''

class KoapKbkMenu(models.Model):
    koap = models.CharField(max_length=255, verbose_name='Статья КоАП РФ', unique=True, db_index=True)
    kbk = models.CharField(max_length=255, verbose_name='КБК')

    def __str__(self):
        return self.coap

    class Meta:
        verbose_name_plural = 'Статья КоАП РФ - КБК меню'


class FizOrUrMenu(models.Model):
    fiz_or_ur = models.CharField(max_length=255, verbose_name='Физ. или Юр. лицо')

    def __str__(self):
        return self.fiz_or_ur

    class Meta:
        verbose_name_plural = "Физ. или Юр. лицо меню"


class ActivityTypeMenu(models.Model):
    activity_type = models.CharField(max_length=255, verbose_name='Вид деятельности')

    def __str__(self):
        return self.activity_type

    class Meta:
        verbose_name_plural = "Вид деятельности меню"


class ViolationTypeMenu(models.Model):
    violation_type = models.CharField(max_length=255, verbose_name='Вид нарушения')

    def __str__(self):
        return self.violation_type

    class Meta:
        verbose_name_plural = "Вид нарушения меню"


"""
bylawes menu
"""


class DistrictsMenu(models.Model):
    district = models.CharField(max_length=255, verbose_name='Район')

    def __str__(self):
        return self.district

    class Meta:
        verbose_name_plural = "Районы меню"


class DepartmentsMenu(models.Model):
    department = models.CharField(max_length=255, verbose_name='Департамент')

    def __str__(self):
        return self.department

    class Meta:
        verbose_name_plural = "Департаменты меню"


class PerformersMenu(models.Model):
    performer = models.CharField(max_length=255, verbose_name='Исполнитель')

    def __str__(self):
        return self.performer

    class Meta:
        verbose_name_plural = "Исполнители меню"


class CheckTypesMenu(models.Model):
    check_type = models.CharField(max_length=255, verbose_name='Тип проверки')

    def __str__(self):
        return self.check_type

    class Meta:
        verbose_name_plural = "Тип проверок меню"

class BaseMenu(models.Model):
    base = models.CharField(max_length=255, verbose_name='Цель')

    def __str__(self):
        return self.base

    class Meta:
        verbose_name_plural = "Цель меню"


class LabSecurityMenu(models.Model):
    lab_security = models.CharField(max_length=255, verbose_name='ФБУЗ меню')

    def __str__(self):
        return self.lab_security

    class Meta:
        verbose_name_plural = "ФБУЗ меню"