from django.shortcuts import render
from django.shortcuts import render
from request_releif_scheme.models import ReqReliefScheme
from relief_scheme.models import ReliefSchem
from django.core.files.storage import FileSystemStorage


# Create your views here.

def request_reliefe(request,idd):
    obb=ReliefSchem.objects.all()
    context={
        'hh':obb
    }
    obc=""
    if request.method=='POST':
        obj=ReqReliefScheme()
        obj.fishermen_id=1
        obj.relief_schem_id=idd
        # obj.id_proof=request.POST.get('prf')
        myfile=request.FILES['prf']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        obj.id_proof=myfile.name
        obj.status="Requested"
        obj.save()
        # return render(request,'relief_scheme/view,reqrelifschem.html')
        obc = "success"
    context = {
            'msg': obc,
        'hh': obb

        }
    return render(request,'request_relief_scheme/req_reliefe_scheme.html',context)

def mngreqrelief(request):
    obj = ReqReliefScheme.objects.filter(status="Requested")
    context = {
        'x': obj,
    }
    return render(request,'request_relief_scheme/mng req relief.html',context)

def approve(request,idd):
    obj=ReqReliefScheme.objects.get(req_relief_schem_id=idd)
    obj.status="Approved"
    obj.save()
    return mngreqrelief(request)
def reject(request,idd):
    obj = ReqReliefScheme.objects.get(req_relief_schem_id=idd)
    obj.status = "Rejected"
    obj.save()
    return mngreqrelief(request)


def viewapprelief(request):
    ss=request.session["u_id"]
    obj = ReqReliefScheme.objects.filter(status='Approved',fishermen_id=ss)
    context = {
        'y': obj,
    }
    return render(request,'request_relief_scheme/view approved relief.html',context)





