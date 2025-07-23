from tkinter.font import names

from django.urls import path, include

from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'complaints', views.ComplaintViewSet)
router.register(r'failure_node', views.FailureNodeViewSet)
router.register(r'recovery_method', views.RecoveryMethodViewSet)


urlpatterns = [
    # api
    path('', include(router.urls)),

    # complaints' creation urls
    path('create', views.ComplaintCreateView.as_view(), name='create_complaint'),
    path('backdate_complaint/create', views.BackdateComplaintCreateView.as_view(), name='create_backdate_complaint'),
    path('failure_node/create', views.FailureNodeCreateView.as_view(), name='create_failure_node'),
    path('recovery_method/create', views.RecoveryMethodCreateView.as_view(), name='create_recovery_method'),

    # complaints' update urls
    path('<int:pk>/update', views.ComplaintUpdateView.as_view(), name='update_complaint'),
    path('backdate_complaint/<int:pk>/update', views.BackdateComplaintUpdateView.as_view(), name='update_backdate_complaint'),
    path('failure_node/<int:pk>/update', views.FailureNodeUpdateView.as_view(), name='update_failure_node'),
    path('recovery_method/<int:pk>/update', views.RecoveryMethodUpdateView.as_view(), name='update_recovery_method'),

    # complaints' delete urls
    path('<int:pk>/delete', views.ComplaintDeleteView.as_view(), name='delete_complaint'),
    path('failure_node/<int:pk>/delete', views.FailureNodeDeleteView.as_view(), name='delete_failure_node'),
    path('recovery_method/<int:pk>/delete', views.RecoveryMethodDeleteView.as_view(), name='delete_recovery_method'),

    # complaints' detail view
    path('failure_node/<int:pk>', views.FailureNodeDetailView.as_view(), name='detail_failure_node'),
    path('recovery_method/<int:pk>', views.RecoveryMethodDetailView.as_view(), name='detail_recovery_method'),
    path('complaint/<int:pk>', views.ComplaintDetailView.as_view(), name='detail_complaint'),

    # complaints' list view
    path('failure_node/list', views.FailureNodeListView.as_view(), name='list_failure_node'),
    path('recovery_method/list', views.RecoveryMethodListView.as_view(), name='list_recovery_method'),
    path('complaint/list', views.ComplaintListView.as_view(), name='list_complaint'),
]