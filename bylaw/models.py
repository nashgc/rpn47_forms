from django.db import models

# Create your models here.

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


class BylawModel(models.Model):

    # district_list = (
    #     ('Московский', 'Московский'),
    #     ('Выборгский', 'Выборгский'),
    #     ('Невский', 'Невский'),
    #     ('Адмиралтейский', 'Адмиралтейский'),
    #     ('Приморский', 'Приморский'),
    #     ('Кировский', 'Кировский'),
    #     ('Управление', 'Управление'),
    # )
    #
    # department_list = (
    #     ('01_Орготдел', '01_Орготдел'),
    #     ('03_ЗПП', '03_ЗПП'),
    #     ('04_Транспорт', '04_Транспорт'),
    #     ('05_Коммуналка', '05_Коммуналка'),
    #     ('06_Труд', '06_Труд'),
    #     ('07_Дети', '07_Дети'),
    #     ('08_Питание', '08_Питание'),
    #     ('09_Эпид', '09_Эпид'),
    #     ('10_Жалобы', '10_Жалобы'),
    #     ('11_Радиологи', '11_Радиологи'),
    #     ('12_Бухгалтерия', '12_Бухгалтерия'),
    #     ('15_Юристы', '15_Юристы'),
    # )
    #
    # performer_list = (
    #     ('РоманцоваВ.Л.', 'РоманцоваВ.Л.'),
    #     ('ЗаботинаИ.А.', 'ЗаботинаИ.А.'),
    # )
    #
    # check_type_list = (
    #     ('Плановая_выездная', 'Плановая_выездная'),
    #     ('Внеплановая_выездная', 'Внеплановая_выездная'),
    #     ('Внеплановая_документарная', 'Внеплановая_документарная'),
    # )


    raspr_date = models.DateField()
    district = models.CharField(max_length=255, blank=True)
    department = models.CharField(max_length=255, blank=True)
    organization = models.CharField(max_length=255, blank=True)
    inn = models.IntegerField()
    performer = models.CharField(max_length=255, blank=True)
    check_type = models.CharField(max_length=255, blank=True)
    date_proved = models.DateField(blank=True)
    raspr_num = models.CharField(max_length=255, blank=True)
    who_created = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name_plural = "Распоряжение форма"
