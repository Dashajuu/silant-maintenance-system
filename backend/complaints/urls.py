from django.urls import path

from . import views

urlpatterns = [
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
]