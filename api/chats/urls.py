from django.urls import path
from . import views

urlpatterns = [
    path('classrooms/', views.ChatList.as_view(), name='chat-list')
]
