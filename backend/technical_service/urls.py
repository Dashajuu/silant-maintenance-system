from django.urls import path

from . import views

urlpatterns = [
    # maintenance creation urls
    path('request/create', views.MaintenanceCreateView.as_view(), name='create_maintenance_request'),
    path('backdate_maintenance/create', views.BackdateMaintenanceCreateView.as_view(), name='create_backdate_maintenance'),
    path('maintenance_type/create', views.MaintenanceTypeCreateView.as_view(), name='create_maintenance_type'),

    # maintenance update urls
    path('request/<int:pk>/update', views.ServiceMaintenanceUpdateView.as_view(), name='maintenance_request_update_service'),
    path('maintenance_type/<int:pk>/edit', views.MaintenanceTypeUpdateView.as_view(), name='edit_maintenance_type'),
    path('request/<int:pk>/edit', views.MaintenanceRequestUpdateView.as_view(), name='edit_maintenance_request_user'),
    path('backdate_maintenance/<int:pk>/edit', views.BackdateMaintenanceUpdateView.as_view(), name='edit_backdate_maintenance'),

    # maintenance delete urls
    path('maintenance_type/<int:pk>/delete', views.MaintenanceTypeDeleteView.as_view(), name='delete_maintenance_type'),
    path('request/<int:pk>/delete', views.MaintenanceDeleteView.as_view(), name='delete_maintenance'),
]