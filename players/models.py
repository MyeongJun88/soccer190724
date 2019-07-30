from django.db import models

class Players(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    age = models.IntegerField()
    view_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to = "images/", null = True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    
    def __str__(self):
        return self.title
        
        
class Player2(models.Model):
    title1 = models.CharField(max_length=200)
    description1 = models.TextField()
    age1 = models.IntegerField(default=0)
    view_count1 = models.IntegerField(default=0)
    
    
    created_at1 = models.DateTimeField(auto_now_add=True)
    updated_at1 = models.DateTimeField(auto_now=True)    
    
    def __str__(self):
        return self.title1
    
