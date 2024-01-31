from django.urls import path
from store import views

app_name = 'store'


urlpatterns = [
    path('', views.home, name='home' ),
    # path('roduct/<int:product_id>/', views.product_page, name='product_page'),
    path('<slug:slug>/', views.product_page, name='product_page'),
    path('store/<slug:category_slug>', views.category_page, name='category_page'),
]
