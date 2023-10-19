"""flyfishers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from login import views


urlpatterns = [
    path('admin/', admin.site.urls),
    url('alert/',include('alert.url')),
    url('compensation/',include('compensation.url')),
    url('deputydirector/',include('deputydirector.url')),
    url('education_assistance/',include('education_assistance.url')),
    url('equipment/', include('equipment.url')),
    url('fisheries_officer/', include('fisheries_officer.url')),
    url('fishermen/', include('fishermen.url')),
    url('freenet_license/', include('freenet_license.url')),
    url('insurance/', include('insurance.url')),
    url('login/', include('login.url')),
    url('orders/', include('orders.url')),
    url('payment/', include('payment.url')),
    url('prawn_filtration/', include('prawn_filtration.url')),
    url('relief_scheme/', include('relief_scheme.url')),
    url('request_compensation/', include('request_compensation.url')),
    url('request_freenet_license/', include('request_freenet_license.url')),
    url('request_insurance/', include('request_insurance.url')),
    url('request_prawn_filtration/', include('request_prawn_filtration.url')),
    url('request_releif_scheme/', include('request_releif_scheme.url')),
    url('student/', include('student.url')),
    url('trolling/', include('trolling.url')),
    url('vessel/', include('vessel.url')),
    url('vessel_license/',include('vessel_license.url')),
    url('request_vessel_licens/',include('request_vessel_license.url')),
    url('temp/',include('temp.url')),
    url('msg/',include('message.url')),
    url('$',views.login)



]
