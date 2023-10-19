from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.shortcuts import render
from student.models import Student
import datetime



def mng_req_edu(request):
    obj = Student.objects.all()
    context = {
        'z': obj,
    }
    return render(request,'student/mng req education.html',context)

def approve(request,idd):
    obj=Student.objects.get(student_id=idd)
    obj.status = "Approved"
    obj.save()
    return mng_req_edu(request)
def reject(request,idd):
    obj=Student.objects.get(student_id=idd)
    obj.status = "Rejected"
    obj.save()
    return mng_req_edu(request)

def student(request,idd):
    ss=request.session["u_id"]
    obc=""
    if request.method == 'POST':
        obj = Student()
        obj.educational_assistance_id = idd
        obj.student_name = request.POST.get('sn')
        obj.student_class = request.POST.get('cls')
        obj.date_of_birth = datetime.datetime.now()
        obj.village = request.POST.get('vlg')
        obj.city = request.POST.get('ct')
        obj.pin_code = request.POST.get('pcd')
        obj.district = request.POST.get('dst')

        # obj.mark = request.POST.get('mrk')

        myfile = request.FILES['ooo']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.fishermen_id_proof= myfile.name
        myfile1 = request.FILES['rrr']
        fs = FileSystemStorage()
        filename1 = fs.save(myfile1.name, myfile1)
        obj.relation_proof= myfile1.name
        obj.institution = request.POST.get('ins')
        myfile = request.FILES['mmm']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.mark = myfile.name
        obj.status ="Requested"
        obj.fishermen_id=ss
        obj.save()
        obc = "success"
    context = {
            'msg': obc
        }
    return render(request,'student/student.html',context)

# def viewreqedu(request):
#     obj = Student.objects.all()
#     context = {
#         'y': obj,
#     }
#     return render(request,'student/view,req education.html',context)
def vieweappedu(request):
    ss = request.session["u_id"]
    obj = Student.objects.filter(status='Approved',fishermen_id=ss)
    context = {
        'x': obj,
    }
    return render(request,'student/view approved educa.html',context)

