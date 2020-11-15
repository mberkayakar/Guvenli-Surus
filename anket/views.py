from django.shortcuts import render

from django.contrib.auth.models import User
from anket.models import Anket

# Create your views here.

def index(request):
    return render(request,"index.html")

def navigasyon(request):
    result = Anket.objects.all()
    kazalar = []
    for res in result:
        kazalar.append('|'+str(res.enlem)+'|'+' '+'|'+str(res.boylam)+'|')
    return render(request,"navigasyon.html", {"kazalar": kazalar})