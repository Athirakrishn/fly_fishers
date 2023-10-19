from django.shortcuts import render
from django.shortcuts import render
from payment.models import Payment
from orders.models import Order


# Create your views here.
def pay(request,idd):
    obc = ""
    obk=Order.objects.get(order_id=idd)
    if request.method == 'POST':
        obj = Payment()
        obj.order_id=idd
        obj.fishermen_id=1
        obj.name = request.POST.get('name')
        obj.account_no = request.POST.get('Account')
        obj.amount = request.POST.get('Amt')
        obj.bank_name = request.POST.get('Bank')
        obj.branch_name = request.POST.get('Branch')
        obj.ifsc_code = request.POST.get('ifc')
        obj.status="Paid"
        obj.save()
        obc = "success"
    context = {
            'e': obk,
            'msg': obc
        }
    return render(request,'payment/payment.html',context)


def vpay(request):
    obj = Payment.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'payment/view payment.html',context)

# Create your views here.
