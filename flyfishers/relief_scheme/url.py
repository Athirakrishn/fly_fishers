from django.conf.urls import url
from relief_scheme import views

urlpatterns = [
    url('reliefschem/', views.relif),
    url('reqreliefscheme',views.reqrelif),
    url('request/(?P<idd>\w+)',views.reqrelif,name='req1'),


]