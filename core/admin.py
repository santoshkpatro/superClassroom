from django.contrib import admin
from .models import Room, Assignment


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('title', 'classroom', 'schedule_on')


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'classroom', 'submission_on')
