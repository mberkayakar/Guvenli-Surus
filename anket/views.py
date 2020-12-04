from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from anket.models import Anket
from .forms import AnketForm
from django.contrib import messages

# Create your views here.


def navigasyon(request):
    result = Anket.objects.all()
    kazalar = []
    for res in result:
        kazalar.append('|'+str(res.enlem)+'|'+' '+'|'+str(res.boylam)+'|')
    return render(request,"navigasyon.html", {"kazalar": kazalar})

def anketekle(request):
    form=AnketForm(request.POST or None)
    if form.is_valid():
        Anket=form.save(commit=False)
        Anket.author=request.user
        Anket.save()
  #      messagess.success(request,"Anket Kaydedildi")
        return redirect("/")

    return render (request,"anket_ekle.html",{"form":form})

def anketyonetimi(request):
    return render (request,"anketyonetimi.html")

def anketislem(request):
    return render (request,"anketislem.html")
