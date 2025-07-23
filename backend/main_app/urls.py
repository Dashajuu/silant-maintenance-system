from django.urls import path

from . import views
from machines.views import MachineListView


urlpatterns = [
    path('', MachineListView.as_view(), name='home_page'),
    path('catalogs', views.get_manager_context_data, name='mangers_catalog'),
    path('list_accounts', views.get_manager_accounts_context_data, name='create_account'),
]