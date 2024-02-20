from django.urls import path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as auth_views


app_name = 'basket'


urlpatterns = [
    path('category', views.CategoryList.as_view()),
    path('category/<int:pk>', views.CategoryDetail.as_view()),
    path('register/', views.UserRegisteration.as_view(), name='user_register'),
    # path('register2/', views.user_register_view, name='register2')
    
]

urlpatterns += [
    path('api-token-auth/', auth_views.obtain_auth_token)
]
