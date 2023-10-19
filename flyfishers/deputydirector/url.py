from django.conf.urls import url
from deputydirector import views


urlpatterns=[
    url('deputy/',views.dd),
    url('ppu/(?P<idd>\w+)',views.update,name='upd'),
    url('mm/(?P<idd>\w+)', views.delete, name='dld'),
    url('manage/',views.managedd)

]