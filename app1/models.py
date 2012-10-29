from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=128)
    phto_url = models.URLField()
    bio =  models.TextField()
    lat = models.FloatField()
    lon = models.FloatField()
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=32)
    profile = models.URLField()
    
