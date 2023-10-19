from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.shortcuts import render
from request_compensation.models import ReqCompensation
# Create your views here.


def mngreqcom(request):
    obj = ReqCompensation.objects.all()
    context = {
        'a': obj,
    }
    return render(request,'request_compensation/mng req compan.html',context)

def approve(request,idd):
    obj=ReqCompensation.objects.get(req_compensation_id=idd)
    obj.status="Approved"
    obj.save()
    return mngreqcom(request)
def reject(request,idd):
    obj = ReqCompensation.objects.get(req_compensation_id=idd)
    obj.status = "Rejected"
    obj.save()
    return mngreqcom(request)


def reqcom(request,idd):
    bdv=''
    if request.method == 'POST':
        obj = ReqCompensation()
        obj.compensation_id=idd
        obj.fishermen_id = 1
        obj.user_name = request.POST.get('usn')
        obj.reason = request.POST.get('rsn')
        # obj.proof = request.POST.get('prf')
        obj.date = request.POST.get('dt')
        myfile=request.FILES['prf']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        obj.proof=myfile.name
        myfile1 = request.FILES['mmm']
        fs = FileSystemStorage()
        filename1 = fs.save(myfile1.name, myfile1)
        obj.details = myfile1.name
        obj.status="pending"
        obj.save()
        print("hello")
        bdv="success"
    context={
        'msg': bdv
    }
    return render(request,'request_compensation/req comp.html', context)

# def viwreqcom(request):
#     obj = ReqCompensation.objects.all()
#     context = {
#         'x': obj,
#     }
#     return render(request,'request_compensation/view,req  comp.html',context)


def viewappcom(request):
    ss = request.session["u_id"]
    obj = ReqCompensation.objects.filter(status='Approved',fishermen_id=ss)
    context = {
        'y': obj,
    }
    return render(request,'request_compensation/vew approved comp.html',context)



# Create your views here.


