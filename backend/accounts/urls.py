from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    # accounts' creation urls
    path('create_account', views.account_creation_home, name='create_account'),
    path('create_manager', views.ManagerCreateView.as_view(), name="create_manager"),
    path('create_client', views.ClientCreateView.as_view(), name="create_client"),
    path('create_service_master', views.ServiceMasterCreateView.as_view(), name='create_service_master'),
    path('create_contact_person', views.ContactPersonCreateView.as_view(), name='create_contact_person'),

    # authorization's urls
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('list_managers', views.ManagerListView.as_view(), name="list_managers"),
]