from itertools import chain

from django.shortcuts import render, HttpResponse
from django.template.loader import render_to_string

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from bylaw.models import BylawModel
from ordinance.models import OrdinanceModel


# Create your views here.


def search(request):
    if request.is_ajax():
        search_text = request.POST['search']
        iins = BylawModel.objects.all().filter(inn__icontains=search_text)
        if not iins:
            html = render_to_string('search/search.html', {'not_found': "ИНН {} не найдено".format(search_text)})
        else:
            html = render_to_string('search/search.html', {'raspr': iins})
        return HttpResponse(html)
    else:
        search_text = request.POST['search']
        bylaw_iins = BylawModel.objects.all().filter(inn__icontains=search_text)
        bylaw_iins.model.model_name = 'Распоряжение'
        ordinance_iins = OrdinanceModel.objects.all().filter(inn__icontains=search_text)
        ordinance_iins.model.model_name = 'Постановление'
        iins = list(chain(bylaw_iins, ordinance_iins))
        print(iins)
        if not iins:
            return render(request, 'search/search.html', {'not_found': "ИНН {} не найдено".format(search_text)})
        else:
            return render(request, 'search/search.html', {'raspr': iins})