from django.urls import include, path
from catalog import views

urlpatterns = [
    # path('catalog.views), 
    path( 'index/', { 'template_name':'catalog/index.html'},name='catalog_home'), 
    # path (('cataegory/','<int:category_slug>/','show_category', {'template_name':'catalog/category.html'},'catalog_category')), 
    # path(('<int:product_slug>/', 'show_product', { 'template_name':'catalog/product.html'},'catalog_product'))
]