from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    heroslider = HeroSection.objects.first()
    additional_images = HeroImage.objects.all()
    about = AboutSection.objects.first()
    insurance = InsuranceSection.objects.all()
    testimonials = Testimonial.objects.all()
    logos = PartnerLogo.objects.all()
    certificates = Certificate.objects.all()
    
    context = {
        'heroslider': heroslider,
        'about': about,
        'insurance': insurance,
        'testimonials':testimonials,
        'logos':logos,
        'certificates': certificates,
        'additional_images': additional_images,
        
    }
    return render(request, 'index.html', context)