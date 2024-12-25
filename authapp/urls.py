from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('submit/', views.submit_credentials, name='submit_credentials'),
]