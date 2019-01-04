from django.contrib import admin

from .models import BylawModel, CheckTypesMenu, DepartmentsMenu, DistrictsMenu, PerformersMenu, GlobalDocNumber
# Register your models here.

admin.site.register(BylawModel)
admin.site.register(CheckTypesMenu)
admin.site.register(DepartmentsMenu)
admin.site.register(DistrictsMenu)
admin.site.register(PerformersMenu)
admin.site.register(GlobalDocNumber)
