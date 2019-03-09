from itertools import chain

from django.shortcuts import render, HttpResponse
from django.template.loader import render_to_string
from django.template.context import RequestContext

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
    elif request.method == 'GET':
        search_text = ''
        bylaw_iins = BylawModel.objects.all().filter(inn__icontains=search_text)
        bylaw_iins.model.model_name = bylaw_iins.model.__name__
        ordinance_iins = OrdinanceModel.objects.all().filter(inn__icontains=search_text)
        ordinance_iins.model.model_name = ordinance_iins.model.__name__
        iins = list(chain(bylaw_iins, ordinance_iins))
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        paginator = Paginator(iins, 10, request=request)
        raspr = paginator.page(page)
        if not raspr:
            return render(request, 'search/search.html', {'not_found': "ИНН {} не найдено".format(search_text)})
        else:
            return render(request, 'search/search.html', {'raspr': raspr})
    else:
        search_text = request.POST['search']
        bylaw_iins = BylawModel.objects.all().filter(inn__icontains=search_text)
        bylaw_iins.model.model_name = bylaw_iins.model.__name__
        ordinance_iins = OrdinanceModel.objects.all().filter(inn__icontains=search_text)
        ordinance_iins.model.model_name = ordinance_iins.model.__name__
        iins = list(chain(bylaw_iins, ordinance_iins))
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        paginator = Paginator(iins, 10, request=request)
        raspr = paginator.page(page)
        # print(raspr)
        if not raspr:
            return render(request, 'search/search.html', {'not_found': "ИНН {} не найдено".format(search_text)})
        else:
            return render(request, 'search/search.html', {'raspr': raspr})