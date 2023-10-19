from django.conf.urls import url
from insurance import views

urlpatterns = [
    url('addinsu/', views.insu),
    url('viewreqinsur/',views.viewreqinsu),
    url('request/(?P<idd>\w+)',views.rin,name='req2')

]