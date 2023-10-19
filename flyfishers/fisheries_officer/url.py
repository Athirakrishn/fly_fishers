from django.conf.urls import url
from fisheries_officer import views



urlpatterns=[
     url('fishoff/',views.fisho),
     url('vv/',views.vmfisho),
     url('viwfisofr/',views.viwfisoff),
     url('u1/(?P<idd>\w+)',views.updatefisho,name='pp'),
     url('dd/(?P<idd>\w+)', views.delete,name='ff'),
]