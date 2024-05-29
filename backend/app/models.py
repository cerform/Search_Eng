from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    CATEGORY_CHOICES = [
        ('research', 'Research'),
        ('report', 'Report'),
        ('presentation', 'Presentation'),
        ('code', 'Code'),
    ]

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
