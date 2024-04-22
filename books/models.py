from django.db import models
from reencrypt.encrypt_fields.fields import encrypt


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    sensitive_data = encrypt(models.CharField(max_length=100))
    author = models.CharField(max_length=100)
    description = models.TextField()
    published_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
