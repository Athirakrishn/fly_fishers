from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.shortcuts import render
from insurance.models import Insurance
from request_insurance.models import ReqInsurance


def insu(request):
    obc=""
    if request.method == 'POST':
        obj = Insurance()
        obj.insurance_name = request.POST.get('insurance')
        # obj.description = request.POST.get('Description')
        myfile = request.FILES['Description']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.description = myfile.name
        obj.save()
        obc = "success"
    context = {
            'msg': obc
        }
    return render(request,'insurance/insurance.html',context)

def viewreqinsu(request):
    obj = Insurance.objects.all()
    context = {
        'y': obj,
    }
    return render(request,'insurance/view,reqinsurance.html',context)

def rin(request,idd):
    obj=Insurance.objects.get(insurance_id=idd)
    obj.save()
    return render(request,'request_insurance/reqinsu.html')


