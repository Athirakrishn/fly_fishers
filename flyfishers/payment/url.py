from django.conf.urls import url
from payment import views

urlpatterns = [
    url('payment/(?P<idd>\w+)', views.pay,name='pay'),
    url('view/',views.vpay)

]