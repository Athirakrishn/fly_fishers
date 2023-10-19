from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render
from login.models import Login



def login(request):

     if request.method =="POST":
        name = request.POST.get("unm")
        password =request.POST.get("psw")
        obj = Login.objects.filter(username=name,password=password)
        tp = ""
        for ob in obj:
            tp=ob.type
            uid=ob.u_id
            if tp == "director":
                request.session["u_id"]=uid
                return  HttpResponseRedirect('/temp/drctr/')
            elif tp == "deputy_director":
                request.session["u_id"]=uid
                return HttpResponseRedirect('/temp/deptydirector/')
            elif tp == "fisheries_officer":
                request.session["u_id"]=uid
                return HttpResponseRedirect('/temp/malyabvnofer/')
            elif tp == "fishermen":
                request.session["u_id"]=uid
                return HttpResponseRedirect('/temp/fimen/')

        else:
            objilist="incorrect username or password... please try again..!"
            context={
                'msg': objilist,
            }
            return render(request,'login/login.html',context)
     return render(request, 'login/login.html')