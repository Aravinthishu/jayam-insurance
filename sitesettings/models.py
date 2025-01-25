from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    googlemap_url = models.CharField(max_length=1000, blank=True, null=True)
    logo = models.ImageField(upload_to='sitesettings/', null=True, blank=True)
    fevicon = models.ImageField(upload_to='sitesettings/', null=True, blank=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Social_links (models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    icon = models.ImageField(upload_to='sitesettings/social_links', null=True, blank=True)
    
    def __str__(self):
        return self.name