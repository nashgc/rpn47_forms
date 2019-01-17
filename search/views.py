from django.shortcuts import render, HttpResponse
from django.template.loader import render_to_string
from django.template.context import RequestContext
from bylaw.models import BylawModel

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
        iins = BylawModel.objects.all().filter(inn__icontains=search_text)
        if not iins:
            return render(request, 'search/search.html', {'not_found': "ИНН {} не найдено".format(search_text)})
        else:
            return render(request, 'search/search.html', {'raspr': iins})
