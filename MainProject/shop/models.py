from django.db import models

# Create your models here.

def uploads_url(instance,filename):
    return f'{instance.type}/{filename}'

class Product(models.Model):
    types = [
        ('cat', 'cat'),
        ('dog', 'dog'),
        ('hamster', 'hamster'),
        ('guinea pig', 'guinea pig'),
        ('all kind', 'all kind')
    ]
    prod_types = [
        ('fd', 'feed'),
        ('ac', 'accessories'),
        ('ps', 'peels')
    ]
    title = models.CharField(max_length=35)
    description = models.TextField(default='')
    type = models.CharField(max_length=30, choices=types)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to=uploads_url,height_field='hf', width_field='wf',blank=True, null=True)
    hf = models.IntegerField(default=0)
    wf = models.IntegerField(default=0)
    product_kind = models.CharField(max_length=30, choices=prod_types, default='none')
