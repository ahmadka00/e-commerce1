from django.urls import path, include
from api import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


app_name = 'api'


router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet, basename='category')
router.register(r'products', views.ProductViewSet, basename='product')

urlpatterns = [
    # path('categories', views.CategoryList.as_view(), name='Category_list'),
    # path('categories/<slug:slug>', views.CategoryDetail.as_view(), name='category_detail'),
    # path('products', views.ProductList.as_view(), name='product_list'),
    # path('products/<slug:slug>', views.ProductDetail.as_view(), name='product_detail'),
    path('', include(router.urls)),
    path('register', views.CustomUserCreate.as_view(), name='user_register'),
    path('logout/blacklist', views.BlacklistTokenView.as_view(), name='blacklist'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/docs/', SpectacularSwaggerView.as_view(url_name="api:schema"))
    
]

#Token from simple JWT
urlpatterns += [
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
