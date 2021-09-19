from django.urls import path
from .import views

urlpatterns = [
    path('', views.AssignmentCreate.as_view(), name='assign-create'),
    path('list/', views.AssignmentList.as_view(), name='assign-list'),
    path('<uuid:pk>/', views.AssignmentDetail.as_view(), name='assign-detail'),
    path('<uuid:pk>/submission/<str:filename>/', views.AssignmentSubmission.as_view(), name='assign-submit'),
]
