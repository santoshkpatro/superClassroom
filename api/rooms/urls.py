from django.urls import path
from .import views

urlpatterns = [
    path('', views.RoomCreate.as_view(), name='room-create'),
    path('list/', views.RoomList.as_view(), name='room-list'),
    path('<uuid:pk>/', views.RoomDetail.as_view(), name='room-detail'),
]
