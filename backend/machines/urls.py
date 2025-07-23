from django.urls import path, include

from rest_framework import routers

from . import views
from . import models


router = routers.DefaultRouter()
router.register(r'machines', views.MachineViewSet)
router.register(r'machine_type', views.MachineTypeViewSet)
router.register(r'engine_type', views.EngineTypeViewSet)
router.register(r'transmission_type', views.TransmissionTypeViewSet)
router.register(r'drive_axle_type', views.DriveAxleTypeSerializer)
router.register(r'steer_axle_type', views.SteerAxleTypeViewSet)


urlpatterns = [
    # api
    path('', include(router.urls)),

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
    path('machine_type/<int:pk>/delete', views.delete_item_view(models.MachineType, 'machinetype').as_view(), name='delete_machine_type'),
    path('engine_type/<int:pk>/delete', views.delete_item_view(models.EngineType, 'enginetype').as_view(), name='delete_engine_type'),
    path('transmission_type/<int:pk>/delete', views.delete_item_view(models.TransmissionType, 'transmissiontype').as_view(), name='delete_transmission_type'),
    path('drive_axle_type/<int:pk>/delete', views.delete_item_view(models.DriveAxleType, 'driveaxletype').as_view(), name='delete_drive_axle_type'),
    path('steer_axle_type/<int:pk>/delete', views.delete_item_view(models.SteerAxleType, 'steeraxletype').as_view(), name='delete_steer_axle_type'),

    # items detail views
    path('machine_type/<int:pk>',
         views.create_detail_view(models.MachineType,
                                  'machines/machines_items_detail.html',
                                  'item',
                                  'Модель техники',
                                  'machine_type').as_view(),
         name='detail_machine_type'),
    path('engine_type/<int:pk>',
         views.create_detail_view(models.EngineType,
                                  'machines/machines_items_detail.html',
                                  'item',
                                  'Модель двигателя',
                                  'engine_type').as_view(),
         name='detail_engine_type'),
    path('transmission_type/<int:pk>',
         views.create_detail_view(models.TransmissionType,
                                  'machines/machines_items_detail.html',
                                  'item',
                                  'Модель трансмиссии',
                                  'transmission_type').as_view(),
         name='detail_transmission_type'),
    path('drive_axle_type/<int:pk>',
         views.create_detail_view(models.DriveAxleType,
                                  'machines/machines_items_detail.html',
                                  'item',
                                  'Модель ведущего моста',
                                  'drive_axle_type').as_view(),
         name='detail_drive_axle_type'),
    path('steer_axle_type/<int:pk>',
         views.create_detail_view(models.SteerAxleType,
                                  'machines/machines_items_detail.html',
                                  'item',
                                  'Модель управляемого моста',
                                  'steer_axle_type').as_view(),
         name='detail_steer_axle_type'),

    # machine detail view
    path('<int:pk>', views.MachineDetailView.as_view(), name='detail_machine'),

    # items list view
    path('machine_type/list',
         views.create_list_view(models.MachineType, 'machines/machines_items_list.html','items').as_view(),
         name='list_machine_type'),
    path('engine_type/list',
         views.create_list_view(models.EngineType, 'machines/machines_items_list.html','items').as_view(),
         name='list_engine_type'),
    path('transmission_type/list',
         views.create_list_view(models.TransmissionType, 'machines/machines_items_list.html','items').as_view(),
         name='list_transmission_type'),
    path('drive_axle_type/list',
         views.create_list_view(models.DriveAxleType, 'machines/machines_items_list.html','items').as_view(),
         name='list_drive_axle_type'),
    path('steer_axle_type/list',
         views.create_list_view(models.SteerAxleType, 'machines/machines_items_list.html', 'items').as_view(),
         name='list_steer_axle_type'),

    # machine list view
    path('list', views.MachineListView.as_view(), name='list_machine'),
]