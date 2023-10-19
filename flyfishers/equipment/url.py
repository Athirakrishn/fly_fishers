from django.conf.urls import url
from equipment import views

urlpatterns=[
     url('addmngequ/',views.addmng),
     url('mngequ/',views.mng),
     url('upt/(?P<idd>\w+)',views.update,name='dat'),
     url('wet/(?P<idd>\w+)',views.delete,name='er'),
     url('viwodrequ/',views.viworequip),
     # url('viewappvedo/', views.vappvdo),
     url('or/(?P<idd>\w+)',views.reo,name='ww'),

]