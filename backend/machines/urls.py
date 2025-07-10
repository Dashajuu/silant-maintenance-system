from tkinter.font import names

from django.urls import path

from . import views

urlpatterns = [
    # create view
    path('create_machine_type', views.MachineTypeCreateView.as_view(), name='create_machine_type'),
    path('create_engine_type', views.EngineTypeCreateView.as_view(), name='create_engine_type'),
    path('create_transmission_type', views.TransmissionTypeCreateView.as_view(), name='create_transmission_type'),
    path('create_drive_axle_type', views.DriveAxleTypeCreateView.as_view(), name='create_drive_axle_type'),
    path('create_steer_axle_type', views.SteerAxleTypeCreateView.as_view(), name='create_steer_axle_type'),
    path('create_machine', views.MachineCreateView.as_view(), name='create_machine'),
]