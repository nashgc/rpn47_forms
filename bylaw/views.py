from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .form import BylawForm
from .models import BylawModel, GlobalDocNumber

import json

# Create your views here.

@login_required
def bylaw_form(request):
    gdn = GlobalDocNumber.objects.get(pk=1)
    form = BylawForm(initial={'who_created': request.user.username})
    return render(request, 'bylaw/bylaw_form.html', {'form': form, 'gdn': gdn})


@login_required()
def bylaw_save(request):
    form = BylawForm(initial={'who_created': request.user.username})
    if request.method == 'POST':
        form = BylawForm(request.POST)
        if form.is_valid():
            gdn = GlobalDocNumber.objects.get(pk=1)
            gdn.gdn += 1
            gdn.save()
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
