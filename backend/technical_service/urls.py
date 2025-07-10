from django.urls import path

from . import views

urlpatterns = [
    # creation urls
    path('request/create', views.MaintenanceCreateView.as_view(), name='create_maintenance_request'),
    path('backdate_maintenance/create', views.BackdateMaintenanceCreateView.as_view(), name='create_backdate_maintenance'),
    path('maintenance_type/create', views.MaintenanceTypeCreateView.as_view(), name='create_maintenance_type'),

    # creation urls
    path('request/<int:pk>/update', views.ServiceMaintenanceUpdateView.as_view(), name='maintenance_request_update_service'),
]