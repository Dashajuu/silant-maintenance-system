from django.urls import path

from . import views

urlpatterns = [
    # creation urls
    path('create', views.ServiceCompanyCreateView.as_view(), name='create_service_company'),
]
