from django.db import models

# Create your models here.


class OrdinanceModel(models.Model):

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


    ordinance_date = models.DateField()
    pay_date = models.DateField()
    expiration = models.IntegerField()
    fact_pay_date = models.DateField()
    income_receipt_date = models.DateField()
    organization = models.CharField(max_length=255)
    fio_official_face = models.CharField(max_length=255)
    passport_data = models.CharField(max_length=255)
    inn = models.IntegerField()
    protocol_date = models.DateField()
    check_type = models.CharField(max_length=255)
    performer = models.CharField(max_length=255)
    fiz_or_ur = models.CharField(max_length=255)
    activity_type = models.CharField(max_length=255)
    violation_type = models.CharField(max_length=255)
    koap_article = models.CharField(max_length=255)
    fine_sum = models.IntegerField()
    payed = models.IntegerField()
    debt = models.IntegerField()
    dont_take_by_court_decision = models.CharField(max_length=255)
    kbk = models.IntegerField()
    kpp = models.IntegerField()
    uin_formed = models.CharField(max_length=255)
    raspr_num = models.CharField(max_length=255, unique=True)
    who_created = models.CharField(max_length=255)

    def __str__(self):
        return str(self.inn)

    class Meta:
        verbose_name_plural = "Распоряжение форма"