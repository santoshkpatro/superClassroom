from django.contrib import admin
from .models import Room, Assignment, Submission


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('title', 'classroom', 'schedule_on')


class SubmissionInline(admin.StackedInline):
    model = Submission
    extra = 0


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'classroom', 'submission_on')
    inlines = [SubmissionInline]


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'student')
