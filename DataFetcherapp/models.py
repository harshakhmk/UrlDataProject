from django.db import models
from django.contrib.auth.models import User,auth
# Create your models here.
class URLData(models.Model):
    url=models.URLField(default="google.com",null=False,blank=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    data=models.TextField(max_length=10000)
    