from django.shortcuts import  get_object_or_404, render
from catalog.models import Category, Product 
# from django.template import RequestContext 

def index(request): 
    categories=Category.objects
    products = Product.objects
    return render(request, 'index.html', {'categories': categories, 'products': products})

# def home(request):
#     products = Product.objects
#     return render(request, 'index.html')
# def home_page(request):
#     return render(request, 'index.html')

# def show_category(request, category_slug, template_name=""): 
#     c = get_object_or_404(Category, slug=category_slug) 
#     products = c.product_set.all() 
#     page_title = c.name 
#     meta_keywords = c.meta_keywords 
#     meta_description = c.meta_description
#     return render(request, 'catalog/category.html',)    
#     product_slug=()
#     p = get_object_or_404(Product, slug=product_slug) 
#     categories = p.categories.filter(is_active=True)
#     page_title = p.name 
#     meta_keywords = p.meta_keywords 
#     meta_description = p.meta_description 
#     return render(request, )

