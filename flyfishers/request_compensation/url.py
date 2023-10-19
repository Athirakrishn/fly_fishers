from django.conf.urls import url
from request_compensation import views

urlpatterns = [
    url('mngreqstcomp/', views.mngreqcom),
    # url('reqstcomp/',views.reqcom),
    url('tttt/(?P<idd>\w+)',views.reqcom,name='bb'),
    url('viewappvedcom/',views.viewappcom),
    url('aa/(?P<idd>\w+)', views.approve, name='a1'),
    url('rr/(?P<idd>\w+)', views.reject, name='r1')



]