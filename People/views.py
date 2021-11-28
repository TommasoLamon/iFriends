from django.shortcuts import render
from .models import Person

def index(request):
    pList = Person.objects.all()
    return render(request, "People/index.html", {
        'list': pList
    })

def info(request, pID):
    user = Person.objects.get(id = pID)
    return render(request, "People/info.html", {
        'user': user
    })
