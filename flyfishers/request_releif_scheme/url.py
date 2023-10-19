from django.conf.urls import url
from request_releif_scheme import views

urlpatterns = [
    url('viewap/', views.viewapprelief),
    # url('rerelif/',views.request_reliefe),
    url('request/(?P<idd>\w+)', views.request_reliefe, name='req1'),
    url('mngreqreliefsche/',views.mngreqrelief),
    url('approve/(?P<idd>\w+)',views.approve, name='app'),
    url('reject/(?P<idd>\w+)', views.reject, name='rej')

]