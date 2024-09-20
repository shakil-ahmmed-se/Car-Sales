from django.db import models
from django.contrib.auth.models import User
from car_post.models import BuyNow
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    buy_history = models.ManyToManyField(BuyNow)
  
       

