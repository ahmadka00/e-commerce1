
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('basket_summary/', include('basket.urls', namespace='basket')),
    path('', include('store.urls', namespace='store')),
    path('api/', include('api.urls', namespace='api')),
    path('account/', include('account.urls', namespace='account')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
