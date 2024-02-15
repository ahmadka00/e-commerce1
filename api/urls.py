from django.urls import path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'basket'


urlpatterns = [
    path('category', views.CategoryList.as_view()),
    path('category/<int:pk>', views.CategoryDetail.as_view())
]


urlpatterns = format_suffix_patterns(urlpatterns)