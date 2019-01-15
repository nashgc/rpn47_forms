from django.contrib import admin

from .models import BylawModel, CheckTypesMenu, DepartmentsMenu, DistrictsMenu, PerformersMenu, GlobalDocNumber
# Register your models here.


# Register your models here.


class BylawAdmin(admin.ModelAdmin):
    list_display = ('raspr_date', 'district', 'department', 'organization', 'inn', 'performer', 'check_type',
                    'date_proved_c', 'date_proved_po', 'raspr_num', 'who_created')
    list_filter = ('raspr_date', 'date_proved_c', 'date_proved_po')
    search_fields = ('inn', 'organization', 'raspr_num')


bylaw_models = [CheckTypesMenu, DepartmentsMenu, DistrictsMenu, PerformersMenu, GlobalDocNumber]
admin.site.register(BylawModel,BylawAdmin)
admin.site.register(bylaw_models)
