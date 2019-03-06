from django.contrib import admin

from .models import OrdinanceModel, ActivityTypeMenu, FizOrUrMenu, KoapArticleMenu, ViolationTypeMenu, GlobalDocNumber

# Register your models here.


class OrdinanceAdmin(admin.ModelAdmin):
    list_display = ('inn', 'organization', 'raspr_num')
    list_filter = ('ordinance_date', )
    search_fields = ('inn', 'organization', 'raspr_num')

ordinance_models = [
    ActivityTypeMenu, FizOrUrMenu, KoapArticleMenu, ViolationTypeMenu, GlobalDocNumber
]

admin.site.register(OrdinanceModel, OrdinanceAdmin)
admin.site.register(ordinance_models)