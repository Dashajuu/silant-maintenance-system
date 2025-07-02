from django.urls import path

from . import views


urlpatterns = [
    path('create_manager', views.ManagerCreateView.as_view(), name="create_manager"),
    path('list_managers', views.ManagerListView.as_view(), name="list_managers"),
]