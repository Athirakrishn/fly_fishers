from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.shortcuts import render
from prawn_filtration.models import PrawnFiltration

def addprawn(request):
     obc=""
     if request.method == 'POST':
        obj = PrawnFiltration()
        obj.available_date = request.POST.get('avd')
        # obj.details = request.POST.get('det')
        myfile = request.FILES['det']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.details = myfile.name
        obj.save()
        obc = "success"
     context = {
            'msg': obc
        }
     return render(request,'prawn_filtration/add prawn filtration.html',context)


def viewprawn(request):
    obj = PrawnFiltration.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'prawn_filtration/view prawn filtration.html',context)
def fisvprn(request):
    obj = PrawnFiltration.objects.all()
    context = {
        'o': obj,
    }
    return render(request,'prawn_filtration/fisv prawn filtration.html',context)

