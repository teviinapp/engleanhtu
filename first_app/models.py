from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Topic(models.Model):
    top_name=models.CharField(max_length=200, unique=True)
    def __str__(self):
        return self.top_name
        
class Webpage(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.PROTECT)
    name=models.CharField(max_length=200, unique=True)
    url = models.URLField(unique=True)
    def __str__(self):
        return self.name

class Content(models.Model):
    webpage = models.ForeignKey(Webpage,on_delete=models.PROTECT)
    name = models.CharField(max_length=200,unique=True)
    content = models.CharField(max_length=200,unique=True)
    image = models.ImageField(upload_to = "images")
    
    def __str__(self):
        return str(self.name)

class UserProfileInfo(models.Model):
    #create relationship from this class to User
    user = models.OneToOneField(User,on_delete=models.PROTECT)
    #add any more attribute you want
    portfolio = models.URLField(blank=True)
    picture = models.ImageField(upload_to = "images/", blank=True)
    
    def __str__(self):
        return self.user.username 
