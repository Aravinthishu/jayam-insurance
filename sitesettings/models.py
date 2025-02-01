from django.db import models

# Create your models here.
class Address(models.Model):
    brand = models.ForeignKey('Brand', related_name='additional_addresses', on_delete=models.CASCADE)  # Link to Brand
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.brand.name} - {self.address}"

class Brand(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    googlemap_url = models.CharField(max_length=1000, blank=True, null=True)
    logo = models.ImageField(upload_to='sitesettings/', null=True, blank=True)
    secondary_logo = models.ImageField(upload_to='sitesettings/', null=True, blank=True)
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
    
class updates(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return self.title