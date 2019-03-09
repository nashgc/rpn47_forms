from django.contrib import admin

from .models import BaseMenu, LabSecurityMenu, CheckTypesMenu, DepartmentsMenu, DistrictsMenu,\
    PerformersMenu, ActivityTypeMenu, FizOrUrMenu, ViolationTypeMenu, KoapKbkMenu

bylaw_models = [
    CheckTypesMenu, DepartmentsMenu, DistrictsMenu, PerformersMenu, LabSecurityMenu, BaseMenu,
    ActivityTypeMenu, FizOrUrMenu, ViolationTypeMenu, KoapKbkMenu
]


admin.site.register(bylaw_models)