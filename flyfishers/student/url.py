from django.conf.urls import url
from student import views

urlpatterns = [
    url('studentt/', views.student),

    url('viewappeducation/',views.vieweappedu),
    url('mngreqedun/',views.mng_req_edu),
    url('ccu/(?P<idd>\w+)',views.student,name='cc'),
    url('ravi/(?P<idd>\w+)',views.approve,name='kiim'),
    url('banu/(?P<idd>\w+)',views.reject,name='jjm')
]