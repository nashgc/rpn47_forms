from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

from .form import BylawForm
from .models import BylawModel

import json

# Create your views here.

@login_required
def bylaw_form(request):
    return render(request, 'bylaw/bylaw_form.html', {'form': BylawForm})

@login_required()
def bylaw_save(request):
    form = BylawForm
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


# @login_required
def get_inn(request):
    if request.method == "POST":
        request = request.POST
        print('First req - '.format(request))
        # print(request['search'])
        iins = BylawModel.objects.all().filter(inn__icontains=request['search'])
        results = []
        for inn in iins:
            print(inn)
            place_json = {}
            place_json['label'] = inn.inn
            place_json['org'] = inn.organization
            results.append(place_json)
        print('JSON - '.format(results))
        data = json.dumps(results)
        print('DATA -'.format(data))
        mimetype = "application/json"
        return HttpResponse(data, mimetype)
