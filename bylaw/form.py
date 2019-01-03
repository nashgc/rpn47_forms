from django.forms import ModelForm, ModelChoiceField, DateInput, Select, TextInput
from .models import BylawModel, DistrictsMenu, DepartmentsMenu, PerformersMenu, CheckTypesMenu


# TODO: disable required fields
class BylawForm(ModelForm):
    district = ModelChoiceField(queryset=DistrictsMenu.objects.all(), to_field_name="district",
                                widget=Select(attrs={'id': "district", 'class': 'form-control col-6', 'required':"false"}))
    department = ModelChoiceField(queryset=DepartmentsMenu.objects.all(), to_field_name="department",
                                  widget=Select(attrs={'id':"department", 'class': "form-control col-6", 'required':"false"}))
    performer = ModelChoiceField(queryset=PerformersMenu.objects.all(), to_field_name="performer",
                                 widget=Select(attrs={'id': "performer", 'class': 'form-control col-6', 'required':"false"}))
    check_type = ModelChoiceField(queryset=CheckTypesMenu.objects.all(), to_field_name="check_type",
                                  widget=Select(attrs={'id': "check_type", 'class': 'form-control col-6', 'required':"false"}))


    class Meta:
        model = BylawModel
        fields = ['raspr_date', 'district', 'department', 'organization', 'inn',
                  'performer', 'check_type', 'date_proved', 'raspr_num', 'who_created'
        ]
        widgets = {
            'raspr_date': DateInput(
                attrs={'type': "text", 'class': "form-control col-6", 'id':"raspr_date", 'required':"false"}
            ),
            'organization': TextInput(
                attrs={'type': "text", 'class': "form-control col-6 org", 'id': "organization", 'required':"false"}
            ),
            'inn': TextInput(
                attrs={'type': "text", 'required':"gfggfgfgfg", 'class': "form-control col-6", 'id': "inn"}
            ),
            'date_proved': DateInput(
                attrs={'type': "text", 'class': "form-control col-6", 'id': "date_proved", 'required':"false"}
            )
        }