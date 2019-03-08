from django.db import models

# Create your models here.
class GlobalDocNumber(models.Model):
    gdn = models.IntegerField(verbose_name='Глобальный номер документов ')

    def __str__(self):
        return str(self.gdn)

    class Meta:
        verbose_name_plural = "Глобальный номер документов"


class OrdinanceModel(models.Model):


    department = models.CharField(max_length=255, default='Unfilled')
    district = models.CharField(max_length=255, default='Unfilled')
    ordinance_date = models.DateField()
    pay_date = models.DateField()
    expiration = models.CharField(max_length=255)
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
    fine_sum = models.CharField(max_length=255)
    payed = models.CharField(max_length=255)
    debt = models.CharField(max_length=255)
    dont_take_by_court_decision = models.CharField(max_length=255)
    kbk = models.CharField(max_length=255)
    kpp = models.CharField(max_length=255)
    uin_formed = models.CharField(max_length=255)
    raspr_num = models.CharField(max_length=255, unique=True)
    who_created = models.CharField(max_length=255)

    def __str__(self):
        return str(self.inn)

    class Meta:
        verbose_name_plural = "Постановление форма"