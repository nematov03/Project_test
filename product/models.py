from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    created_at = models.DateField(auto_now = True)
    updated_at = models.DateField(auto_now_add = True)
    
    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateField(auto_now = True)
    updated_at = models.DateField(auto_now_add = True)
    
    def __str__(self) -> str:
        return self.name
