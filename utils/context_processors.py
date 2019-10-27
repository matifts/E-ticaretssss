from catalog.models import Category, Product
from E_ticaret import settings 
def Eticaret(request): 
    # categories=Category.objects
    return { 
# /    'active_categories': categories.objects.all(is_active=True), 
    'site_name': settings.SITE_NAME, 
    'meta_keywords': settings.META_KEYWORDS, 
    'meta_description': settings.META_DESCRIPTION, 
    'request': request 
} 