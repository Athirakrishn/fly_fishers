from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.shortcuts import render
from equipment.models import Equipment
from orders.models import Order
# Create your views here.


def addmng(request):
    obc=''
    if request.method == 'POST':
        obj = Equipment()
        obj.equipment_name = request.POST.get('equt')
        # obj.equipmentimage = request.POST.get('eqimg')
        myfile = request.FILES['eg']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.equipmentimage = myfile.name
        obj.quandity = request.POST.get('Qua')
        obj.price = request.POST.get('prc')
        obj.subsidy = request.POST.get('Sub')
        obj.fishermen_id= 1
        obj.status="Pending"
        obj.save()
        obc = "success"
    context = {
            'msg': obc
        }
    return render(request,'equipment/add,mng equipment.html',context)


def mng(request):
    obj = Equipment.objects.all()
    context = {
        'd': obj,
    }
    return render(request,'equipment/mng equipment.html',context)

def update(request,idd):

    obj = Equipment.objects.get(equipment_id=idd)
    context = {
        'd': obj,
    }

    if request.method == 'POST':
        obj = Equipment.objects.get(equipment_id=idd)
        obj.equipment_name = request.POST.get('equt')
        # obj.equipmentimage = request.POST.get('eqimg')
        myfile = request.FILES['uu']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.equipmentimage = myfile.name
        obj.quandity = request.POST.get('Qua')
        obj.price = request.POST.get('Price')
        obj.subsidy = request.POST.get('Sub')
        obj.save()
    return render(request,'equipment/update equipment.html',context)

def delete(request,idd):
    obj=Equipment.objects.get(equipment_id=idd)
    obj.delete()
    return mng(request)



def viworequip(request):
    obj = Equipment.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'equipment/view,order equipment.html',context)
def reo(request,idd):
    obj = Equipment.objects.get(equipment_id=idd)
    obj.save()
    return render(request,'orders/ordvw.html')

def status(request):
    ss = request.session["u_id"]
    obj = Equipment.objects.filter(status="Approved",fishermen_id=ss)
    context = {
        'a': obj,
    }
    return render(request,'equipment/view approved order.html',context)

# def vappvdo(request):
#     obj = Equipment.objects.all()
#     context = {
#         'z': obj
#     }
#     return render(request,'equipment/',context)


# def mod(request):
#     obj = Equipment.objects.all()
#     context = {
#         'c': obj,
#     }
#     return render(request,'equipment/mngordr.html',context)
