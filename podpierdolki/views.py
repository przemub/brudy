from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from django.db.models import Q

from ipware import get_client_ip
from geoip import geolite2

from .models import Brudas, Donos

def main_index(request):
    return render(request, 'podpierdolki/index.html')


def add(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(request)
	
    ip = get_client_ip(request)
    #print(ip, file=environ['wsgi.errors'])
    #print("ARKA GDYNIA KURWA ŚWINIA", file=environ['wsgi.errors'])

    brudas = Brudas.objects.get_or_create(nazwa=request.POST['name'])[0]
    donos = Donos(obsmarowany=brudas, tytul=request.POST['tytul'], tresc=request.POST['tresc'])
    donos.save()

    return render(request, 'podpierdolki/index.html', {'alert': True, 'ip': ip, 'lokacja': ip})

def search(request):
    q = request.POST.get('q', '')
    f = Donos.objects.filter(Q(obsmarowany__nazwa__icontains=q) | Q(tytul__icontains=q))

    return render(request, 'podpierdolki/search.html', {'q': q, 'brudy': [f for f in f]})
