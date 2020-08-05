from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(default='')
    cost = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)