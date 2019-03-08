from django.contrib import admin

from .models import BaseMenu, LabSecurityMenu, CheckTypesMenu, DepartmentsMenu, DistrictsMenu,\
    PerformersMenu, ActivityTypeMenu, FizOrUrMenu, ViolationTypeMenu, CoapKbkMenu

bylaw_models = [
    CheckTypesMenu, DepartmentsMenu, DistrictsMenu, PerformersMenu, LabSecurityMenu, BaseMenu,
    ActivityTypeMenu, FizOrUrMenu, ViolationTypeMenu, CoapKbkMenu
]


admin.site.register(bylaw_models)