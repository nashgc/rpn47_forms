from django.shortcuts import render, redirect, HttpResponse, reverse
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
    if raspr_num_1:
        return render(request, 'bylaw/bylaw_form.html',
                      {'form': form, 'gdn': gdn, 'msg': msg, 'raspr_num_1': raspr_num_1, 'raspr_num_2': raspr_num_2})
    else:
        return render(request, 'bylaw/bylaw_form.html', {'form': form, 'gdn': gdn, 'msg': msg})



@login_required()
def bylaw_save(request):
    form = BylawForm(initial={'who_created': request.user.username})
    if request.method == 'POST':
        form = BylawForm(request.POST)
        if form.is_valid():
            gdn = GlobalDocNumber.objects.get(pk=1)
            gdn.gdn += 1
            gdn.save()
            raspr_num = form.cleaned_data['raspr_num'][:]
            raspr_num = raspr_num.split('/')
            form.save()
            return redirect('bylaw_form_pa',
                            msg='Распоряжение успешно сохранено.', raspr_num_1=raspr_num[0], raspr_num_2=raspr_num[1])
            # return render(request, 'bylaw/bylaw_form.html',
            #               {'msg': 'Спасибо за уделённое время! Ваш отзыв успешно отправлен.'})
        else:
            return redirect('bylaw_form_pa',
                            msg='Форма была заполненна некорректно или произошла ошибка. Попробуйте ещё раз')
            # return render(request, 'bylaw/bylaw_form.html',
            #               {'msg': 'Произошла ошибка, обновите страницу и попробуйте снова.'})
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
