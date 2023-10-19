from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
def depty(request):
    return render(request,'temp/deputydirector.html')
def dierctr(request):
    return render(request,'temp/director.html')
def fismn(request):
    return render(request,'temp/fishermen.html')
def hom(request):
    return render(request,'temp/home.html')
def malsyaofficer(request):
    return render(request,'temp/Matsya_Bhavan_Officer.html')
def abt(request):
    return render(request,'temp/aboutt.html')
def fiabt(request):
    return render(request,'temp/fiabout.html')
