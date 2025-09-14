from django.db import models
import uuid

# Create your models here.

class Product(models.Model):

    CATEGORY_CHOICES = [
    ('jersey', 'Jersey'),
    ('shoes', 'Shoes'),
    ('training', 'Training Wear'),   
    ('accessories', 'Accessories'),  
    ('kids', 'Kids'),        
    ('lifestyle', 'Lifestyle'),   
    ('collectibles', 'Collectibles')
]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']
