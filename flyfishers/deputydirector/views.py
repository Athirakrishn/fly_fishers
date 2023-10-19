
from django.shortcuts import render
from django.shortcuts import render
from deputydirector.models import Deputydirector
import datetime
from login.models import Login
# Create your views here.


def dd(request):
    obc=""
    if request.method == 'POST':
        obj = Deputydirector()
        obj.name = request.POST.get('nam')
        obj.date_of_birth = datetime.datetime.now()
        obj.gender = request.POST.get('gen')
        obj.qualification = request.POST.get('Qua')
        obj.pincode = request.POST.get('nn')
        obj.city = request.POST.get('city')
        obj.district = request.POST.get('District')
        obj.contact_no = request.POST.get('number')
        obj.email = request.POST.get('email')
        obj.password = request.POST.get('Password')
        obj.save()
        ob=Login()
        ob.username=obj.name
        ob.password=obj.password
        ob.type="deputy_director"
        ob.u_id=obj.deputydirector_id
        ob.save()
        obc="success"
    context={
        'msg':obc
    }
    return render(request,'deputydirector/deputy director.html',context)


def managedd(request):
    obj = Deputydirector.objects.all()
    context = {
        'a': obj,
      }
    return render(request,'deputydirector/manage DD.html',context)


def update(request,idd):
    obj = Deputydirector.objects.get(deputydirector_id=idd)
    context = {
        'a': obj,
    }
    if request.method == 'POST':
        obj = Deputydirector.objects.get(deputydirector_id=idd)

        obj.name = request.POST.get('nam')
        obj.date_of_birth = datetime.datetime.now()
        obj.gender = request.POST.get('gen')
        obj.qualification = request.POST.get('Qua')
        obj.pincode = request.POST.get('num')
        obj.city = request.POST.get('city')
        obj.district = request.POST.get('District')
        obj.contact_no = request.POST.get('num')
        obj.email = request.POST.get('email')
        obj.password = request.POST.get('Password')
        obj.save()
        return managedd(request)

    return render(request,'deputydirector/update dd.html',context)

# def update(request,idd):
#     obj=Deputydirector.objects.get(deputydirector_id=idd)
#     obj.save()
#     return updatedd(request)
def delete(request,idd):
    obj=Deputydirector.objects.get(deputydirector_id=idd)
    obj.delete()
    return managedd(request)






