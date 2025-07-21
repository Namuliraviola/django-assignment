from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES =[
        ('PENDING','pending'),
        ('COMPLETED','Completed'),
    ]
    
    PRIORITY_CHOICES = [
        ('LOW','Low'),
        ('MEDIUM','Medium'),
        ('HIGH','High'),
    ]
    
    
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='MEDIUM')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    def __str__(self):
       return f"{self.title} ({self.get_priority_display()})- {self.status}"