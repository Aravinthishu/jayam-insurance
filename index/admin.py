from django.contrib import admin
from . models import *
# Register your models here.

class HeroImageInline(admin.TabularInline):  # Use TabularInline for a compact table view
    model = HeroImage
    extra = 1  # Number of empty slots for new images
    fields = ['image']  # Fields to display for each image
    verbose_name = "Additional Image"
    verbose_name_plural = "Additional Images"

# Customizing HeroSection in the admin
@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subHead', 'btn_text')  # Fields to display in the admin list view
    search_fields = ('title', 'subHead')  # Fields to enable search functionality
    list_filter = ('title',)  # Add filters in the admin panel
    inlines = [HeroImageInline]  # Include the inline for additional images

admin.site.register(AboutSection)
admin.site.register(InsuranceSection)
admin.site.register(Testimonial)
admin.site.register(PartnerLogo)
admin.site.register(Certificate)
admin.site.register(Contact)