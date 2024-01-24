from django.db import models
from django.utils import timezone

class todo(models.Model):
    title=models.CharField(max_length=30)
    tag=models.CharField(max_length=30)
    venue=models.CharField(max_length=300)
    slot=models.DateTimeField(default=timezone.now())
    description=models.TextField()
# Create your models here.
