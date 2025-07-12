from django.urls import path

from . import views

urlpatterns = [
    # service companies' creation urls
    path('create', views.ServiceCompanyCreateView.as_view(), name='create_service_company'),

    # service companies' update urls
    path('<int:pk>/update', views.ServiceCompanyUpdateView.as_view(), name='update_service_company'),

    # service companies' delete urls
    path('<int:pk>/delete', views.ServiceCompanyDeleteView.as_view(), name='delete_service_company'),
]
