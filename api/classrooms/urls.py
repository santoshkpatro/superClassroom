from django.urls import path
from .import views

urlpatterns = [
    path('', views.ClassroomCreate.as_view(), name='classroom-create'),
    path('list/', views.ClassroomList.as_view(), name='classroom-list'),
    path('<uuid:pk>/', views.ClassroomDetail.as_view(), name='classroom-detail'),
]
