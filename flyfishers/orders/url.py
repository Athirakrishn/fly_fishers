from django.conf.urls import url
from orders import views

urlpatterns = [
    # url('vieworder/', views.vo),
    url('roveor/',views.vappo),
    url('app/(?P<idd>\w+)',views.eo,name='ww'),
    url('aaaapaa/(?P<idd>\w+)',views.approve,name='a1a'),
    url('rrrrprr/(?P<idd>\w+)',views.reject,name='r1r'),
    url('asd/', views.status),
    url('tyt/(?P<idd>\w+)', views.paynt,name='pay'),

]