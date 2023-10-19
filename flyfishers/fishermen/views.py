from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from fishermen.models import Fishermen
import datetime
from login.models import Login

def fishm(request):
    fi=''
    if request.method == 'POST':
        obj = Fishermen()
        obj.name = request.POST.get('nam')
        obj.date_of_birth = datetime.datetime.now()
        obj.gender = request.POST.get('gen')
        obj.qualification = request.POST.get('qua')
        obj.pincode = request.POST.get('pin')
        obj.city = request.POST.get('cty')
        obj.district = request.POST.get('dis')
        obj.contact = request.POST.get('number')
        obj.email = request.POST.get('eml')
        obj.password = request.POST.get('psw')
        myfile = request.FILES['ccc']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.id_proof = myfile.name
        obj.save()
        ob = Login()
        ob.username = obj.name
        ob.password = obj.password
        ob.type = "fishermen"
        ob.u_id = obj.fishermen_id
        ob.save()
        fi = "success"
    context = {
            'msg': fi
        }
    return render(request,'fishermen/fishermen.html',context)


def vfishm(request):
    obj = Fishermen.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'fishermen/view fishermen.html',context)

def dvfishm(request):
    obj = Fishermen.objects.all()
    context = {
        'y': obj,
    }
    return render(request,'fishermen/view fishermendrtr.html',context)
def mmvvff(request):
    obj = Fishermen.objects.all()
    context = {
        'a': obj,
    }
    return render(request,'fishermen/mmvv fishermen.html',context)
