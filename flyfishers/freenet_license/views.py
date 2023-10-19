from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

from django.shortcuts import render
from freenet_license.models import FreenetLicence
from  request_freenet_license.models import ReqFreenetLicense


def addfree(request):
    obc=""
    if request.method == 'POST':
        obj = FreenetLicence()

        obj.type_of_net = request.POST.get('typ')
        # obj.description = request.POST.get('Des')
        myfile = request.FILES['Des']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.description = myfile.name
        obj.save()
        obc = "success"
    context = {
            'msg': obc
        }
    return render(request,'freenet_license/add freenet.html',context)

def vfree(request):
    obj = FreenetLicence.objects.all()
    context = {
        'y': obj,
    }
    return render(request,'freenet_license/view,req freenet.html',context)

def ref(request,idd):
    obj = FreenetLicence.objects.get(freenet_licence_id=idd)
    obj.save()
    return render(request,'request_freenet_license/req freenet licence.html')

def fisvfree(request):
    obj = FreenetLicence.objects.all()
    context = {
        'y': obj,
    }
    return render(request,'freenet_license/fisview,req freenet.html',context)
