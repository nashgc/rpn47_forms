from django.shortcuts import render
from bylaw.models import BylawModel

# Create your views here.


def search(request):
    if request.method == 'POST':
        search_text = request.POST['search']
        iins = BylawModel.objects.all().filter(inn__icontains=search_text)
        print(iins)
        return render(request, 'search/search.html', {'raspr': iins})
    else:
        return render(request, 'search/search.html')
