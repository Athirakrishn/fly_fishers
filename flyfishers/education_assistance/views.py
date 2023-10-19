from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.shortcuts import render
from education_assistance.models import EducationalAssistance
from student.models import Student
# Create your views here.


def edu(request):
    obc=''
    if request.method == 'POST':
        obj = EducationalAssistance()
        obj.educational_assistance_id = 1
        obj.scolarship_name = request.POST.get('scp')
        # obj.description = request.POST.get('desc')
        myfile = request.FILES['desc']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.description = myfile.name
        obj.status="Pending"
        obj.save()
        obc = "success"
    context = {
            'msg': obc
        }
    return render(request,'educational_assistance/education.html',context)


def viewedu(request):
    obj = EducationalAssistance.objects.all()
    context = {
        'x': obj,
    }
    return render(request,'educational_assistance/view education.html',context)
def viewreqedu(request):
    obj = EducationalAssistance.objects.all()
    context = {
        'y': obj,
    }
    return render(request,'educational_assistance/view,req education.html',context)

def rse(request,idd):
    obj=EducationalAssistance.objects.get(educational_assistance_id=idd)
    obj.save()
    return render(request,'student/student.html')