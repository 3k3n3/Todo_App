from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class Todo(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('In progress', 'In progress'),
        ('Cancelled', 'Cancelled'),
        ('Completed', 'Completed'),
    )

    title = models.CharField(max_length=100, unique=True, null=False, blank=False)
    detail = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS, default='Pending')

    class Meta:
        ordering = ['status']

    def __str__(self):
        return self.title
