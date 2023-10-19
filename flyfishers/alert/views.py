from django.http import HttpResponse
from django.shortcuts import render
from alert.models import Alert
import datetime
# Create your views here.


def alert(request):
    qwe=""
    if request.method == 'POST':
        obj = Alert()
        obj.date = datetime.datetime.now()
        obj.description = request.POST.get('ss')
        obj.save()
        qwe="success"
    context={
            'msg':qwe
        }
    return render(request,'alert/critical alert.html',context)
def mange_alert(request):
    obj = Alert.objects.all()
    context = {
        'b': obj,
    }

    return render(request,'alert/mngalert.html',context)
def delete(request,idd):
    obj=Alert.objects.get(alert_id=idd)
    obj.delete()
    return mange_alert(request)

def view_crit(request):
    obj = Alert.objects.all()
    context = {
        'x': obj,
    }

    return render(request,'alert/view critical alert.html',context)


