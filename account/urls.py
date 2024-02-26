from django.urls import path
from account import views
from django.contrib.auth import views as auth_views
from account.forms import UserPasswordResetForm, UserPasswordResetConfirmViewForm
from django.urls import reverse_lazy

app_name = 'account'


urlpatterns = [
   path('login/', views.login_user, name='login'),
   path('logout/', views.logout_user, name='logout'),
   path('register/', views.account_register, name='register'),
   path('activate/<slug:uidb64>/<slug:token>/', views.account_activate, name='activate'),
   # User dashboard
   path('dashboard/', views.dashboard, name='dashboard'),
   path('profile/edit', views.edit_details, name='edite_details' ),
   
]


# Password Reset Urls
urlpatterns += [
     path('change_password/', views.UserPasswordChange.as_view(), name='change_password'), 

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="account/password_reset/password_reset.html", 
                                                                 form_class=UserPasswordResetForm, success_url=reverse_lazy('account:password_reset_done')), name='password_reset'),

    path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(template_name="account/password_reset/password_reset_done.html"), name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset/password_reset_confirm.html", 
                                                                 form_class=UserPasswordResetConfirmViewForm, success_url=reverse_lazy('account:password_reset_complete')), name='password_reset_confirm'),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="account/password_reset/password_reset_complete.html"), name='password_reset_complete'),
]