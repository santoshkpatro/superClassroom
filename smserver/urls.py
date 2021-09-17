from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('api.auth.urls')),
    path('api/classrooms/', include('api.classrooms.urls')),
    path('api/rooms/', include('api.rooms.urls')),
    path('api/notes/', include('api.notes.urls')),
    path('api/assignments/', include('api.assignments.urls')),
]
