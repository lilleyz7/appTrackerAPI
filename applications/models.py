from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Application(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('interviewed', 'Interviewed'),
        ('interested', 'Interested'),
        ('offered', 'Offered'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=30)
    details = models.TextField(blank=True)
    location = models.CharField(max_length=50, blank=True )
    listing = models.URLField(blank=True)
    added = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True)
    status = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.job_title} - {self.company}"