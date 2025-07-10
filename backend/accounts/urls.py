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

    # authorization's urls
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),

    path('list_managers', views.ManagerListView.as_view(), name="list_managers"),
]