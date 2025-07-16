from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings

from . import views


urlpatterns = [
    # accounts' creation urls
    path('create', views.account_creation_home, name='create_account'),
    path('manager/create', views.ManagerCreateView.as_view(), name="create_manager"),
    path('client/create', views.ClientCreateView.as_view(), name="create_client"),
    path('service_master/create', views.ServiceMasterCreateView.as_view(), name='create_service_master'),
    path('contact_person/create', views.ContactPersonCreateView.as_view(), name='create_contact_person'),

    # accounts' update urls
    path('manager/<int:pk>/edit', views.ManagerUpdateView.as_view(), name='update_manager'),
    path('client/<int:pk>/edit', views.ClientUpdateView.as_view(), name='update_client'),
    path('service_master/<int:pk>/edit', views.ServiceMasterUpdateView.as_view(), name='update_service_master'),
    path('contact_person/<int:pk>/edit', views.ContactPersonUpdateView.as_view(), name='update_contact_person'),

    # accounts' delete urls
    path('<int:pk>/delete', views.AccountDeleteView.as_view(), name='delete_account'),

    # authorization's urls
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),

    # profile detail views
    path('manager/<int:pk>', views.ManagerProfileDetailView.as_view(), name='manager_detail'),
    path('client/<int:pk>', views.ClientProfileDetailView.as_view(), name='client_detail'),
    path('service_master/<int:pk>', views.ServiceMasterProfileDetailView.as_view(), name='service_master_detail'),
    path('contact_person/<int:pk>', views.ContactPersonProfileDetailView.as_view(), name='contact_person_detail'),

    # profile list views
    path('manager/list', views.ManagerListView.as_view(), name="list_managers"),
    path('client/list', views.ClientListView.as_view(), name='list_clients'),
    path('service_master/list', views.ServiceMasterListView.as_view(), name='list_serivce_master'),
    path('contact_person/list', views.ContactPersonListView.as_view(), name='list_contact_person'),
]