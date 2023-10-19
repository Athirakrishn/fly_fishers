from django.conf.urls import url
from vessel import views

urlpatterns = [
    url('verifyvessels/', views.verifyvessel),
    url('vessels/',views.vessel),
    url('fied/',views.vrifd),
    url('rify/(?P<idd>\w+)', views.verify,name='vfy'),
    url('jrct/(?P<idd>\w+)',views.reject,name='rjt')
]