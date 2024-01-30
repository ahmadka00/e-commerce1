from django.urls import path
from basket import views

app_name = 'basket'


urlpatterns = [
    path('', views.basket_summary, name='basket_summary' ),
    path('add_basket/', views.add_basket, name='add_basket'),
    path('delete_basket/', views.delete_basket, name='delete_basket'),
    path('update_basket/', views.update_basket, name='update_basket'),

]