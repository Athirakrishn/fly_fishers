from django.shortcuts import render
from django.shortcuts import render
from request_vessel_license.models import ReqVesselLicense

def req_ves1(request):
    obc=""
    if request.method == 'POST':
        obj = ReqVesselLicense()
        obj.vessel_license_id = 1
        obj.fishermen_id = 1
        obj.name = request.POST.get('nam')
        obj.vessel_no = request.POST.get('vsl')
        obj.request = request.POST.get('rst')
        obj.id_proof = request.POST.get('prf')
        obj.manifacture_date = request.POST.get('mnf')
        obj.status = 'requested'
        obj.save()
        obc = "success"
    context = {
            'msg': obc
        }
    return render(request,'request_vessel_license/re for vessel license.html',context)
def viwmngreqvessel(request):
    obj = ReqVesselLicense.objects.filter(status="Requested")
    context = {
        'y': obj,
    }
    return render(request,'request_vessel_license/view,mng req for vessel license.html',context)
def approve(request,idd):
    obj=ReqVesselLicense.objects.get(req_vessel_license_id=idd)
    obj.status="Approved"
    obj.save()
    return viwmngreqvessel(request)
def reject(request,idd):
    obj=ReqVesselLicense.objects.get(req_vessel_license_id=idd)
    obj.status = "Rejected"
    obj.save()
    return viwmngreqvessel(request)


def viwappvessel(request):
    ss = request.session["u_id"]
    obj = ReqVesselLicense.objects.filter(status='Approved',fishermen_id=ss)
    context = {
        'x': obj,
    }
    return render(request,'request_vessel_license/view  approved vessel licence .html',context)


