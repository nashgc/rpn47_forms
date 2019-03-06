from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

from .models import OrdinanceModel
from .models import GlobalDocNumber

from .form import OrdinanceForm

import qrcode
import base64
from io import BytesIO


@login_required
def ordinance_form(request, msg='', raspr_num_1='', raspr_num_2=''):
    gdn = GlobalDocNumber.objects.get(pk=1)
    form = OrdinanceForm(initial={'who_created': request.user.username})
    if raspr_num_1 and raspr_num_2:
        raspr_num = '{}/{}'.format(raspr_num_1, raspr_num_2)
        return render(request, 'ordinance/ordinance_form.html',
                        {'form': form, 'gdn': gdn, 'msg': msg, 'raspr_num': raspr_num, 'print_btn': 'print_btn'})
    else:
        return render(request, 'ordinance/ordinance_form.html',
                        {'form': form, 'gdn': gdn, 'msg': msg})


@login_required
def ordinance_save(request):
    form = OrdinanceForm(initial={'who_created': request.user.username})
    if request.method == 'POST':
        form = OrdinanceForm(request.POST)
        if form.is_valid():
            gdn = GlobalDocNumber.objects.get(pk=1)
            raspr_num = form.cleaned_data['raspr_num'][:]
            raspr_num = raspr_num.split('/')
            ordinance = form.save(commit=False)
            if not ordinance.department:
                ordinance.department = 'Не заполненно'
            if not ordinance.district:
                ordinance.district = 'Не заполненно'
            if not ordinance.check_type:
                ordinance.check_type = 'Не заполненно'
            if not ordinance.performer:
                ordinance.performer = 'Не заполненно'
            if not ordinance.fiz_or_ur:
                ordinance.fiz_or_ur = 'Не заполненно'
            if not ordinance.activity_type:
                ordinance.activity_type = 'Не заполненно'
            if not ordinance.violation_type:
                ordinance.violation_type = 'Не заполненно'
            if not ordinance.koap_article:
                ordinance.koap_article = 'Не заполненно'
            raspr_num_list = ordinance.raspr_num.split('-')
            raspr_num_list[3] = str(gdn).zfill(4)
            ordinance.raspr_num = '-'.join(raspr_num_list)
            ordinance.save()
            gdn.gdn += 1
            gdn.save()
            return ordinance_form(request, msg='Распоряжение успешно сохранено.',
                                  raspr_num_1=raspr_num[0], raspr_num_2=raspr_num[1])
        else:
            return ordinance_form(request, msg='Форма была заполненна некорректно или произошла ошибка. Попробуйте ещё раз')
    return render(request, 'ordinance/ordinance_form.html', {'form': form})


@login_required()
def ordinance_print(request, raspr_num=''):
    if request.method == 'POST':
        obj = OrdinanceModel.objects.get(raspr_num__exact=request.POST['raspr_num'])
        data = 'Lastname=obj.fio_official_face obj.passport_data|PayerAddress=Санкт-Петербург|OKTMO=40913000|CBC=obj.kbk|Purpose=штрафы 78-02-1-0700-18|UIN=|Sum=obj.fine_sum|Category=4815573529'
        img = qrcode.make(data)

        buffered = BytesIO()
        img.save(buffered, format="PNG")

        img_str = base64.b64encode(buffered.getvalue())
        return render(request, 'ordinance/print_form.htm', {'ord_raw': obj, 'qrcode': img_str.decode('utf-8')})