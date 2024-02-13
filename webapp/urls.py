from django.contrib import admin
from django.urls import path
from .views import CreateAccount, ItemDashboard
from django.contrib.auth import views as authentication_views

urlpatterns = [
    path('', authentication_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('item-dashboard/', ItemDashboard.as_view(), name='item-dashboard'),
    path('create-account/', CreateAccount.as_view(), name='create-account'),
    path('logout/', authentication_views.LogoutView.as_view(template_name='login/logout.html'), name='logout'),

]
