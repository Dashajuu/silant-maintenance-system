from django.urls import path

from . import views

urlpatterns = [
    # creation urls
    path('create', views.ComplaintCreateView.as_view(), name='create_complaint'),
    path('backdate_complaint/create', views.BackdateComplaintCreateView.as_view(), name='create_backdate_complaint'),
    path('failure_node/create', views.FailureNodeCreateView.as_view(), name='create_failure_node'),
    path('recovery_method/create', views.RecoveryMethodCreateView.as_view(), name='create_recovery_method'),

    # update urls
    path('<int:pk>/update', views.ComplaintUpdateView.as_view(), name='update_complaint'),
]