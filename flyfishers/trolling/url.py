from django.conf.urls import url
from trolling import views

urlpatterns = [
    url('addtrol/', views.addtroling),
    url('viewtroll/',views.viewtroling),
    url('mngtrol/',views.managetroling),
    url('lkj/(?P<idd>\w+)', views.delete, name='qwe')

]