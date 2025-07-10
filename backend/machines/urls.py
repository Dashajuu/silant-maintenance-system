from django.urls import path

from . import views

urlpatterns = [
    # creation urls
    path('create', views.MachineCreateView.as_view(), name='create_machine'),
    path('machine_type/create', views.MachineTypeCreateView.as_view(), name='create_machine_type'),
    path('engine_type/create', views.EngineTypeCreateView.as_view(), name='create_engine_type'),
    path('transmission_type/create', views.TransmissionTypeCreateView.as_view(), name='create_transmission_type'),
    path('drive_axle_type/create', views.DriveAxleTypeCreateView.as_view(), name='create_drive_axle_type'),
    path('steer_axle_type/create', views.SteerAxleTypeCreateView.as_view(), name='create_steer_axle_type'),
]