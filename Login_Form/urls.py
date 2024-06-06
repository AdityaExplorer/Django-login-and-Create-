from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
urlpatterns = [
    path('',views.Home,name='home_page_acesss'),
    path('Create_Acc',views.Create_Accs,name='Create_ACC Acess'),
    path('Login',views.login,name='Login page '),
    path('change_password',views.change_password,name='change_password'),
    path('logout',views.logout,name='Logout code')


]
