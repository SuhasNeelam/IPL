
from django.contrib import admin
from django.urls import path
from .views import adminloginview, admin_homepage_view, logout_admin, authenticate_admin, update_points

urlpatterns = [
    path('admin/', adminloginview, name='adminloginpage'),
    path('adminauthenticate/', authenticate_admin),
    path('admin/homepage/', admin_homepage_view, name='adminhomepage'),
    path('adminlogout/', logout_admin),
    path('updatepoints/', update_points)

]
