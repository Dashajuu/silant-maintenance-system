from tkinter.font import names

from django.urls import path

from . import views
from . import models

urlpatterns = [
    # machines' creation urls
    path('create', views.MachineCreateView.as_view(), name='create_machine'),
    path('machine_type/create', views.MachineTypeCreateView.as_view(), name='create_machine_type'),
    path('engine_type/create', views.EngineTypeCreateView.as_view(), name='create_engine_type'),
    path('transmission_type/create', views.TransmissionTypeCreateView.as_view(), name='create_transmission_type'),
    path('drive_axle_type/create', views.DriveAxleTypeCreateView.as_view(), name='create_drive_axle_type'),
    path('steer_axle_type/create', views.SteerAxleTypeCreateView.as_view(), name='create_steer_axle_type'),

    # machines' update urls
    path('<int:pk>/update', views.MachineUpdateView.as_view(), name='update_machine'),
    path('machine_type/<int:pk>/update', views.MachineTypeUpdateView.as_view(), name='update_machine_type'),
    path('engine_type/<int:pk>/update', views.EngineTypeUpdateView.as_view(), name='update_engine_type'),
    path('transmission_type/<int:pk>/update', views.TransmissionTypeUpdateView.as_view(), name='update_transmission_type'),
    path('drive_axle_type/<int:pk>/update', views.DriveAxleTypeUpdateView.as_view(), name='update_drive_axle_type'),
    path('steer_axle_type/<int:pk>/update', views.SteerAxleTypeUpdateView.as_view(), name='update_steer_axle_type'),

    # machines' delete urls
    path('<int:pk>/delete', views.MachineDeleteView.as_view(), name='delete_machine'),
    path('machine_type/<int:pk>/delete', views.delete_item_view(models.MachineType).as_view(), name='delete_machine_type'),
    path('engine_type/<int:pk>/delete', views.delete_item_view(models.EngineType).as_view(), name='delete_engine_type'),
    path('transmission_type/<int:pk>/delete', views.delete_item_view(models.TransmissionType).as_view(), name='delete_transmission_type'),
    path('drive_axle_type/<int:pk>/delete', views.delete_item_view(models.DriveAxleType).as_view(), name='delete_drive_axle_type'),
    path('steer_axle_type/<int:pk>/delete', views.delete_item_view(models.SteerAxleType).as_view(), name='delete_steer_axle_type'),
]