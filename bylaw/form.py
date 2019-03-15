from django.forms import ModelForm, ModelChoiceField, DateInput, Select, TextInput, DateField, CharField
from .models import BylawModel
from references.models import DistrictsMenu, DepartmentsMenu, PerformersMenu, CheckTypesMenu, LabSecurityMenu, BaseMenu


# TODO: disable required fields
class BylawForm(ModelForm):
    raspr_date = DateField(required=False,
                           widget=DateInput(attrs={'type': "text", 'class': "form-control col-6", 'id': "raspr_date"}))

    district = ModelChoiceField(required=True, queryset=DistrictsMenu.objects.all(), to_field_name="district",
                                widget=Select(attrs={'id': "district", 'class': 'form-control col-6'}))

    department = ModelChoiceField(required=True, queryset=DepartmentsMenu.objects.all(), to_field_name="department",
                                  widget=Select(attrs={'id':"department", 'class': "form-control col-6"}))

    organization = CharField(required=False, widget=TextInput(
                attrs={'type': "text", 'class': "form-control col-6 org", 'id': "organization"}))

    inn = CharField(required=True, widget=TextInput(
                attrs={'type': "text", 'minlength': '10', 'maxlength': '12', 'class': "form-control col-6", 'id': "inn"}))

    performer = ModelChoiceField(required=False, queryset=PerformersMenu.objects.all(), to_field_name="performer",
                                 widget=Select(attrs={'id': "performer", 'class': 'form-control col-6'}))

    check_type = ModelChoiceField(required=False, queryset=CheckTypesMenu.objects.all(), to_field_name="check_type",
                                  widget=Select(attrs={'id': "check_type", 'class': 'form-control col-6'}))

    date_proved_c = DateField(required=False,
                        widget=DateInput(attrs={'type': "text", 'class': "form-control col-6", 'id': "date_proved_c"}))

    date_proved_po = DateField(required=False,
                        widget=DateInput(attrs={'type': "text", 'class': "form-control col-6", 'id': "date_proved_po"}))

    base = ModelChoiceField(required=False, queryset=BaseMenu.objects.all(), to_field_name="base",
                                  widget=Select(attrs={'id': "base", 'class': 'form-control col-6'}))

    lab_security = ModelChoiceField(required=False, queryset=LabSecurityMenu.objects.all(), to_field_name="lab_security",
                                  widget=Select(attrs={'id': "lab_security", 'class': 'form-control col-6'}))




    class Meta:
        model = BylawModel
        fields = ['raspr_date', 'district', 'department', 'organization', 'inn',
                  'performer', 'check_type', 'date_proved_c', 'date_proved_po',
                  'base', 'lab_security', 'raspr_num', 'who_created'
        ]
        widgets = {
            # 'raspr_date': DateInput(
            #     attrs={'type': "text", 'class': "form-control col-6", 'id':"raspr_date", 'required':"false"}
            # ),
            # 'organization': TextInput(
            #     attrs={'type': "text", 'class': "form-control col-6 org", 'id': "organization", 'required':"false"}
            # ),
            # 'inn': TextInput(
            #     attrs={'type': "text", 'required':"gfggfgfgfg", 'class': "form-control col-6", 'id': "inn"}
            # ),
            # 'date_proved': DateInput(
            #     attrs={'type': "text", 'class': "form-control col-6", 'id': "date_proved", 'required':"false"}
            # ),
            'raspr_num': TextInput(
                attrs={'type': "text", 'class': "form-control col-10", 'id': "raspr_num", 'readonly': ''}
            ),
            'who_created': TextInput(
                attrs={'type': "text", 'class': "form-control col-10", 'id': "who_created", 'readonly': ''}
            )
        }