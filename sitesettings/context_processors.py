from .models import *


def site_settings(request):
    return {
        'brand': Brand.objects.first(),
        'social_links': Social_links.objects.all(),
    }
    