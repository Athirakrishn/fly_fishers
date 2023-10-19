from django.conf.urls import url
from request_freenet_license import views

urlpatterns = [
    # url('reqfree/', views.reqfree),
    url('rfr/(?P<idd>\w+)', views.reqfree, name='ee'),

    url('viewmngfree/',views.mngfree),
    url('viewappvedofree/',views.viewappreqfree),
    url('aa1/(?P<idd>\w+)', views.approve, name='a5'),
    url('rr1/(?P<idd>\w+)', views.reject, name='r5')

]