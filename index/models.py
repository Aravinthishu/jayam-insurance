from django.db import models

# Create your models here.


from django.db import models

class HeroSection(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    subHead = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='hero/', null=True, blank=True)  # Keep this for the primary image
    btn_url = models.URLField(max_length=200, blank=True, null=True)
    btn_text = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title


class HeroImage(models.Model):
    hero_section = models.ForeignKey(
        HeroSection, 
        on_delete=models.CASCADE, 
        related_name='additional_images'
    )
    image = models.ImageField(upload_to='hero/multiple/')

    def __str__(self):
        return f"Image for {self.hero_section.title}"

    
class AboutSection(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='about/', null=True, blank=True)
    admin_image = models.ImageField(upload_to='about/', null=True, blank=True)
    admin_name = models.CharField(max_length=200, blank=True, null=True)
    position = models.CharField(max_length=200, blank=True, null=True)
    admin2_image = models.ImageField(upload_to='about/', null=True, blank=True)
    admin2_name = models.CharField(max_length=200, blank=True, null=True)
    admin2_position = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title
    
class InsuranceSection(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='insurance/', null=True, blank=True)
    icon = models.ImageField(upload_to='insurance/', null=True, blank=True)
    icon2 = models.ImageField(upload_to='insurance/', null=True, blank=True)

    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    position = models.CharField(max_length=200, blank=True, null=True)
    testimonial = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='testimonial/', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    
class PartnerLogo(models.Model):
    logo = models.ImageField(upload_to='partner/', null=True, blank=True)
    
    def __str__(self):
        return self.logo.url
    
class ClientLogo(models.Model):
    logo = models.ImageField(upload_to='client/', null=True, blank=True)
    
    def __str__(self):
        return self.logo.url
    
class Certificate(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='certificate/', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    
    INSURANCE_CHOICES = [
        ('Life Insurance', 'Life Insurance'),
        ('Car Insurance', 'Car Insurance'),
        ('Health Insurance', 'Health Insurance'),
        ('Home & Industrial Insurance', 'Home & Industrial Insurance'),
        ('Fire Insurance', 'Fire Insurance'),
        ('Transit Insurance', 'Transit Insurance')
        
    ]

    insurance = models.CharField(
        max_length=200,
        choices=INSURANCE_CHOICES,
        default='Car Insurance'
    )
    
    def __str__(self):
        return self.name
    
class HowToClaim(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='hoe_to_claim/', null=True, blank=True)
    
    def __str__(self):
        return self.name