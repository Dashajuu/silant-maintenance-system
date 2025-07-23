from django.urls import path, include

from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'maintenances', views.MaintenanceViewSet)
router.register(r'maintenance_type', views.MaintenanceTypeViewSet)


urlpatterns = [
    # api
    path('', include(router.urls)),

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

    # TODO: добавить разные вьюшки для бэкдейт и просто заявки
    # maintenance detail urls
    path('maintenance_type/<int:pk>', views.MaintenanceTypeDetailView.as_view(), name='detail_maintenance_type'),
    path('maintenance/<int:pk>', views.MaintenanceDetailView.as_view(), name='detail_maintenance'),

    # maintenance list urls
    path('maintenance_type/list', views.MaintenanceTypeListView.as_view(), name='list_maintenance_type'),
    path('maintenance/list', views.MaintenanceListView.as_view(), name='maintenance'),
]