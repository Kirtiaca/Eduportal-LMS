from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Assignment(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assignments")
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.title

class Submission(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="submissions")
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name="submissions")
    file = models.FileField(upload_to="assignments/")
    submitted_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.student.username} - {self.assignment.title}"
