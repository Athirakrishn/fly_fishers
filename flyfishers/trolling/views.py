from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.shortcuts import render
from trolling.models import Trolling
import datetime
def viewtroling(request):
    obj = Trolling.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'trolling/view troling info.html',context)

def addtroling(request):
    obc=""
    if request.method == 'POST':
        obj = Trolling()
        # obj.trolling_info = request.POST.get('trf')
        myfile = request.FILES['trf']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.trolling_info = myfile.name
        obj.starting_date = datetime.datetime.now()
        obj.ending_date = datetime.datetime.now()
        obj.save()
        obc = "success"
    context = {
            'msg': obc
        }
    return render(request,'trolling/add troling info.html',context)

def managetroling(request):
    obj = Trolling.objects.all()
    context = {
        'y': obj,
    }
    return render(request,'trolling/managetrol.html',context)
def delete(request,idd):
    obj=Trolling.objects.get(trolling_id=idd)
    obj.delete()
    return managetroling(request)






