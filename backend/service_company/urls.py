from django.urls import path

from . import views

urlpatterns = [
    path('create_service_company', views.ServiceCompanyCreateView.as_view(), name='create_service_company'),
]
