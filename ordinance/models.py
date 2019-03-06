from django.db import models

# Create your models here.

class GlobalDocNumber(models.Model):
    gdn = models.IntegerField(verbose_name='Глобальный номер документов')

    def __str__(self):
        return str(self.gdn)

    class Meta:
        verbose_name_plural = "Глобальный номер документов"


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


class KoapArticleMenu(models.Model):
    koap_article = models.CharField(max_length=255, verbose_name='Статья КоАП РФ')

    def __str__(self):
        return self.koap_article

    class Meta:
        verbose_name_plural = "Статья КоАП РФ меню"


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