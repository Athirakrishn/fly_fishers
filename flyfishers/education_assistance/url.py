from django.conf.urls import url
from education_assistance import views


urlpatterns=[
    url('edu/',views.edu),
    url('view/',views.viewedu),
    url('viewreqweduc/',views.viewreqedu),
    url('kkk/(?P<idd>\w+)',views.rse,name='cc')

]