from django.shortcuts import render

from django.shortcuts import render
from orders.models import Order
from payment.models import Payment
from equipment.models import Equipment



def eo(request,idd):
    ss=request.session["u_id"]
    obb=Equipment.objects.get(equipment_id=idd)
    a=obb.price
    context = {
        'jj': obb
    }
    if request.method == 'POST':
        obj = Order()
        obj.fishermen_id =ss
        obj.equipment_id = idd
        obj.quantity = request.POST.get('cc')
        obj.subcidy = request.POST.get('Sub')
        b=obj.subcidy
        obj.amount = a * int(obj.quantity)- int(b)
        obj.status='ordered'
        obj.save()
    return render(request,'orders/ordvw.html',context)

def status(request):
    ss=request.session["u_id"]
    obj = Order.objects.filter(status="Approved",fishermen_id=ss)
    context = {
        'a': obj,
    }
    return render(request,'orders/view approved order.html',context)

def paynt(request,idd):
    obj = Order.objects.get(order_id=idd)
    obj.save()
    return render(request,'payment/payment.html')

def vappo(request):
    ss=request.session["u_id"]
    obj = Order.objects.filter(fishermen_id=ss)
    context = {
        'b': obj,
    }
    return render(request,'orders/view ,approve order.html',context)

def approve(request,idd):
    obj=Order.objects.get(order_id=idd)
    obj.status="Approved"
    obj.save()
    return vappo(request)
def reject(request,idd):
    obj=Order.objects.get(order_id=idd)
    obj.status = "Rejected"
    obj.save()
    return vappo(request)



