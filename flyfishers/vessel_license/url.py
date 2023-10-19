from django.conf.urls import url
from vessel_license import views

urlpatterns = [
    url('viewaddvessel/', views.addves),
    url('viewvesselicense/',views.viewves),
    url('fisvwvsl/',views.fisvwves)

]