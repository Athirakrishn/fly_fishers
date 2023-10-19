from django.shortcuts import render
from django.shortcuts import render
from vessel.models import Vessel

# Create your views here.

def vessel(request):
    abc=''
    if request.method == 'POST':
        obj = Vessel()
        obj.fishermen_id = 1
        obj.fishermen_name = request.POST.get('fsn')
        obj.name_of_vessel = request.POST.get('vsl')
        obj.register_no = request.POST.get('rgn')
        obj.license_no = request.POST.get('lisn')
        obj.crew = request.POST.get('crw')
        obj.year = request.POST.get('yar')
        obj.register_date = request.POST.get('regd')
        obj.register_place = request.POST.get('regp')
        obj.detailed_description =request.POST.get('dtd')
        obj.status='Requested'
        obj.save()
        abc="success"
    context={
        'msg':abc
    }
    return render(request,'vessel/vessel.html',context)
def vrifd(request):
    obj = Vessel.objects.all()
    context = {
        'u': obj,
    }
    return render(request,'vessel/verified.html',context)

def verifyvessel(request):
    obj = Vessel.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'vessel/verifyvessel.html',context)

def verify(request,idd):
    obj=Vessel.objects.get(vessel_id=idd)
    obj.status="Verified"
    obj.save()
    return verifyvessel(request)
def reject(request,idd):
    obj = Vessel.objects.get(vessel_id=idd)
    obj.status = "Rejected"
    obj.save()
    return verifyvessel(request)