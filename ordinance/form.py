from django.forms import Form, ModelForm, ModelChoiceField, DateInput, Select, TextInput, DateField, CharField
from .models import OrdinanceModel, FizOrUrMenu, ActivityTypeMenu, ViolationTypeMenu, KoapArticleMenu
from bylaw.models import DistrictsMenu, DepartmentsMenu, PerformersMenu, CheckTypesMenu


# TODO: disable required fields
class OrdinanceForm(ModelForm):

    department = ModelChoiceField(required=False, queryset=DepartmentsMenu.objects.all(), to_field_name="department",
                                  widget=Select(attrs={'id':"department", 'class': "form-control col-6"}))

    district = ModelChoiceField(required=False, queryset=DistrictsMenu.objects.all(), to_field_name="district",
                                widget=Select(attrs={'id': "district", 'class': 'form-control col-6'}))

    ordinance_date = DateField(required=False,
                           widget=DateInput(attrs={'type': "text", 'class': "form-control col-6", 'id': "ordinance_date"}))

    pay_date = DateField(required=False,
                           widget=DateInput(attrs={'type': "text", 'class': "form-control col-6", 'id': "pay_date"}))

    expiration = CharField(required=False, widget=TextInput(
                attrs={'type': "text", 'class': "form-control col-6", 'id': "expiration"}))

    fact_pay_date = DateField(required=False,
                           widget=DateInput(attrs={'type': "text", 'class': "form-control col-6", 'id': "fact_pay_date"}))

    income_receipt_date = DateField(required=False,
                           widget=DateInput(attrs={'type': "text", 'class': "form-control col-6", 'id': "income_receipt_date"}))

    organization = CharField(required=False, widget=TextInput(
                attrs={'type': "text", 'class': "form-control col-6", 'id': "organization"}))

    fio_official_face = CharField(required=False, widget=TextInput(
                attrs={'type': "text", 'class': "form-control col-6", 'id': "fio_official_face"}))

    passport_data = CharField(required=False, widget=TextInput(
                attrs={'type': "text", 'class': "form-control col-6", 'id': "passport_data"}))

    inn = CharField(required=True, widget=TextInput(
                attrs={'type': "text", 'class': "form-control col-6", 'id': "inn"}))

    protocol_date = DateField(required=False,
                           widget=DateInput(attrs={'type': "text", 'class': "form-control col-6", 'id': "protocol_date"}))

    check_type = ModelChoiceField(required=False, queryset=CheckTypesMenu.objects.all(), to_field_name="check_type",
                                  widget=Select(attrs={'id': "check_type", 'class': 'form-control col-6'}))

    performer = ModelChoiceField(required=False, queryset=PerformersMenu.objects.all(), to_field_name="performer",
                                 widget=Select(attrs={'id': "performer", 'class': 'form-control col-6'}))

    fiz_or_ur = ModelChoiceField(required=False, queryset=FizOrUrMenu.objects.all(), to_field_name="fiz_or_ur",
                                 widget=Select(attrs={'id': "fiz_or_ur", 'class': 'form-control col-6'}))

    activity_type = ModelChoiceField(required=False, queryset=ActivityTypeMenu.objects.all(), to_field_name="activity_type",
                                 widget=Select(attrs={'id': "activity_type", 'class': 'form-control col-6'}))

    violation_type = ModelChoiceField(required=False, queryset=ViolationTypeMenu.objects.all(), to_field_name="violation_type",
                                 widget=Select(attrs={'id': "violation_type", 'class': 'form-control col-6'}))

    koap_article = ModelChoiceField(required=False, queryset=KoapArticleMenu.objects.all(), to_field_name="koap_article",
                                 widget=Select(attrs={'id': "koap_article", 'class': 'form-control col-6'}))

    fine_sum = CharField(required=False, widget=TextInput(
                attrs={'type': "text", 'class': "form-control col-6", 'id': "fine_sum"}))

    payed = CharField(required=False, widget=TextInput(
                attrs={'type': "text", 'class': "form-control col-6", 'id': "payed"}))

    debt = CharField(required=False, widget=TextInput(
                attrs={'type': "text", 'class': "form-control col-6", 'id': "debt"}))

    dont_take_by_court_decision = CharField(required=False, widget=TextInput(
                attrs={'type': "text", 'class': "form-control col-6", 'id': "dont_take_by_court_decision"}))

    kbk = CharField(required=False, widget=TextInput(
                attrs={'type': "text", 'class': "form-control col-6", 'id': "kbk"}))

    kpp = CharField(required=False, widget=TextInput(
                attrs={'type': "text", 'class': "form-control col-6", 'id': "kpp"}))

    uin_formed = CharField(required=False, widget=TextInput(
                attrs={'type': "text", 'class': "form-control col-6", 'id': "uin_formed"}))


    class Meta:
        model = OrdinanceModel
        fields = ['department', 'ordinance_date', 'pay_date', 'expiration', 'fact_pay_date',
                  'income_receipt_date', 'organization', 'fio_official_face', 'passport_data', 'inn',
                  'protocol_date', 'check_type', 'performer', 'fiz_or_ur', 'activity_type', 'violation_type',
                  'koap_article', 'fine_sum', 'payed', 'debt', 'dont_take_by_court_decision', 'kbk',
                  'kpp', 'uin_formed', 'raspr_num', 'who_created'
        ]
        widgets = {
            'raspr_num': TextInput(
                attrs={'type': "text", 'class': "form-control col-10", 'id': "raspr_num", 'readonly': ''}
            ),
            'who_created': TextInput(
                attrs={'type': "text", 'class': "form-control col-10", 'id': "who_created", 'readonly': ''}
            )
        }