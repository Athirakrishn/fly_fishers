
from django.shortcuts import render
from fisheries_officer.models import FisheriesOfficer
import datetime
from login.models import Login

def fisho(request):
    ce=''
    if request.method == 'POST':
        obj = FisheriesOfficer()
        obj.name = request.POST.get('nam')
        obj.date_of_birth = datetime.datetime.now()
        obj.gender = request.POST.get('gender')
        obj.qualification = request.POST.get('qua')
        obj.pincode = request.POST.get('pnc')
        obj.city = request.POST.get('city')
        obj.district = request.POST.get('District')
        obj.contact_no = request.POST.get('num')
        obj.email = request.POST.get('email')
        obj.password = request.POST.get('psw')
        obj.save()
        ob = Login()
        ob.username = obj.name
        ob.password = obj.password
        ob.type = "fisheries_officer"
        ob.u_id = obj.fisheries_officer_id
        ob.save()
        ce = "success"
    context = {
            'msg': ce
    }
    return render(request,'fisheries_officer/fisheries officer.html',context)


def vmfisho(request):
    obj = FisheriesOfficer.objects.all()
    context = {
        'b': obj,
    }
    return render(request,'fisheries_officer/view,mng fiseries officer.html',context)


def updatefisho(request,idd):
    obj = FisheriesOfficer.objects.get(fisheries_officer_id=idd)
    context = {
        'b': obj,
    }
    if request.method == 'POST':
        obj = FisheriesOfficer.objects.get(fisheries_officer_id=idd)
        obj.name = request.POST.get('nam')
        obj.date_of_birth = datetime.datetime.now()
        # obj.gender = request.POST.get('gender')
        obj.qualification = request.POST.get('Qua')
        obj.pincode = request.POST.get('pin')
        obj.city = request.POST.get('city')
        obj.district = request.POST.get('District')
        obj.contact_no = request.POST.get('num')
        obj.email = request.POST.get('email')
        obj.password = request.POST.get('paa')
        obj.save()
    return render(request,'fisheries_officer/update fisheries officer.html',context)

def delete(request,idd):
    obj=FisheriesOfficer.objects.get(fisheries_officer_id=idd)
    obj.delete()
    return vmfisho(request)


def viwfisoff(request):
    obj = FisheriesOfficer.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'fisheries_officer/view fishoff.html',context)

