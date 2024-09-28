from django.db import models

# Create your models here.
class Product(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE,"Live"),(DELETE,"Delete"))
    title = models.CharField(max_length=200)
    brand = models.CharField(max_length=200,null=True)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to="media/")
    priority = models.IntegerField(default=0)
    deleted_status = models.IntegerField(choices=DELETE_CHOICES,default=0 )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.brand + " " + self.title