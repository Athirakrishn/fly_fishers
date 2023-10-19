from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

from django.shortcuts import render
from request_prawn_filtration.models import ReqPrawnFiltration
import datetime
def reqprawn(request):
    obc=""
    if request.method == 'POST':
        obj = ReqPrawnFiltration()
        obj.fishermen_id = 1
        obj.prawn_filtration_id = 1
        obj.license_no = request.POST.get('lin')
        # obj.description = request.POST.get('rst')
        myfile = request.FILES['rst']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.request = myfile.name
        obj.date = datetime.datetime.now()
        obj.status = 'requested'
        obj.save()
        obc = "success"
    context = {
            'msg': obc
        }
    return render(request,'request_prawn_filtration/req prawn filtration.html',context)
def viewapprawn(request):
    ss = request.session["u_id"]
    obj = ReqPrawnFiltration.objects.filter(status='Approved',fishermen_id=ss)
    context = {
        'x': obj,
    }
    return render(request,'request_prawn_filtration/view approved prawn filtration.html',context)
def mangerepr(requset):
    obj = ReqPrawnFiltration.objects.all()
    context = {
        'y': obj,
    }
    return render(requset,'request_prawn_filtration/view req prawn filtration.html',context)

def approve(request,idd):
    obj = ReqPrawnFiltration.objects.get(req_prawn_filtration_id=idd)
    obj.status = "Approved"
    obj.save()
    return mangerepr(request)
def reject(request,idd):
    obj = ReqPrawnFiltration.objects.get(req_prawn_filtration_id=idd)
    obj.status = "Rejected"
    obj.save()
    return mangerepr(request)