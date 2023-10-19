from django.conf.urls import url
from request_prawn_filtration import views

urlpatterns = [
    url('reqstprawn/', views.reqprawn),
    url('viewprawnfil/',views.viewapprawn),
    url('manageprwn/',views.mangerepr),
    url('aa3/(?P<idd>\w+)', views.approve, name='a4'),
    url('rr3/(?P<idd>\w+)', views.reject, name='r4')
]