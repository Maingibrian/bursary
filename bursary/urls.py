from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("cdfofficial", views.cdfofficial, name='cdfofficial'),
    path("eduinstitution", views.eduinstitution, name='eduinstitution'),
    path("beneficiary", views.beneficiary, name='beneficiary'),
    path("chequeform", views.chequeform, name='chequeform'),
    path("register", views.register, name='register'),
    path("login_user", views.login_user, name='login_user'),
    path("logout_user", views.logout_user, name='logout_user'),
]