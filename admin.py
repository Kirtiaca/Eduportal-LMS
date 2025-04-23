from django.contrib import admin
from .models import Assignment, Submission

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'deadline', 'created_at')
    search_fields = ('title', 'teacher__username')
    list_filter = ('deadline', 'created_at')

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'student', 'submitted_at')
    search_fields = ('assignment__title', 'student__username')
    list_filter = ('submitted_at',)
