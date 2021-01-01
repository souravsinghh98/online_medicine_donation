from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('donor_home/', views.donor_home, name='donor_home'),
    path('login/',views.signin, name='login'),
    path('register/', views.signup, name='register'),
    path('donor_login/', views.donor_login, name='donor_login'),
    path('donor_register/', views.donor_register, name='donor_register'),
    
    path('ngo_login/', views.ngo_login, name='ngo_login'),
    path('ngo_register/', views.ngo_register, name='ngo_register'),
    path('logout/', views.signout, name='logout'),
    path('ngo_home/', views.ngo_home, name='ngo_home'),
    path('donate/<str:pk>/', views.donate, name='donate'),
    path('update_status/<str:pk>/', views.status_update, name='update_status'),
]
