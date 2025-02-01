from .models import *


def site_settings(request):
    aditional_addresses = Address.objects.all()
    return {
        'brand': Brand.objects.first(),
        'aditional_addresses': aditional_addresses,
        'social_links': Social_links.objects.all(),
        'updates': updates.objects.all(),
    }
    