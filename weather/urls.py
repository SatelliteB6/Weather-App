from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # the path for our index view
    path('login/', views.CustomAuthToken.as_view(), name='api_login'),
    path('logout/', views.Logout.as_view(), name='api_logout'),
    path('weather/', views.WeatherListCreateView.as_view(), name='weather-list-create'),
    path('weather/<int:pk>/', views.WeatherRetrieveUpdateDestroyView.as_view(), name='weather-detail'),
]
