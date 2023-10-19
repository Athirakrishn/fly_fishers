from django.conf.urls import url
from freenet_license import views

urlpatterns = [
    url('addfreenet/', views.addfree),
    url('viewfree/', views.vfree),
    url('fisvifree/',views.fisvfree),
    url('dcf/(?P<idd>\w+)',views.ref,name='ee')

]