from django.conf.urls import url
from request_insurance import views

urlpatterns = [
    url('mngreqinsur/', views.mngreqinsu),
    # url('reqinsura/',views.reqinsu),
    url('vstat/',views.status),
    url('uuu/(?P<idd>\w+)', views.reins, name='req2'),
    url('av/(?P<idd>\w+)', views.approve, name='aw'),
    url('rv/(?P<idd>\w+)', views.reject, name='rw')

]