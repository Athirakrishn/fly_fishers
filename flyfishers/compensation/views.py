from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.shortcuts import render
from compensation.models import Compensation
from request_compensation.models import ReqCompensation
# Create your views here.


def comp(request):
    obc=""
    if request.method == 'POST':
        obj = Compensation()
        obj.title = request.POST.get('ren')
        obj.amount = request.POST.get('amt')
        # obj.rules = request.POST.get('rls')
        myfile=request.FILES['rls']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        obj.rules=myfile.name
        obj.save()
        obc = "success"
    context = {
            'msg': obc
        }
    return render(request,'compensation/compansation.html',context)


def viewcomp(request):
    obj = Compensation.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'compensation/view compansation.html',context)

def fisvcomp(request):
    obj = Compensation.objects.all()
    context = {
        'f': obj,
    }
    return render(request,'compensation/fis view compansation.html',context)

def rc(request,idd):
    obj=Compensation.objects.get(compensation_id=idd)
    obj.save()
    return render(request,'request_compensation/req comp.html')


def viwreqcom(request):
    obj = Compensation.objects.all()
    context = {
        'y': obj,
    }
    return render(request,'compensation/view,req  comp.html',context)









