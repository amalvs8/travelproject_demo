from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import TeamMember

# Create your views here.

def demo1(request):
    return HttpResponse("Helloo")

def demo(request):
    obj1 = Place.objects.all()
    obj2 = TeamMember.objects.all()
    return render(request, 'index.html', {'result': obj1, 'member': obj2})


