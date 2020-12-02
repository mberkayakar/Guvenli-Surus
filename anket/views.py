from django.shortcuts import render
from django.contrib.auth.models import User
from anket.models import Anket


# Create your views here.


def navigasyon(request):
    result = Anket.objects.all()
    kazalar = []
    for res in result:
        kazalar.append('|'+str(res.enlem)+'|'+' '+'|'+str(res.boylam)+'|')
    return render(request,"navigasyon.html", {"kazalar": kazalar})

def anketekle(request):
    return render (request,"anket_ekle.html")