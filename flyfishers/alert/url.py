from django.conf.urls import url
from alert import views


urlpatterns=[
    url('critical alert/',views.alert),
    url('viewc/',views.view_crit),
    url('mngalert/',views.mange_alert),
    url('lpo/(?P<idd>\w+)', views.delete, name='cvb')

]