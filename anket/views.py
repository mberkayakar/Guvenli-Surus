from django.shortcuts import render,redirect,get_list_or_404
from django.contrib.auth.models import User
from .models import Anket
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
    newAnket=Anket.objects.filter(author=request.user)
    return render (request,"anketislem.html",{"newAnket":newAnket})

def anketdetay(request,id):
    newAnket=Anket.objects.filter(id=id).first()
    newAnket=get_list_or_404(Anket,id=id)
    return render (request,"anketdetay.html",{"newAnket":newAnket})