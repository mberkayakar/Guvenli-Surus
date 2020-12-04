from django.shortcuts import render,redirect
 
def index(request):
    return render(request,"index.html")
def hakkında(request):
    return render(request,"hakkında.html")

