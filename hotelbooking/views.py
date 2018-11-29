from django.shortcuts import render
from .models import Hotels
# Create your views here.
def openHomePage(request):
    type="home"
    return render(request,"index.html",{"type":type})
def openUserLogin(request):
    type=request.GET.get("type")
    return render(request,"index.html",{"type":type})
def openUserRegister(request):
    type=request.GET.get("type")
    return render(request,"index.html",{"type":type})