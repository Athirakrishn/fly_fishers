from django.conf.urls import url
from request_vessel_license import views

urlpatterns = [
    url('reqvesselli/', views.req_ves1),
    url('viwmngreqvess/',views.viwmngreqvessel),
    url('viewappvesselli/',views.viwappvessel),
    url('a11/(?P<idd>\w+)', views.approve, name='a6'),
    url('r11/(?P<idd>\w+)', views.reject, name='r6')

]