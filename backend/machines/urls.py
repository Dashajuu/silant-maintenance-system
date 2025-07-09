from tkinter.font import names

from django.urls import path

from . import views

urlpatterns = [
    path('create_machine_type', views.MachineTypeCreateView.as_view(), name='create_machine_type')
]