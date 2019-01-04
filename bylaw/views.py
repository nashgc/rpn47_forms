from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .form import BylawForm
from .models import BylawModel

import json

# Create your views here.

@login_required
def bylaw_form(request):
    form = BylawForm(initial={'who_created': request.user.username, 'raspr_num': '78-___-____/28-___-2019'})
    return render(request, 'bylaw/bylaw_form.html', {'form': form})


@login_required()
def bylaw_save(request):
    form = BylawForm(initial={'who_created': request.user.username, 'raspr_num': '78-___-____/28-___-2019'})
    if request.method == 'POST':
        form = BylawForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'bylaw/bylaw_form.html',
                          {'msg': 'Спасибо за уделённое время! Ваш отзыв успешно отправлен.'})
        else:
            return render(request, 'bylaw/bylaw_form.html',
                          {'msg': 'Произошла ошибка, обновите страницу и попробуйте снова.'})
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
