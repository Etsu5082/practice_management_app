from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Practice(models.Model):
    date = models.DateField()
    max_participants = models.PositiveIntegerField()
    is_closed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.date} (Max: {self.max_participants})"

class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} registered for {self.practice.date}"
