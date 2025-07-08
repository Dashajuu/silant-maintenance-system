from django.urls import path

from . import views


urlpatterns = [
    path('create_account', views.account_creation_home, name='create_account'),
    path('create_manager', views.ManagerCreateView.as_view(), name="create_manager"),
    path('list_managers', views.ManagerListView.as_view(), name="list_managers"),
    path('create_client', views.ClientCreateView.as_view(), name="create_client"),
    path('create_service_master', views.ServiceMasterCreateView.as_view(), name='create_service_master'),
    path('create_contact_person', views.ContactPersonCreateView.as_view(), name='create_contact_person'),
]