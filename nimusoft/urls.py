from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView

from django.urls import re_path as url


urlpatterns = [
    
    path('', include('home.urls', namespace='home')),
    path('accounts/', include('allauth.urls')),

    url(r'^robots\.txt/$', TemplateView.as_view(template_name='robots.txt',
                                            content_type='text/plain')),
    url(r'^sitemap\.xml/$', TemplateView.as_view(template_name='sitemap.xml',
                                            content_type='text/plain')),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

