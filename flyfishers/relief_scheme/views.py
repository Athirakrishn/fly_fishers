from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.shortcuts import render
from relief_scheme.models import ReliefSchem
from request_releif_scheme.models import ReqReliefScheme

def mngreli(request):
    obj = ReliefSchem.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'relief_scheme/mng req relief.html',context)

def relif(request):
    obc=''
    if request.method == 'POST':
        obj = ReliefSchem()
        obj.scheme_name = request.POST.get('scm')
        # obj.description = request.POST.get('des')
        myfile = request.FILES['des']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.description = myfile.name
        obj.save()
        obc = "success"
    context = {
            'msg': obc
        }
    return render(request,'relief_scheme/relief schem.html',context)

def reqrelif(request):
    obj = ReliefSchem.objects.all()
    context = {
        'z': obj,
    }
    return render(request,'relief_scheme/view,reqrelifschem.html',context)

def reqrlf(request,idd):
    obj=ReliefSchem.objects.get(relief_schem_id=idd)
    obj.save()
    return render(request,'request_relief_scheme/req_reliefe_scheme.html')


