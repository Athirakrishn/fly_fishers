from django.conf.urls import url
from prawn_filtration import views

urlpatterns = [
    url('addprwnfill/', views.addprawn),
    url('vprwn/',views.viewprawn),
    url('fvprn/',views.fisvprn)

]