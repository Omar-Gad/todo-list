from django.db import models
from config import settings

class Todo(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='todos')
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
