from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .form import BylawForm
from .models import BylawModel, GlobalDocNumber

import json

# Create your views here.

@login_required
def bylaw_form(request, msg='', raspr_num_1='', raspr_num_2=''):
    gdn = GlobalDocNumber.objects.get(pk=1)
    form = BylawForm(initial={'who_created': request.user.username})
    if raspr_num_1 and raspr_num_2:
        raspr_num = '{}/{}'.format(raspr_num_1, raspr_num_2)
        return render(request, 'bylaw/bylaw_form.html',
                      {'form': form, 'gdn': gdn, 'msg': msg, 'raspr_num': raspr_num})
    else:
        return render(request, 'bylaw/bylaw_form.html', {'form': form, 'gdn': gdn, 'msg': msg})



@login_required
def bylaw_save(request):
    form = BylawForm(initial={'who_created': request.user.username})
    if request.method == 'POST':
        form = BylawForm(request.POST)
        if form.is_valid():
            gdn = GlobalDocNumber.objects.get(pk=1)
            raspr_num = form.cleaned_data['raspr_num'][:]
            raspr_num = raspr_num.split('/')
            bylaw = form.save(commit=False)
            if not bylaw.district:
                bylaw.district = 'Не заполненно'
            if not bylaw.department:
                bylaw.department = 'Не заполненно'
            if not bylaw.performer:
                bylaw.performer = 'Не заполненно'
            if not bylaw.check_type:
                bylaw.check_type = 'Не заполненно'
            raspr_num_list = bylaw.raspr_num.split('-')
            raspr_num_list[3] = str(gdn).zfill(4)
            bylaw.raspr_num = '-'.join(raspr_num_list)
            bylaw.save()
            gdn.gdn += 1
            gdn.save()
            return bylaw_form(request, msg='Распоряжение успешно сохранено.',
                              raspr_num_1=raspr_num[0], raspr_num_2=raspr_num[1])
        else:
            return bylaw_form(request, msg='Форма была заполненна некорректно или произошла ошибка. Попробуйте ещё раз')
    return render(request, 'bylaw/bylaw_form.html', {'form': form})



@login_required
def get_inn(request):
    if request.method == "POST":
        request = request.POST
        # print(request['search'])
        iins = BylawModel.objects.all().filter(inn__icontains=request['search'])
        results = []
        for inn in iins:
            place_json = {}
            place_json['label'] = inn.inn
            place_json['org'] = inn.organization
            results.append(place_json)
        data = json.dumps(results)
        mimetype = "application/json"
        return HttpResponse(data, mimetype)
