from django.contrib import admin

from .models import OrdinanceModel, ActivityTypeMenu, FizOrUrMenu, KoapArticleMenu, ViolationTypeMenu

# Register your models here.


class OrdinanceAdmin(admin.ModelAdmin):
    list_display = ('inn', 'organization', 'raspr_num')
    list_filter = ('ordinance_date', )
    search_fields = ('inn', 'organization', 'raspr_num')

ordinance_models = [
    ActivityTypeMenu, FizOrUrMenu, KoapArticleMenu, ViolationTypeMenu
]

admin.site.register(OrdinanceModel, OrdinanceAdmin)
admin.site.register(ordinance_models)