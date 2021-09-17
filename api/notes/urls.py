from django.urls import path
from .import views

urlpatterns = [
    path('', views.NoteCreate.as_view(), name='note-create'),
    path('list/', views.NoteList.as_view(), name='note-list'),
    path('<uuid:pk>/', views.NoteDetail.as_view(), name='note-detail'),
]
