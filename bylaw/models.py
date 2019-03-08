from django.db import models

# Create your models here.

class GlobalDocNumber(models.Model):
    gdn = models.IntegerField(verbose_name='Глобальный номер документов')

    def __str__(self):
        return str(self.gdn)

    class Meta:
        verbose_name_plural = "Глобальный номер документов"


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
    district = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    organization = models.CharField(max_length=255, blank=True, null=True)
    inn = models.IntegerField(db_index=True)
    performer = models.CharField(max_length=255, blank=True, null=True)
    check_type = models.CharField(max_length=255, blank=True, null=True)
    date_proved_c = models.DateField()
    date_proved_po = models.DateField()
    base = models.CharField(max_length=255, blank=True, null=True)
    lab_security = models.CharField(max_length=255, blank=True, null=True)
    raspr_num = models.CharField(max_length=255, unique=False, null=True)
    who_created = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.inn)

    class Meta:
        verbose_name_plural = "Распоряжение форма"
