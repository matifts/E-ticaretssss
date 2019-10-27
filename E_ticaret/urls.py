"""E_ticaret URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from products import views
from catalog import views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings


admin.site.site_header = "Hos geldiniz Sayin Yonetici"
admin.site.site_title = "Paneli"
admin.site.index_title = "Asmira Grup"

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', TemplateView.as_view(template_name = 'base.html')),
    path('', views.index, name = 'home'),
    path('home/', views.index, name ='home_page'),
    # path('catalog/', include('catalog.urls')),
    # path('catalog/', views.home, name = 'index.html'),
    # path('', include('catalog.urls')),
    # path('', TemplateView.as_view(template_name='base.html')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

