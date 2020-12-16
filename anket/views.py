from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404
from django.contrib.auth.models import User
from .models import Anket
from .forms import AnketForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/user/giris")
def navigasyon(request):
    result = Anket.objects.all()
    kazalar = []
    for res in result:
        kazalar.append('|'+str(res.enlem)+'|'+' '+'|'+str(res.boylam)+'|')
    return render(request,"navigasyon.html", {"kazalar": kazalar})




@login_required(login_url="/user/giris")
def anketekle(request):
    form=AnketForm(request.POST or None)
    
    if form.is_valid():
        Anket=form.save(commit=False)
        Anket.author=request.user
        Anket.save()
  #      messagess.success(request,"Anket Kaydedildi")
        return redirect("/anket/anketyonetimi/")

    return render (request,"anket_ekle.html",{"form":form})



@login_required(login_url="/user/giris")
def anketyonetimi(request):
    return render (request,"anketyonetimi.html")


    
@login_required(login_url="/user/giris")
def anketislem(request):
    newAnket=Anket.objects.filter(author=request.user)
    return render (request,"anketislem.html",{"newAnket":newAnket})

def anketdetay(request,id):
  
    newAnket=get_list_or_404(Anket,id=id)
    newAnket=newAnket[0]
    return render (request,"anketdetay.html",{"newAnket":newAnket})


def anketsil(request,id):
    anket=get_object_or_404(Anket,id=id)
    anket.delete()
    return redirect ("/anket/anketislem/")


 
    


 
def anketguncelle(request,id):
    
 
    anket=get_object_or_404(Anket,id=id)
#    anket=anket[0]
    form = AnketForm(request.POST or None , request.FILES or None , instance=anket)
    if form.is_valid():
        print("form is valide e girildi kanks")
        anket= form.save(commit=False)
        anket.author=request.user
        anket.save()
        print("anket.save e gelindi")
        return redirect("/")
   
    return render (request,"anketguncelle.html",{"form":form})
 
   
 