from django.urls import path
from account import views
from django.contrib.auth import views as auth_views
from account.forms import UserLoginForm
app_name = 'account'


urlpatterns = [
   path('login/', views.login_user, name='login'),
   path('logout/', views.logout_user, name='logout'),
   path('register/', views.account_register, name='register'),
   path('activate/<slug:uidb64>/<slug:token>/', views.account_activate, name='activate'),
   # User dashboard
   path('dashboard/', views.dashboard, name='dashboard'),
]