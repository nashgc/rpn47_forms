from django.contrib import admin

from .models import OrdinanceModel, GlobalDocNumber

# Register your models here.


class OrdinanceAdmin(admin.ModelAdmin):
    list_display = ('ordinance_date', 'district', 'department', 'inn', 'organization', 'fio_official_face',
'passport_data', 'protocol_date', 'check_type', 'performer', 'fiz_or_ur', 'activity_type', 'violation_type',
'koap_article', 'fine_sum', 'dont_take_by_court_decision', 'kbk', 'debt', 'raspr_num', 'who_created')

    list_filter = ('ordinance_date', )
    search_fields = ('inn', 'organization', 'fio_official_face', 'raspr_num')


admin.site.register(OrdinanceModel, OrdinanceAdmin)
admin.site.register(GlobalDocNumber)





# unused, but still in a model
# 'pay_date', 'expiration', 'fact_pay_date', 'income_receipt_date', 'payed', 'kpp','uin_formed',
