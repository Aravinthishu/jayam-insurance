from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage
from .models import Contact, HeroSection, HeroImage, AboutSection, InsuranceSection, Testimonial, PartnerLogo, Certificate

def index(request):
    heroslider = HeroSection.objects.first()
    additional_images = HeroImage.objects.all()
    about = AboutSection.objects.first()
    insurance = InsuranceSection.objects.all()
    testimonials = Testimonial.objects.all()
    logos = PartnerLogo.objects.all()
    certificates = Certificate.objects.all()
    
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email", None)
        phone = request.POST.get("phone")
        insurance_type = request.POST.get("insurance_type")

        if not insurance_type:
            messages.error(request, "Please select an insurance type.")
            return redirect("index:index")

        # Save the contact information
        Contact.objects.create(name=name, email=email, phone=phone, insurance=insurance_type)

        # Render email content using an HTML template
        subject = f"New Insurance Request: {insurance_type.capitalize()} Insurance"
        context = {
            'name': name,
            'email': email,
            'phone': phone,
            'insurance_type': insurance_type,
        }
        email_body = render_to_string('contact_email.html', context)

        if insurance_type == 'life' or insurance_type == 'health':
            to_email = [settings.ADMIN_EMAIL2, settings.ADMIN_EMAIL]  # Replace with your email address
        else:
            to_email = [settings.ADMIN_EMAIL]
            
        from_email = settings.ADMIN_EMAIL  # Replace with a valid from address
        
        try:
            email_message = EmailMessage(subject, email_body, from_email, to_email)
            email_message.content_subtype = 'html'  # Set the email content to HTML
            email_message.send()
            print("Email sent successfully!")
            messages.success(request, "Your message has been submitted successfully!")
        except Exception as e:
            print("An error occurred while sending the email:", e)
            messages.error(request, f"An error occurred while sending the email: {e}")

        return redirect("index:index")
    
    context = {
        'heroslider': heroslider,
        'about': about,
        'insurance': insurance,
        'testimonials': testimonials,
        'logos': logos,
        'certificates': certificates,
        'additional_images': additional_images,
    }
    return render(request, 'index.html', context)
