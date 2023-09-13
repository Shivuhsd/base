from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Merchant_Store(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    m_name = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    images = models.ImageField(upload_to='merchant_srote_images/')




class Merchant(models.Model):
    pass


class Products(models.Model):
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    store_id = models.ForeignKey(Merchant_Store, on_delete=models.CASCADE)
    p_name = models.CharField(max_length=200, blank=False)
    price = models.FloatField(blank=False)
    product_description = models.TextField(blank=False)
    product_image = models.ImageField(upload_to='product_image/')

  

