from django.conf.urls import url
from compensation import views


urlpatterns=[
    url('compn/',views.comp),
    url('viwco/',views.viewcomp),
    url('fvcom/',views.fisvcomp),
    url('request/(?P<idd>\w+)',views.rc,name='bb'),
    url('viewreqcomp/',views.viwreqcom),
]