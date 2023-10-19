from django.conf.urls import url
from temp import views

urlpatterns = [
    url('deptydirector/', views.depty),
    url('drctr/', views.dierctr),
    url('fimen/', views.fismn),
    url('hom/', views.hom),
    url('malyabvnofer/', views.malsyaofficer),
    url('aot/',views.abt),
    url('ff/',views.fiabt)


]