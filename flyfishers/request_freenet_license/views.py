from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.shortcuts import render
from request_freenet_license.models import ReqFreenetLicense
import datetime
from freenet_license.models import FreenetLicence

# Create your views here.
def mngfree(request):
    obj = ReqFreenetLicense.objects.all()
    context = {
        'y': obj,
    }
    return render(request,'request_freenet_license/mng free net.html',context)

def approve(request,idd):
    obj=ReqFreenetLicense.objects.get(req_freenet_license_id=idd)
    obj.status="Approved"
    obj.save()
    return mngfree(request)
def reject(request,idd):
    obj=ReqFreenetLicense.objects.get(req_freenet_license_id=idd)
    obj.status = "Rejected"
    obj.save()

    return mngfree(request)


def viewappreqfree(request):
    ss = request.session["u_id"]
    obj = ReqFreenetLicense.objects.filter(status="Approved",fishermen_id=ss)
    context = {
        'x': obj,
    }
    return render(request,'request_freenet_license/view app req free net.html',context)

def reqfree(request,idd):
    obj=ReqFreenetLicense.objects.all()

    abc=''
    if request.method == 'POST':
        obj = ReqFreenetLicense()
        obj.fishermen_id = 1
        obj.freenet_licence_id=idd
        obj.date = datetime.datetime.now()
        # obj.id_proof=request.POST.get('idp')
        myfile = request.FILES['idp']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.id_proof = myfile.name
        myfile = request.FILES['yyy']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.more_details = myfile.name

        obj.status="Requested"
        obj.save()
        abc="success"
    context = {
            'msg': abc,
            'ff': obj
        }
    return render(request,'request_freenet_license/req freenet licence.html',context)




# Create your views here.



