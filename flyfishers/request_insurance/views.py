from django.shortcuts import render
from django.shortcuts import render
from request_insurance.models import ReqInsurance
from vessel.models import Vessel
from django.core.files.storage import FileSystemStorage
# Create your views here.
def mngreqinsu(request):
    obj = ReqInsurance.objects.filter(status="Requested")
    context = {
        'x': obj,
    }
    return render(request,'request_insurance/mng req insurance.html',context)

def approve(request,idd):
    obj=ReqInsurance.objects.get(req_insurance_id=idd)
    obj.status="Approved"
    obj.save()
    return mngreqinsu(request)
def reject(request,idd):
    obj = ReqInsurance.objects.get(req_insurance_id=idd)
    obj.status = "Rejected"
    obj.save()
    return mngreqinsu(request)



def status(request):
    ss = request.session["u_id"]
    obj = ReqInsurance.objects.filter(status='Approved',fishermen_id=ss)
    context = {
        'z': obj,
    }
    return render(request,'request_insurance/sinsu.html',context)

# def reqinsu(request):
#     obj = ReqInsurance.objects.all()
#     context = {
#         'z': obj,
#     }
#     return render(request,'request_insurance/reqinsu.html',context)

def reins(request,idd):
    ob=Vessel.objects.all()
    context={
        'x':ob
    }
    obc=""
    if request.method=='POST':
       obj = ReqInsurance()
       obj.insurance_id=idd
       obj.fishermen_id = 1
       obj.vessel_id=request.POST.get('vss')
       myfile = request.FILES['idp']
       fs = FileSystemStorage()
       filename = fs.save(myfile.name, myfile)
       obj.id_proof = myfile.name
       obj.status="Requested"
       # obj.proof = request.POST.get('prf')
       obj.save()
       obc = "success"
    context = {
           'msg': obc,
            'x': ob
       }
    return render(request,'request_insurance/reqinsu.html',context)

