from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from django.db.models import Q

from .models import Brudas, Donos

def main_index(request):
    return render(request, 'podpierdolki/index.html')


def add(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(request)

    brudas = Brudas.objects.get_or_create(nazwa=request.POST['name'])[0]
    donos = Donos(obsmarowany=brudas, tytul=request.POST['tytul'], tresc=request.POST['tresc'])
    donos.save()

    return render(request, 'podpierdolki/index.html', {'alert': True})

def search(request):
    q = request.POST.get('q', '')
    f = Donos.objects.filter(Q(obsmarowany__nazwa__icontains=q) | Q(tytul__icontains=q))

    return render(request, 'podpierdolki/search.html', {'q': q, 'brudy': [f for f in f]})