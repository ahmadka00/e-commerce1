from django.urls import path
from api import views

app_name = 'basket'


urlpatterns = [
    path('category', views.category_list),
    path('category/<int:pk>', views.category_detail)
]