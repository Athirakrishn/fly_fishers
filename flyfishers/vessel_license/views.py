from django.shortcuts import render
from django.shortcuts import render
from vessel_license.models import VesselLicense



def addves(request):
    obc=""
    if request.method == 'POST':
        obj = VesselLicense()
        obj.type_of_vessel = request.POST.get('type')
        obj.license_type = request.POST.get('lcst')
        obj.save()
        obc = "success"
    context = {
            'msg': obc
        }
    return render(request,'vessel_license/add vessel license.html',context)
def viewves(request):
    obj = VesselLicense.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'vessel_license/view vessel licence.html',context)
def fisvwves(request):
    obj = VesselLicense.objects.all()
    context = {
        'y': obj,
    }
    return render(request,'vessel_license/fisvw vessel licence.html',context)




