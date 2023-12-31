# api/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('api/', views.OrderList.as_view()),
    path('api/csrf-token/', views.GetCsrfToken),
    path('api/auth/register', views.UserRegister.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
